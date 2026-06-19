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


class PostureApp:
    """
    Main desktop GUI application for PostureGuard.
    Handles the Tkinter window layout, video frame capture, event loop, and alert logic.
    """
    def __init__(self, window: tk.Tk, window_title: str) -> None:
        """
        Initializes the PostureApp GUI window, camera stream, and detector.

        :param window: The root Tkinter window instance.
        :param window_title: The title text for the window.
        """
        self.window: tk.Tk = window
        self.window.title(window_title)

        # Setup logging
        self.logger = setup_logger()
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
        self.config_manager: ConfigManager = ConfigManager()
        camera_index: int = self.config_manager.get("camera_index", 0)
        camera_width: int = self.config_manager.get("camera_width", 640)
        camera_height: int = self.config_manager.get("camera_height", 480)

        self.running: bool = True
        self.calibrated: bool = False

        try:
            self.cap: cv2.VideoCapture = cv2.VideoCapture(camera_index)
            if not self.cap.isOpened():
                raise CameraNotFoundError(camera_index)
            
            self.logger.info(f"Webcam with index {camera_index} opened successfully.")
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

            self.detector: PostureDetector = PostureDetector()
        except (CameraNotFoundError, ModelLoadError) as e:
            self.logger.error(f"Initialization error: {e}")
            messagebox.showerror("Initialization Error", str(e))
            self.running = False
            if hasattr(self, 'cap') and self.cap is not None:
                self.cap.release()
            self.window.destroy()
            return

        # Modern Color Palette (Sleek Dark Theme)
        self.bg_color: str = "#1e1e2e"
        self.fg_color: str = "#cdd6f4"
        self.accent_color: str = "#89b4fa"       # Blue status
        self.success_color: str = "#a6e3a1"      # Green status/calibrate
        self.warning_color: str = "#f9e2af"      # Yellow warnings
        self.danger_color: str = "#f38ba8"       # Red alerts/quit
        self.btn_bg: str = "#313244"
        self.btn_fg: str = "#11111b"

        self.window.configure(bg=self.bg_color)

        # LOGIC SETTINGS
        self.slouch_threshold: int = self.config_manager.get("slouch_threshold_px", 40)
        self.frames_bad: int = 0
        self.TIME_TO_ALERT: int = self.config_manager.get("time_to_alert_frames", 50)
        self.frame_delay_ms: int = self.config_manager.get("frame_delay_ms", 15)

        # UI Setup
        self.top_frame: tk.Frame = tk.Frame(window, bg=self.bg_color)
        self.top_frame.pack(pady=15)

        self.btn_calibrate: Button = Button(
            self.top_frame, text="📸 Sit Straight & Calibrate", width=22, command=self.calibrate,
            bg=self.success_color, fg=self.btn_fg, font=("Segoe UI", 10, "bold"), relief="flat",
            activebackground="#89dceb", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_calibrate.pack(side=tk.LEFT, padx=8)

        self.btn_settings: Button = Button(
            self.top_frame, text="⚙️ Settings", width=12, command=self.open_settings,
            bg=self.accent_color, fg=self.btn_fg, font=("Segoe UI", 10, "bold"), relief="flat",
            activebackground="#74c7ec", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_settings.pack(side=tk.LEFT, padx=8)

        self.btn_quit: Button = Button(
            self.top_frame, text="❌ Quit", width=10, command=self.close_app,
            bg=self.danger_color, fg=self.btn_fg, font=("Segoe UI", 10, "bold"), relief="flat",
            activebackground="#f38ba8", activeforeground=self.btn_fg, cursor="hand2", padx=5, pady=5
        )
        self.btn_quit.pack(side=tk.LEFT, padx=8)

        self.status_label: Label = Label(
            window, text="Status: Not Calibrated", font=("Segoe UI", 12, "bold"),
            bg=self.bg_color, fg=self.accent_color
        )
        self.status_label.pack(pady=10)

        # A beautiful frame to hold the webcam feed with a border
        self.video_frame: tk.Frame = tk.Frame(window, bg="#313244", bd=2, relief="groove")
        self.video_frame.pack(padx=15, pady=10)

        self.video_label: Label = Label(self.video_frame, bg="#11111b")
        self.video_label.pack()

        self.update()
        self.window.mainloop()

    def calibrate(self) -> None:
        """
        Calibrates the target posture baseline from the detector.
        Updates the UI state based on success or failure of face detection.
        """
        self.logger.info("Calibration requested...")
        baseline = self.detector.calibrate()
        if baseline:
            self.calibrated = True
            self.status_label.config(text=f"Calibrated! Face Y: {int(baseline)}", fg=self.success_color)
            self.frames_bad = 0
            self.logger.info(f"App calibrated. Baseline Face Y set to {baseline:.2f}")
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
        if current_y > (baseline + self.slouch_threshold):
            self.frames_bad += 1
        else:
            self.frames_bad = 0

        # Alerting
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

    def update(self) -> None:
        """
        Periodic update method that reads frames from the camera, processes them
        using the posture detector, updates GUI widgets, and schedules the next update.
        """
        ret, frame = self.cap.read()
        if ret:
            frame, current_y = self.detector.process_frame(frame)
            self.check_posture(current_y)

            # Convert for Tkinter
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        if self.running:
            self.window.after(self.frame_delay_ms, self.update)

    def close_app(self) -> None:
        """
        Stops the application update loop, releases resources, and closes the window.
        """
        self.logger.info("Closing application...")
        self.running = False
        self.cap.release()
        self.window.destroy()
        self.logger.info("Application closed successfully.")

    def open_settings(self) -> None:
        """
        Opens a settings modal dialog allowing the user to configure posture threshold and alert parameters.
        """
        self.logger.info("Opening settings dialog.")
        settings_win = tk.Toplevel(self.window)
        settings_win.title("PostureGuard Settings")
        settings_win.configure(bg=self.bg_color)
        settings_win.transient(self.window)
        settings_win.grab_set()

        # Labels & Entry fields
        # Threshold
        lbl_threshold = Label(settings_win, text="Slouch Threshold (px):", bg=self.bg_color, fg=self.fg_color, font=("Segoe UI", 10))
        lbl_threshold.grid(row=0, column=0, padx=15, pady=10, sticky="w")
        self.entry_threshold = tk.Entry(settings_win, font=("Segoe UI", 10), bg="#313244", fg=self.fg_color, insertbackground="white", bd=0)
        self.entry_threshold.insert(0, str(self.slouch_threshold))
        self.entry_threshold.grid(row=0, column=1, padx=15, pady=10)

        # Time to Alert
        lbl_alert_time = Label(settings_win, text="Time to Alert (frames):", bg=self.bg_color, fg=self.fg_color, font=("Segoe UI", 10))
        lbl_alert_time.grid(row=1, column=0, padx=15, pady=10, sticky="w")
        self.entry_alert_time = tk.Entry(settings_win, font=("Segoe UI", 10), bg="#313244", fg=self.fg_color, insertbackground="white", bd=0)
        self.entry_alert_time.insert(0, str(self.TIME_TO_ALERT))
        self.entry_alert_time.grid(row=1, column=1, padx=15, pady=10)

        # Frame Delay
        lbl_delay = Label(settings_win, text="Frame Delay (ms):", bg=self.bg_color, fg=self.fg_color, font=("Segoe UI", 10))
        lbl_delay.grid(row=2, column=0, padx=15, pady=10, sticky="w")
        self.entry_delay = tk.Entry(settings_win, font=("Segoe UI", 10), bg="#313244", fg=self.fg_color, insertbackground="white", bd=0)
        self.entry_delay.insert(0, str(self.frame_delay_ms))
        self.entry_delay.grid(row=2, column=1, padx=15, pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(settings_win, bg=self.bg_color)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)

        btn_save = Button(
            btn_frame, text="💾 Save", width=10, command=lambda: self.save_settings_from_ui(settings_win),
            bg=self.success_color, fg=self.btn_fg, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2"
        )
        btn_save.pack(side=tk.LEFT, padx=10)

        btn_cancel = Button(
            btn_frame, text="❌ Cancel", width=10, command=settings_win.destroy,
            bg=self.danger_color, fg=self.btn_fg, font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2"
        )
        btn_cancel.pack(side=tk.LEFT, padx=10)

    def save_settings_from_ui(self, settings_win: tk.Toplevel) -> None:
        """
        Stub to save UI configuration. To be implemented.
        """
        settings_win.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PostureApp(root, "PostureGuard (Lite Mode)")

