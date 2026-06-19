import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import cv2
from plyer import notification
from posture_detector import PostureDetector
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

        self.cap: cv2.VideoCapture = cv2.VideoCapture(0)
        self.detector: PostureDetector = PostureDetector()

        self.running: bool = True
        self.calibrated: bool = False

        # LOGIC SETTINGS
        self.slouch_threshold: int = 40  # If face drops 40 pixels, it's a slouch
        self.frames_bad: int = 0
        self.TIME_TO_ALERT: int = 50  # Approx 2-3 seconds

        # UI Setup
        self.top_frame: tk.Frame = tk.Frame(window)
        self.top_frame.pack(pady=10)

        self.btn_calibrate: Button = Button(
            self.top_frame, text="Sit Straight & Calibrate", width=25, command=self.calibrate,
            bg="#4CAF50", fg="white"
        )
        self.btn_calibrate.pack(side=tk.LEFT, padx=10)

        self.btn_quit: Button = Button(
            self.top_frame, text="Quit", width=10, command=self.close_app, bg="#f44336", fg="white"
        )
        self.btn_quit.pack(side=tk.LEFT, padx=10)

        self.status_label: Label = Label(window, text="Status: Not Calibrated", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        self.video_label: Label = Label(window)
        self.video_label.pack()

        self.update()
        self.window.mainloop()

    def calibrate(self) -> None:
        """
        Calibrates the target posture baseline from the detector.
        Updates the UI state based on success or failure of face detection.
        """
        baseline = self.detector.calibrate()
        if baseline:
            self.calibrated = True
            self.status_label.config(text=f"Calibrated! Face Y: {int(baseline)}", fg="green")
            self.frames_bad = 0
        else:
            self.status_label.config(text="Calibration Failed: No face detected", fg="orange")

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
            self.status_label.config(text="⚠️ SLOUCHING! SIT UP! ⚠️", fg="red")

            if self.frames_bad % 100 == 0:  # Sound alert occasionally
                notification.notify(
                    title='PostureGuard',
                    message='You are slouching! Sit up straight.',
                    timeout=2
                )
        elif self.frames_bad == 0:
            self.status_label.config(text=f"Posture Good. Deviation: {int(current_y - baseline)}px", fg="green")

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
            self.window.after(15, self.update)

    def close_app(self) -> None:
        """
        Stops the application update loop, releases resources, and closes the window.
        """
        self.running = False
        self.cap.release()
        self.window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PostureApp(root, "PostureGuard (Lite Mode)")

