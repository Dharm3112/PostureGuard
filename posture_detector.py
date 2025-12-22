import cv2
import numpy as np
from collections import deque


class PostureDetector:
    def __init__(self, buffer_size=10):
        # Load the pre-trained face detector from OpenCV
        # This comes built-in with opencv-python, no extra download needed usually.
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Buffer to smooth out jitter
        self.y_buffer = deque(maxlen=buffer_size)

        # Baseline: The Y-coordinate of your face when sitting straight
        self.baseline_y = None

    def process_frame(self, frame):
        """
        Detects face and returns the Y-coordinate of the face center.
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

        current_y = None

        if len(faces) > 0:
            # Find the largest face (assuming it's the user)
            largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
            (x, y, w, h) = largest_face

            # Calculate center Y of the face
            center_y = y + (h // 2)
            center_x = x + (w // 2)
            
            # Draw rectangle around face and a center dot
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            # Add to buffer and smooth
            self.y_buffer.append(center_y)
            current_y = sum(self.y_buffer) / len(self.y_buffer)

            # Visualization: Draw the Baseline Line if calibrated
            if self.baseline_y is not None:
                # Draw a line where the "limit" is
                limit_y = int(self.baseline_y + 30)  # 30 pixels threshold
                cv2.line(frame, (0, limit_y), (frame.shape[1], limit_y), (0, 255, 255), 1)
                cv2.putText(frame, "Limit", (10, limit_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        return frame, current_y

    def calibrate(self):
        """Sets the current face height as the 'Good Posture' baseline."""
        if len(self.y_buffer) > 0:
            # Average the last few frames to get a stable baseline
            self.baseline_y = sum(self.y_buffer) / len(self.y_buffer)
            return self.baseline_y
        return None
