import sys
import tkinter as tk
from tkinter import Label, Button, messagebox
from PIL import Image, ImageTk
import cv2
from plyer import notification
from posture_detector import PostureDetector
from config_manager import ConfigManager
from logger_config import setup_logger
from exceptions import CameraNotFoundError, ModelLoadError
from typing import Optional
import threading
import time


class CameraStream:
    """
    A helper class that captures video frames from cv2.VideoCapture in a separate daemon thread
    to prevent blocking the Tkinter event loop.
    """
    def __init__(self, cap: cv2.VideoCapture) -> None:
        self.cap = cap  # Set webcam video capture handler instance
        self.frame = None
        self.ret = False
        self.running = True  # Initialize tracking run status active state flag
        # Construct background thread target with daemon mode enabled
        self.thread = threading.Thread(target=self._update, daemon=True)
        self.thread.start()

    def __enter__(self) -> 'CameraStream':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.release()

    def _update(self) -> None:
        try:
            while self.running:
                if self.cap.isOpened():
                    ret, frame = self.cap.read()
                    if ret:
                        self.ret = ret
                        self.frame = frame
                time.sleep(0.01)
        except Exception as e:
            # Silence logging thread error
            pass

    def read(self):
        # Return last captured frame buffer status and frame data tuple
        return self.ret, self.frame

    def release(self) -> None:
        self.running = False
        # Attempt clean shutdown join operations on capture threads sequence
        self.thread.join(timeout=0.5)


class PostureApp:
    """
    Main desktop GUI application for PostureGuard.
    Handles the Tkinter window layout, video frame capture, event loop, and alert logic.
    """
    FONT_FAMILY = "Segoe UI"
    FONT_LARGE = ("Segoe UI", 12, "bold")
    FONT_MEDIUM = ("Segoe UI", 10, "bold")
    FONT_NORMAL = ("Segoe UI", 10)
    FONT_SMALL = ("Segoe UI", 8)
    PAD_X = 15
    PAD_Y = 10
    def __init__(self, window: tk.Tk, window_title: str) -> None:
        """
        Initializes the PostureApp GUI window, camera stream, and detector.

        :param window: The root Tkinter window instance.
        :param window_title: The title text for the window.
        """
        self.window: tk.Tk = window
        self.window.title(window_title)
        # Position the window in the center of the screen
        # Configure default startup window size geometry bounds
        self.window.geometry("700x600")

        # Setup logging
        log_level_val = self.config_manager.get("log_level", "INFO")
        log_level = getattr(sys.modules['logging'], log_level_val, sys.modules['logging'].INFO) if 'logging' in sys.modules else 20
        # Load rotation configs from manager dynamically
        log_bytes = self.config_manager.get("log_max_bytes", 1048576)
        self.logger = setup_logger(level=log_level)
        # Log initialization message parameters settings checks
        self.logger.info("Starting PostureGuard Application...")

        # Set Window Icon
        try:
            icon_img = Image.open("assets/icon.png")
            photo_icon = ImageTk.PhotoImage(icon_img)
            self.window.iconphoto(False, photo_icon)
            self.window.photo_icon = photo_icon  # Keep reference
            self.logger.info("Application window icon loaded successfully.")
        except Exception as e:
            self.logger.warning(f"Could not load application window icon: {e}")

        # Load configuration settings
        # Instantiate dynamic configuration manager helper properties
        self.config_manager: ConfigManager = ConfigManager()
        camera_index: int = self.config_manager.get("camera_index", 0)
        camera_width: int = self.config_manager.get("camera_width", 640)
        camera_height: int = self.config_manager.get("camera_height", 480)

        self.running: bool = True
        self.calibrated: bool = False

        try:
            self.cap: cv2.VideoCapture = cv2.VideoCapture(camera_index)
            if not self.cap.isOpened():
                # Fallback to default index 0 if configured was different and failed
                if camera_index != 0:
                    self.logger.warning(f"Camera index {camera_index} failed, trying fallback index 0...")
                    self.cap = cv2.VideoCapture(0)
                if not self.cap.isOpened():
                    raise CameraNotFoundError(camera_index)
            
            self.logger.info(f"Webcam with index {camera_index} opened successfully.")
            # Initialize webcam resolution frame width settings bounds check
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
            # Initialize webcam resolution frame height settings bounds limit
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

            # Start camera stream background thread
            self.stream: CameraStream = CameraStream(self.cap)

            self.detector: PostureDetector = PostureDetector()
        except (CameraNotFoundError, ModelLoadError) as e:
            self.logger.error(f"Initialization error: {e}")
            messagebox.showerror("Initialization Error", str(e))
            self.running = False
            if hasattr(self, 'cap') and self.cap is not None:
                self.cap.release()
            self.window.destroy()
            return

        # Modern Color Palette Theme Dictionary
        self.theme: dict = {
            "bg": "#1e1e2e",
            "fg": "#cdd6f4",
            "accent": "#89b4fa",
            "success": "#a6e3a1",
            "warning": "#f9e2af",
            "danger": "#f38ba8",
            "btn_bg": "#313244",
            "btn_fg": "#11111b"
        }
        self.bg_color = self.theme["bg"]  # Save local copy bg color
        self.fg_color = self.theme["fg"]  # Save local copy fg color
        self.accent_color = self.theme["accent"]  # Save local copy accent color
        self.success_color = self.theme["success"]  # Save local copy success color
        self.warning_color = self.theme["warning"]  # Save local copy warning color
        self.danger_color = self.theme["danger"]  # Save local copy danger color
        self.btn_bg = self.theme["btn_bg"]  # Save local copy button bg color
        self.btn_fg = self.theme["btn_fg"]  # Save local copy button fg color

        self.window.configure(bg=self.theme["bg"])

        # LOGIC SETTINGS
        self.slouch_threshold: int = self.config_manager.get("slouch_threshold_px", 40)
        self.frames_bad: int = 0
        self.log_counter: int = 0
        self.TIME_TO_ALERT: int = self.config_manager.get("time_to_alert_frames", 50)
        self.frame_delay_ms: int = self.config_manager.get("frame_delay_ms", 15)

        # UI Setup
        self.top_frame: tk.Frame = tk.Frame(window, bg=self.bg_color)
        self.top_frame.pack(pady=self.PAD_Y)

        self.btn_calibrate: Button = Button(
            self.top_frame, text="📸 Sit Straight & Calibrate", width=22, command=self.calibrate,
            bg=self.success_color, fg=self.btn_fg, font=self.FONT_MEDIUM, relief="flat",
            activebackground="#89dceb", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_calibrate.pack(side=tk.LEFT, padx=8)  # Render calibration trigger button

        self.btn_pause: Button = Button(
            self.top_frame, text="⏸️ Pause", width=10, command=self.toggle_monitoring,
            bg=self.accent_color, fg=self.btn_fg, font=self.FONT_MEDIUM, relief="flat",
            activebackground="#b4befe", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_pause.pack(side=tk.LEFT, padx=8)  # Render pause trigger button

        self.btn_settings: Button = Button(
            self.top_frame, text="⚙️ Settings", width=12, command=self.open_settings,
            bg=self.accent_color, fg=self.btn_fg, font=self.FONT_MEDIUM, relief="flat",
            activebackground="#74c7ec", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_settings.pack(side=tk.LEFT, padx=8)  # Render settings trigger button

        self.btn_stats: Button = Button(
            self.top_frame, text="📊 Stats", width=10, command=self.show_statistics,
            bg=self.accent_color, fg=self.btn_fg, font=self.FONT_MEDIUM, relief="flat",
            activebackground="#b4befe", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_stats.pack(side=tk.LEFT, padx=8)  # Render statistics trigger button

        self.btn_quit: Button = Button(
            self.top_frame, text="❌ Quit", width=10, command=self.close_app,
            bg=self.danger_color, fg=self.btn_fg, font=self.FONT_MEDIUM, relief="flat",
            activebackground="#f38ba8", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_quit.pack(side=tk.LEFT, padx=8)  # Render quit trigger button

        # Enable monitoring active state flag by default configuration settings
        self.monitoring_active: bool = True
        self.bind_hover_highlight(self.btn_calibrate, "#89dceb", self.success_color, "Calibrate baseline sitting position")
        self.bind_hover_highlight(self.btn_pause, "#b4befe", self.accent_color, "Pause or resume posture monitoring")
        self.bind_hover_highlight(self.btn_settings, "#74c7ec", self.accent_color, "Open settings configuration panel")
        self.bind_hover_highlight(self.btn_stats, "#b4befe", self.accent_color, "View posture history statistics")
        self.bind_hover_highlight(self.btn_quit, "#f38ba8", self.danger_color, "Quit application")
        
        # Bind Ctrl+C to clean exit
        # Bind Control-C keyboard shortcut triggers for clean closure exits
        self.window.bind("<Control-c>", lambda event: self.close_app(confirm=False))
        # Bind Ctrl+L to calibrate
        # Bind Control-L keyboard shortcut triggers for baseline calibrations
        self.window.bind("<Control-l>", lambda event: self.calibrate())

        self.status_label: Label = Label(
            window, text="Status: Not Calibrated", font=self.FONT_LARGE,
            bg=self.bg_color, fg=self.accent_color
        )
        if not hasattr(self, 'detector') or self.detector.face_cascade.empty():
            self.status_label.config(text="Status: Classifier Load Warning", fg=self.warning_color)
        self.status_label.pack(pady=10)

        # Check for persisted baseline calibration
        # Extract configuration template baseline index variables dynamically
        saved_baseline = self.config_manager.get("saved_baseline_y", None)
        if saved_baseline is not None:
            self.detector.baseline_y = float(saved_baseline)
            self.calibrated = True
            self.status_label.config(text=f"Calibrated! (Loaded baseline Y: {int(saved_baseline)})", fg=self.success_color)
            self.logger.info(f"Loaded saved baseline Face Y: {saved_baseline:.2f} from configuration.")

        # A beautiful frame to hold the webcam feed with a border
        # Construct canvas frame element with standard dark themes borders
        self.video_frame: tk.Frame = tk.Frame(window, bg="#313244", bd=2, relief="groove")
        self.video_frame.pack(padx=self.PAD_X, pady=10)
        
        # Add simple status label bar at the bottom
        # Build application bottom info bar pane container
        self.status_bar: Label = Label(window, text="Camera Stream: Active", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg=self.bg_color, fg=self.fg_color, font=self.FONT_SMALL)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.video_label: Label = Label(self.video_frame, bg="#11111b")
        self.video_label.pack()  # Render label widget inside video frame

        self.update()
        self.window.mainloop()

    def calibrate(self) -> None:
        """
        Calibrates the target posture baseline from the detector.
        Updates the UI state based on success or failure of face detection.
        """
        self.logger.info("Calibration requested...")
        # Execute calibration procedures to establish baseline heights
        baseline = self.detector.calibrate()
        if baseline:
            self.calibrated = True
            self.status_label.config(text=f"Calibrated! Face Y: {int(baseline)}", fg=self.success_color)
            self.frames_bad = 0
            # Persist baseline calibration
            # Persist custom calibration vertical index baseline coordinates to disk config
            self.config_manager.set("saved_baseline_y", baseline)
            self.logger.info(f"App calibrated. Baseline Face Y set and saved to {baseline:.2f}")
        else:
            self.status_label.config(text="Calibration Failed: No face detected", fg=self.warning_color)
            self.logger.warning("App calibration failed: no face detected.")

    def check_posture(self, current_y: Optional[float]) -> None:
        """
        Evaluates the user's posture deviation compared to the calibration baseline.
        Updates the status label and triggers system notifications if poor posture is sustained.

        :param current_y: The current vertical position of the face (smoothed center coordinate).
        """
        if not self.calibrated or current_y is None:
            return

        baseline = self.detector.baseline_y
        if baseline is None:
            return

        # LOGIC: In images, Y increases as you go DOWN.
        # So, if Current Y > Baseline + Threshold, you have dropped down (slouched).
        # Check if vertical pixel offset exceeds standard calibration range
        if current_y > (baseline + self.slouch_threshold):
            self.frames_bad += 1
        else:
            self.frames_bad = 0

        # Alerting
        # Check if slouch tracking duration exceeds limit settings constraints
        if self.frames_bad > self.TIME_TO_ALERT:
            self.status_label.config(text="⚠️ SLOUCHING! SIT UP! ⚠️", fg=self.danger_color)

            if self.frames_bad % 100 == 0:  # Sound alert occasionally
                self.logger.warning(f"Slouching detected for {self.frames_bad} frames. Sending system notification.")
                notification.notify(
                    title='PostureGuard',
                    message='You are slouching! Sit up straight.',
                    timeout=2
                )
        elif self.frames_bad == 0:
            self.status_label.config(text=f"Posture Good. Deviation: {int(current_y - baseline)}px", fg=self.success_color)

        # Periodic posture history logging
        self.log_counter += 1  # Increment periodic log interval checks counters
        if self.log_counter >= 100:
            self.log_counter = 0
            # Write current deviation metric to CSV history storage
            self.log_posture_history(current_y)

    def update(self) -> None:
        """
        Periodic update method that reads frames from the camera, processes them
        using the posture detector, updates GUI widgets, and schedules the next update.
        """
        ret, frame = self.stream.read()
        if ret and frame is not None:
            # Create a copy to prevent thread frame modifications during processing
            frame = frame.copy()
            if self.monitoring_active:
                frame, current_y = self.detector.process_frame(frame)
                self.check_posture(current_y)
            else:
                # Bypassed - draw text indicating paused state
                h, w, _ = frame.shape
                cv2.putText(
                    frame, "MONITORING PAUSED", (w // 2 - 120, h // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 165, 255), 2
                )

            # Convert for Tkinter
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        if self.running:
            # Reschedule layout refresh task checks dynamically
            self.window.after(self.frame_delay_ms, self.update)

    def set_tooltip(self, widget: tk.Widget, text: str) -> None:
        """Helper to bind hover information to a specific widget."""
        widget.bind("<Enter>", lambda e: widget.config(caption=text) if hasattr(widget, 'caption') else None)

    def bind_hover_highlight(self, button: tk.Button, hover_bg: str, normal_bg: str, status_text: str = "") -> None:
        """Applies visual button highlights and updates status bar descriptions on hover."""
        def on_enter(e):
            button.config(bg=hover_bg)
            if status_text and hasattr(self, 'status_bar'):
                self.status_bar.config(text=f"Camera Stream: Active | {status_text}")

        def on_leave(e):
            button.config(bg=normal_bg)
            if hasattr(self, 'status_bar'):
                self.status_bar.config(text="Camera Stream: Active")

        # Bind hover enter action handlers to button widgets
        button.bind("<Enter>", on_enter)
        # Bind hover leave action handlers to button widgets
        button.bind("<Leave>", on_leave)

    def close_app(self, confirm: bool = True) -> None:
        """
        Stops the application update loop, releases resources, and closes the window.
        """
        if confirm:
            if not messagebox.askokcancel("Quit PostureGuard", "Are you sure you want to exit?"):
                return
        # Log application cleanup sequence initiation info
        self.logger.info("Closing application...")
        self.running = False
        self.stream.release()
        self.cap.release()
        self.window.destroy()
        self.logger.info("Application closed successfully.")

    def toggle_monitoring(self) -> None:
        """
        Toggles posture monitoring state between active and paused.
        """
        # Toggle active tracking state configuration settings boolean
        self.monitoring_active = not self.monitoring_active
        if self.monitoring_active:
            # Update pause button layout parameters to active monitoring views
            self.btn_pause.config(text="⏸️ Pause", bg=self.accent_color)
            self.status_label.config(text="Status: Monitoring Active", fg=self.accent_color)
            self.logger.info("Posture monitoring resumed.")
        else:
            # Update pause button layout parameters to paused views
            self.btn_pause.config(text="▶️ Resume", bg=self.success_color)
            self.status_label.config(text="Status: Monitoring Paused", fg=self.warning_color)
            self.logger.info("Posture monitoring paused.")

    def log_posture_history(self, current_y: float) -> None:
        """
        Appends the current posture state (good or slouching) along with timestamp and deviation
        to the local CSV file posture_history.csv.
        """
        import datetime
        import csv
        import os

        if not self.config_manager.get("save_history", True):
            return

        # Verify if local posture logs storage file is present
        file_exists = os.path.exists("posture_history.csv")
        try:
            with open("posture_history.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["timestamp", "deviation_px", "state"])

                state = "Slouching" if self.frames_bad > self.TIME_TO_ALERT else "Good"
                # Compute absolute deviation pixels compared to baseline Y
                deviation = int(current_y - self.detector.baseline_y)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([timestamp, deviation, state])
        except OSError as e:
            self.logger.warning(f"Failed to write posture history to CSV: {e}")

    # Subclass / separated layout for Settings UI
    def open_settings(self) -> None:
        """
        Opens a settings modal dialog allowing the user to configure posture threshold and alert parameters.
        """
        self.logger.info("Opening settings dialog.")
        settings_win = tk.Toplevel(self.window)
        settings_win.title("PostureGuard Settings")
        settings_win.configure(bg=self.bg_color)
        # Bind settings dialog modal relations to main parent window
        settings_win.transient(self.window)
        # Focus GUI events exclusively onto settings dialog modals
        settings_win.grab_set()

        # Labels & Entry fields
        # Threshold
        lbl_threshold = Label(settings_win, text="Slouch Threshold (px):", bg=self.bg_color, fg=self.fg_color, font=self.FONT_NORMAL)
        lbl_threshold.grid(row=0, column=0, padx=self.PAD_X, pady=10, sticky="w")
        # Configure slouch threshold coordinates input fields layout settings
        self.entry_threshold = tk.Entry(settings_win, font=self.FONT_NORMAL, bg="#313244", fg=self.fg_color, insertbackground="white", bd=0)
        self.entry_threshold.insert(0, str(self.slouch_threshold))  # Populates entry threshold value
        self.entry_threshold.grid(row=0, column=1, padx=self.PAD_X, pady=10)

        # Time to Alert
        lbl_alert_time = Label(settings_win, text="Time to Alert (frames):", bg=self.bg_color, fg=self.fg_color, font=self.FONT_NORMAL)
        lbl_alert_time.grid(row=1, column=0, padx=self.PAD_X, pady=10, sticky="w")
        # Configure alert frames limit timing input fields layout settings
        self.entry_alert_time = tk.Entry(settings_win, font=self.FONT_NORMAL, bg="#313244", fg=self.fg_color, insertbackground="white", bd=0)
        self.entry_alert_time.insert(0, str(self.TIME_TO_ALERT))  # Populates entry alert frames value
        self.entry_alert_time.grid(row=1, column=1, padx=self.PAD_X, pady=10)

        # Frame Delay
        lbl_delay = Label(settings_win, text="Frame Delay (ms):", bg=self.bg_color, fg=self.fg_color, font=self.FONT_NORMAL)
        lbl_delay.grid(row=2, column=0, padx=self.PAD_X, pady=10, sticky="w")
        # Configure refresh timings delay inputs fields layout settings
        self.entry_delay = tk.Entry(settings_win, font=self.FONT_NORMAL, bg="#313244", fg=self.fg_color, insertbackground="white", bd=0)
        self.entry_delay.insert(0, str(self.frame_delay_ms))  # Populates entry frame delay timing values
        self.entry_delay.grid(row=2, column=1, padx=self.PAD_X, pady=10)

        # Camera Index selection (Dropdown OptionMenu)
        lbl_camera = Label(settings_win, text="Webcam Device:", bg=self.bg_color, fg=self.fg_color, font=self.FONT_NORMAL)
        lbl_camera.grid(row=3, column=0, padx=self.PAD_X, pady=10, sticky="w")
        
        # Default list of supported camera devices indices dropdown choices
        # Setup choices containing list of available camera device hardware indexes
        self.camera_choices = ["0", "1", "2", "3"]
        self.camera_var = tk.StringVar(settings_win)  # Setup string variable tracker
        current_camera = str(self.config_manager.get("camera_index", 0))  # Retrieve current index settings
        self.camera_var.set(current_camera)  # Set camera variables selection bounds
        
        # Construct camera devices options dropdown selection menu widget
        self.opt_camera = tk.OptionMenu(settings_win, self.camera_var, *self.camera_choices)
        self.opt_camera.config(
            font=("Segoe UI", 9), bg="#313244", fg=self.fg_color,
            activebackground="#313244", activeforeground=self.fg_color,
            highlightthickness=0, bd=0
        )
        self.opt_camera["menu"].config(bg="#313244", fg=self.fg_color)
        self.opt_camera.grid(row=3, column=1, padx=self.PAD_X, pady=10, sticky="ew")

        # Resolution selection (Dropdown OptionMenu)
        lbl_resolution = Label(settings_win, text="Video Resolution:", bg=self.bg_color, fg=self.fg_color, font=self.FONT_NORMAL)
        lbl_resolution.grid(row=4, column=0, padx=self.PAD_X, pady=10, sticky="w")
        
        # Default list of supported video frame resolutions choices
        # Setup choices list containing target frame resolutions selection profiles
        self.resolution_choices = ["320x240", "640x480", "1280x720"]
        self.resolution_var = tk.StringVar(settings_win)  # Setup resolution string variables tracker
        w_val = self.config_manager.get("camera_width", 640)
        h_val = self.config_manager.get("camera_height", 480)
        self.resolution_var.set(f"{w_val}x{h_val}")  # Set default resolution string selections
        
        # Construct frame resolutions options dropdown selection menu widget
        self.opt_resolution = tk.OptionMenu(settings_win, self.resolution_var, *self.resolution_choices)
        self.opt_resolution.config(
            font=("Segoe UI", 9), bg="#313244", fg=self.fg_color,
            activebackground="#313244", activeforeground=self.fg_color,
            highlightthickness=0, bd=0
        )
        self.opt_resolution["menu"].config(bg="#313244", fg=self.fg_color)
        self.opt_resolution.grid(row=4, column=1, padx=self.PAD_X, pady=10, sticky="ew")

        # Buttons Frame
        # Construct settings pane buttons layout frame wrapper container
        btn_frame = tk.Frame(settings_win, bg=self.bg_color)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=self.PAD_Y)

        # Construct save settings dialog modal submission button widgets
        btn_save = Button(
            btn_frame, text="💾 Save", width=10, command=lambda: self.save_settings_from_ui(settings_win),
            bg=self.success_color, fg=self.btn_fg, font=self.FONT_MEDIUM, relief="flat", cursor="hand2"
        )
        btn_save.pack(side=tk.LEFT, padx=10)  # Render save triggers button

        # Construct cancel settings dialog modal triggers button widgets
        btn_cancel = Button(
            btn_frame, text="❌ Cancel", width=10, command=settings_win.destroy,  # Close settings modal window
            bg=self.danger_color, fg=self.btn_fg, font=self.FONT_MEDIUM, relief="flat", cursor="hand2"
        )
        btn_cancel.pack(side=tk.LEFT, padx=10)

    def save_settings_from_ui(self, settings_win: tk.Toplevel) -> None:
        """
        Validates settings entries from the UI. If valid, updates application attributes.
        """
        try:
            # Read slouch threshold entry coordinates validation check values
            threshold = int(self.entry_threshold.get().strip())
            # Read alert time threshold frames checks validation values
            alert_time = int(self.entry_alert_time.get().strip())
            # Read system frame timing delays validation checks values
            delay = int(self.entry_delay.get().strip())

            if not (5 <= threshold <= 200):
                raise ValueError("Slouch threshold must be an integer between 5 and 200 pixels.")
            if not (10 <= alert_time <= 500):
                raise ValueError("Time to alert must be an integer between 10 and 500 frames.")
            if not (5 <= delay <= 200):
                raise ValueError("Frame delay must be an integer between 5 and 200 milliseconds.")
        except ValueError as e:
            self.logger.warning(f"Settings validation failed: {e}")
            messagebox.showwarning("Invalid Input", str(e), parent=settings_win)
            return

        # Updates properties in memory and writes to config file
        self.slouch_threshold = threshold
        self.TIME_TO_ALERT = alert_time
        self.frame_delay_ms = delay
        self.config_manager.set("slouch_threshold_px", threshold)
        self.config_manager.set("time_to_alert_frames", alert_time)
        self.config_manager.set("frame_delay_ms", delay)

        # Camera Index change dynamic reinitialization
        try:
            # Read selected camera index setting value configurations checks
            camera_idx = int(self.camera_var.get())
            old_camera_index = self.config_manager.get("camera_index", 0)
            if camera_idx != old_camera_index:
                self.logger.info(f"Camera index changed from {old_camera_index} to {camera_idx}. Reinitializing camera...")
                self.stream.release()
                self.cap.release()
                self.cap = cv2.VideoCapture(camera_idx)
                if not self.cap.isOpened():
                    raise CameraNotFoundError(camera_idx, "Failed to open newly selected webcam device index.")
                self.config_manager.set("camera_index", camera_idx)
        except Exception as e:
            self.logger.error(f"Error switching camera devices: {e}")
            messagebox.showwarning("Camera Error", f"Warning: Switching to camera index {self.camera_var.get()} failed. Falling back. Detail: {e}", parent=settings_win)

        # Camera Resolution change dynamic update
        try:
            # Read selected resolution constraints values configurations checks
            res_str = self.resolution_var.get()
            if 'x' not in res_str:
                raise ValueError("Invalid resolution format selection.")
            w_str, h_str = res_str.split('x')
            camera_width = int(w_str)
            camera_height = int(h_str)

            # Fetch previously configured screen dimension parameters
            old_w = self.config_manager.get("camera_width", 640)
            old_h = self.config_manager.get("camera_height", 480)

            if camera_width != old_w or camera_height != old_h or camera_idx != old_camera_index:
                self.logger.info(f"Setting camera resolution to {camera_width}x{camera_height}...")
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)
                self.config_manager.set("camera_width", camera_width)
                self.config_manager.set("camera_height", camera_height)

            if camera_idx != old_camera_index:
                self.stream = CameraStream(self.cap)
        except Exception as e:
            self.logger.error(f"Error setting camera resolution: {e}")
            messagebox.showwarning("Resolution Error", f"Could not set resolution to {self.resolution_var.get()}: {e}", parent=settings_win)

        self.logger.info("Settings validated, updated in memory, and saved to file.")
        settings_win.destroy()

    def show_statistics(self) -> None:
        """
        Opens a modal display window showing aggregate posture statistics from stats.py.
        """
        from stats import get_posture_stats

        self.logger.info("Opening posture statistics window.")
        try:
            stats = get_posture_stats("posture_history.csv")
        except Exception as e:
            self.logger.error(f"Error loading stats file: {e}")
            stats = {
                "total_records": 0, "good_count": 0, "slouch_count": 0,
                "good_percent": 0.0, "slouch_percent": 0.0, "avg_deviation": 0.0
            }

        stats_win = tk.Toplevel(self.window)
        stats_win.title("Posture History Statistics")
        stats_win.configure(bg=self.bg_color)
        # Bind stats details modal relations to main parent window
        stats_win.transient(self.window)
        # Focus GUI events exclusively onto stats details modals container
        stats_win.grab_set()

        # Design a clean layout
        lbl_title = Label(stats_win, text="📊 Posture History Overview", font=self.FONT_LARGE, bg=self.bg_color, fg=self.accent_color)
        lbl_title.pack(pady=self.PAD_Y, padx=20)

        # Construct stats dialog grid panel frame layout settings
        frame = tk.Frame(stats_win, bg="#313244", padx=self.PAD_X, pady=self.PAD_Y, bd=1, relief="solid")
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        details = [
            ("Total Records logged:", f"{stats['total_records']}"),
            ("Good Posture Count:", f"{stats['good_count']}"),
            ("Slouching Count:", f"{stats['slouch_count']}"),
            ("Good Posture %:", f"{stats['good_percent']:.1f}%"),
            ("Slouching Posture %:", f"{stats['slouch_percent']:.1f}%"),
            ("Avg Deviation (pixels):", f"{stats['avg_deviation']:.1f} px")
        ]

        for i, (label_text, val_text) in enumerate(details):
            # Create specific label container widgets dynamically
            lbl_l = Label(frame, text=label_text, font=self.FONT_NORMAL, bg="#313244", fg=self.fg_color)
            lbl_l.grid(row=i, column=0, sticky="w", pady=5, padx=5)

            # Highlight values
            color = self.success_color if "Good" in label_text or "total" in label_text.lower() else self.fg_color
            if "%" in val_text and "Slouching" in label_text:
                color = self.danger_color

            lbl_r = Label(frame, text=val_text, font=self.FONT_MEDIUM, bg="#313244", fg=color)
            lbl_r.grid(row=i, column=1, sticky="e", pady=5, padx=5)

        btn_close = Button(
            stats_win, text="Close", width=12, command=stats_win.destroy,  # Exit statistics pane screen
            bg=self.btn_bg, fg=self.fg_color, font=self.FONT_MEDIUM, relief="flat", cursor="hand2"
        )
        btn_close.pack(pady=self.PAD_Y)


def main() -> None:
    """
    Main entry point for starting the PostureGuard application.
    """
    root = tk.Tk()
    app = PostureApp(root, "PostureGuard (Lite Mode)")


if __name__ == "__main__":
    main()

