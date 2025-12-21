import cv2
import mediapipe as mp
import numpy as np
from collections import deque


class PostureDetector:
    def __init__(self, buffer_size=10):
        # Initialize MediaPipe Pose
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        # Smoothing buffer (stores last 10 angles)
        self.angle_buffer = deque(maxlen=buffer_size)
        self.baseline_angle = 90  # Default, will be updated by calibration

    def find_angle(self, p1, p2):
        """Calculates angle between two points relative to vertical axis."""
        x1, y1 = p1
        x2, y2 = p2
        # Calculate angle (in degrees)
        theta = np.arctan2(y2 - y1, x2 - x1)
        angle = np.abs(theta * 180.0 / np.pi)
        return angle

    def process_frame(self, frame):
        """
        Takes a frame, finds landmarks, and returns the frame with drawings
        plus the calculated average angle.
        """
        # Convert to RGB for MediaPipe
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)

        current_angle = None
        h, w, _ = frame.shape

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates (Left Shoulder: 11, Left Ear: 7)
            # We use LEFT side by default.
            # Ideally user should sit with left side to camera.
            l_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value]
            l_ear = landmarks[self.mp_pose.PoseLandmark.LEFT_EAR.value]

            # Convert to pixel coordinates
            shoulder_pt = (int(l_shoulder.x * w), int(l_shoulder.y * h))
            ear_pt = (int(l_ear.x * w), int(l_ear.y * h))

            # Draw points and line
            cv2.circle(frame, shoulder_pt, 7, (255, 255, 255), -1)
            cv2.circle(frame, ear_pt, 7, (255, 255, 255), -1)
            cv2.line(frame, shoulder_pt, ear_pt, (0, 255, 0), 2)

            # Calculate Angle
            raw_angle = self.find_angle(shoulder_pt, ear_pt)
            self.angle_buffer.append(raw_angle)

            # Smooth the angle
            current_angle = sum(self.angle_buffer) / len(self.angle_buffer)

        return frame, current_angle

    def calibrate(self):
        """Sets the current average angle as the 'Good Posture' baseline."""
        if len(self.angle_buffer) > 0:
            self.baseline_angle = sum(self.angle_buffer) / len(self.angle_buffer)
            return self.baseline_angle
        return None