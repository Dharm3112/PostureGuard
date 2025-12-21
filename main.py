import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import cv2
from plyer import notification
from posture_detector import PostureDetector


class PostureApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.cap = cv2.VideoCapture(0)
        self.detector = PostureDetector()

        self.running = True
        self.calibrated = False

        # LOGIC SETTINGS
        self.slouch_threshold = 40  # If face drops 40 pixels, it's a slouch
        self.frames_bad = 0
        self.TIME_TO_ALERT = 50  # Approx 2-3 seconds

        # UI Setup
        self.top_frame = tk.Frame(window)
        self.top_frame.pack(pady=10)

        self.btn_calibrate = Button(self.top_frame, text="Sit Straight & Calibrate", width=25, command=self.calibrate,
                                    bg="#4CAF50", fg="white")
        self.btn_calibrate.pack(side=tk.LEFT, padx=10)

        self.btn_quit = Button(self.top_frame, text="Quit", width=10, command=self.close_app, bg="#f44336", fg="white")
        self.btn_quit.pack(side=tk.LEFT, padx=10)

        self.status_label = Label(window, text="Status: Not Calibrated", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

        self.video_label = Label(window)
        self.video_label.pack()

        self.update()
        self.window.mainloop()

    def calibrate(self):
        baseline = self.detector.calibrate()
        if baseline:
            self.calibrated = True
            self.status_label.config(text=f"Calibrated! Face Y: {int(baseline)}", fg="green")
            self.frames_bad = 0
        else:
            self.status_label.config(text="Calibration Failed: No face detected", fg="orange")

    def check_posture(self, current_y):
        if not self.calibrated or current_y is None:
            return

        baseline = self.detector.baseline_y

        # LOGIC: In images, Y increases as you go DOWN.
        # So, if Current Y > Baseline + Threshold, you have dropped down (slouched).
        if current_y > (baseline + self.slouch_threshold):
            self.frames_bad += 1
        else:
            self.frames_bad = 0

        
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

    def update(self):
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

    def close_app(self):
        self.running = False
        self.cap.release()
        self.window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PostureApp(root, "PostureGuard (Lite Mode)")
