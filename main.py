import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import cv2
import time
from plyer import notification
from posture_detector import PostureDetector


class PostureApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Initialize Camera and Detector
        self.cap = cv2.VideoCapture(0)
        self.detector = PostureDetector()

        # Application State
        self.running = True
        self.calibrated = False
        self.slouch_counter = 0
        self.slouch_threshold = 15  # Degrees deviation allowed
        self.time_threshold = 50  # Frames (~2-3 seconds)
        self.frames_bad = 0

        # UI Elements
        self.top_frame = tk.Frame(window)
        self.top_frame.pack(pady=10)

        self.btn_calibrate = Button(self.top_frame, text="Sit Straight & Calibrate", width=25, command=self.calibrate,
                                    bg="#4CAF50", fg="white")
        self.btn_calibrate.pack(side=tk.LEFT, padx=10)

        self.btn_quit = Button(self.top_frame, text="Quit", width=10, command=self.close_app, bg="#f44336", fg="white")
        self.btn_quit.pack(side=tk.LEFT, padx=10)

        self.status_label = Label(window, text="Status: Not Calibrated", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        # Video Canvas
        self.video_label = Label(window)
        self.video_label.pack()

        # Start Loop
        self.update()
        self.window.mainloop()

    def calibrate(self):
        baseline = self.detector.calibrate()
        if baseline:
            self.calibrated = True
            self.status_label.config(text=f"Calibrated! Baseline: {int(baseline)}°", fg="green")
            self.frames_bad = 0

    def check_posture(self, current_angle):
        if not self.calibrated or current_angle is None:
            return

        baseline = self.detector.baseline_angle

        # Check if angle deviates too much (e.g., > 15 degrees from baseline)
        # Note: If you lean forward, angle usually increases or decreases depending on camera side.
        # We check absolute difference.
        if abs(current_angle - baseline) > self.slouch_threshold:
            self.frames_bad += 1
        else:
            self.frames_bad = 0

        # Trigger Alert
        if self.frames_bad > self.time_threshold:
            self.status_label.config(text="⚠️ SLOUCHING DETECTED! ⚠️", fg="red")

            # Send Notification (only once every 100 frames to avoid spam)
            if self.frames_bad % 100 == 0:
                notification.notify(
                    title='PostureGuard',
                    message='Sit up straight! You are hurting your back.',
                    timeout=2
                )
        elif self.frames_bad == 0:
            self.status_label.config(text=f"Posture Good. Angle: {int(current_angle)}°", fg="green")

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            # 1. Process with AI
            frame, angle = self.detector.process_frame(frame)

            # 2. Check Logic
            self.check_posture(angle)

            # 3. Convert to Tkinter Image
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        if self.running:
            self.window.after(15, self.update)

    def close_app(self):
        self.running = False
        self.cap.release()
        self.window.destroy()


# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = PostureApp(root, "PostureGuard AI")