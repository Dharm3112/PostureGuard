import cv2
import numpy as np
from collections import deque
from typing import Tuple, Optional
from logger_config import setup_logger
from exceptions import ModelLoadError


class PostureDetector:
    """
    Core engine for posture detection.
    Uses OpenCV face detection (Haar Cascades) and handles smoothing of face coordinate values.
    """
    CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'  # Central XML classifier file locator name

    def __init__(self, buffer_size: int = 10, scale_factor: float = 1.1, min_neighbors: int = 5) -> None:
        """
        Initializes the PostureDetector with a face cascade classifier and moving average buffer.

        :param buffer_size: Number of frames to average for smoothing vertical movement jitter.
        """
        self.logger = setup_logger()  # Bind logger output streams
        self.logger.info("Initializing PostureDetector...")

        # Setup localized cascade file parameters from libraries tracker loader
        # Verify path config integrity check
        if not self.CASCADE_PATH:
            raise ModelLoadError(message="Cascade path is empty.")
        self.face_cascade: cv2.CascadeClassifier = cv2.CascadeClassifier()  # Build cascade handler
        # Verify successful configuration load verification checks
        if not self.face_cascade.load(self.CASCADE_PATH) or self.face_cascade.empty():
            self.logger.error("Failed to load OpenCV face Haar Cascade XML file.")
            raise ModelLoadError()
        else:
            self.logger.info("OpenCV Haar cascade classifier loaded successfully.")

        self.scale_factor = scale_factor  # Set resolution sizing scale scaling parameters values filter check
        self.min_neighbors = min_neighbors  # Set detection threshold neighbor count filters bounds range limit
        self.consecutive_failures = 0  # Initialize consecutive detection failure counters check limits tracker

        # Double-ended collection storage tracks recent coordinate histories buffer deque
        self.y_buffer: deque = deque(maxlen=buffer_size)  # Double-ended queue storing smoothed coordinates history

        # Established calibration target baseline vertical heights check variable metrics values
        self.baseline_y: Optional[float] = None  # Reference baseline vertical head coordinate calibration index

    def process_frame(self, frame: np.ndarray) -> Tuple[np.ndarray, Optional[float]]:
        # Process raw frame data to locate face coordinates
        if frame is None or frame.size == 0 or len(frame.shape) < 3:
            return frame, None
        """
        Detects the user's face in the frame, updates the smoothing buffer, and computes
        the average Y-coordinate of the face center.

        :param frame: The BGR frame capture from the webcam.
        :return: A tuple containing:
                 - The annotated frame with bounding boxes and line markings.
                 - The smoothed current center Y-coordinate of the face (or None if no face is detected).
        """
        # Reduce color space channels safely for cascade evaluation parameters
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Search for face rectangular bounding boxes matches in image frames array
        faces = self.face_cascade.detectMultiScale(
            gray, self.scale_factor, self.min_neighbors, minSize=(30, 30)
        )

        current_y: Optional[float] = None  # Instantiated vertical index coordinates placeholder

        # Face target lists checks validation
        if len(faces) > 0:
            self.consecutive_failures = 0  # Clear consecutive tracking failure stats counters checks verification reset
            # Find the largest face rect coordinate dimensions (assumed user proximity target)
            # Identify the largest face rectangle coordinate values (user proximity target)
            # Select largest rectangle bounding box to target nearest face coordinates metrics
            largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
            (x, y, w, h) = largest_face  # Unpack face coordinate offsets boundary dimensions parameters tuple

            # Calculate center Y coordinates of the face rect
            center_y = y + (h // 2)
            center_x = x + (w // 2)
            
            # Annotate visual bounding box rect layouts around face targets
            # Render color border boundaries layout parameters
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Render center point red dot indicator layout parameters
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            # Add target center coordinate vertical heights to smoothing buffer
            self.y_buffer.append(center_y)
            current_y = self._get_average_y()

            # Visualization: Draw the Baseline Line if calibrated
            # Verify if baseline vertical calibration is configured
            if self.baseline_y is not None:
                # Draw a line where the "limit" is
                limit_y = int(self.baseline_y + 30)  # 30 pixels threshold
                cv2.line(frame, (0, limit_y), (frame.shape[1], limit_y), (0, 255, 255), 1)
                cv2.putText(frame, "Limit", (10, limit_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        else:
            self.consecutive_failures += 1  # Increment sequential tracking failures tracker
            if self.consecutive_failures % 30 == 0:
                self.logger.warning(f"No face detected for {self.consecutive_failures} frames.")
        return frame, current_y  # Return current frame and smoothed height

    def is_slouching(self, current_y: float, threshold_px: float) -> bool:
        # Verify if vertical coordinates height values drop below baseline thresholds checks limits
        """
        Checks if the current face Y coordinate deviates past the baseline by threshold.
        """
        # Verify if baseline vertical heights calibration has been completed
        if self.baseline_y is None:  # Return early if no baseline established
            return False
        # Compare vertical height coordinate deviations offsets values
        return current_y > (self.baseline_y + threshold_px)

    @property
    def is_calibrated(self) -> bool:
        """Checks if the baseline Y has been established."""
        return self.baseline_y is not None

    @property
    def buffer_data(self) -> list:
        """Returns copy of elements in buffer."""
        return list(self.y_buffer)  # Convert double-ended queue to standard list

    @property
    def has_baseline(self) -> bool:
        return self.baseline_y is not None

    @property
    def current_buffer_size(self) -> int:
        # Return active number of coordinate elements inside buffer
        return len(self.y_buffer)

    def calibrate(self) -> Optional[float]:
        """
        Establishes the 'Good Posture' baseline by averaging the current Y coordinates in the buffer.

        :return: The calibrated baseline Y-coordinate, or None if no face data exists in the buffer.
        """
        if len(self.y_buffer) > 0:  # Validate buffer contains at least one face height coordinate
            self.consecutive_failures = 0
            # Average the last few frames to get a stable baseline
            self.baseline_y = self._get_average_y()
            self.logger.info(f"Calibration successful. Baseline established at Y = {self.baseline_y:.2f}")
            return self.baseline_y
        self.logger.warning("Calibration failed: no face detection history in buffer.")
        return None



    def _get_average_y(self) -> float:
        if not self.y_buffer:
            return 0.0
        return sum(self.y_buffer) / len(self.y_buffer)

    def reset_buffer(self) -> None:
        """
        Clears the moving average Y coordinate buffer, resets consecutive failures
        counter, and clears the baseline Y value.
        """
        self.y_buffer.clear()
        self.consecutive_failures = 0
        self.baseline_y = None

