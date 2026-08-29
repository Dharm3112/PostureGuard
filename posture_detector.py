import cv2  # Import OpenCV library module package tool
import numpy as np  # Import NumPy numerical array library module package
from collections import deque  # Import double-ended queue collection class helper structure
from typing import Tuple, Optional  # Import typing tuple and optional annotations type
from logger_config import setup_logger  # Import logger setup utility function module
from exceptions import ModelLoadError  # Import ModelLoadError custom exception class


class PostureDetector:
    """
    Core engine for posture detection.
    Uses OpenCV face detection (Haar Cascades) and handles smoothing of face coordinate values.
    """
    CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'  # Central XML classifier file locator name path locator path

    def __init__(self, buffer_size: int = 10, scale_factor: float = 1.1, min_neighbors: int = 5) -> None:
        """
        Initializes the PostureDetector with a face cascade classifier and moving average buffer.

        :param buffer_size: Number of frames to average for smoothing vertical movement jitter.
        """
        self.logger = setup_logger()  # Bind logger output streams helper instance
        self.logger.info("Initializing PostureDetector...")  # Log detector initialization start message item log

        # Setup localized cascade file parameters from libraries tracker loader
        # Verify path config integrity check
        if not self.CASCADE_PATH:  # Check cascade path exists check check
            raise ModelLoadError(message="Cascade path is empty.")
        self.face_cascade: cv2.CascadeClassifier = cv2.CascadeClassifier()  # Build cascade handler instance object helper object
        # Verify successful configuration load verification checks
        if not self.face_cascade.load(self.CASCADE_PATH) or self.face_cascade.empty():
            self.logger.error("Failed to load OpenCV face Haar Cascade XML file.")
            raise ModelLoadError()
        else:
            self.logger.info("OpenCV Haar cascade classifier loaded successfully.")  # Log success message

        self.scale_factor = scale_factor  # Set resolution sizing scale scaling parameters values filter configuration setting value setting param
        self.min_neighbors = min_neighbors  # Set detection threshold neighbor count filters bounds range value setting value setting param
        self.consecutive_failures = 0  # Initialize consecutive detection failure counters check limits value setting value setting counter

        # Double-ended collection storage tracks recent coordinate histories buffer deque
        self.y_buffer: deque = deque(maxlen=buffer_size)  # Double-ended queue storing smoothed coordinates history deque queue

        # Established calibration target baseline vertical heights check variable metrics values
        self.baseline_y: Optional[float] = None  # Reference baseline vertical head coordinate calibration index value value

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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale for detection matrix

        # Search for face rectangular bounding boxes matches in image frames array
        faces = self.face_cascade.detectMultiScale(  # Detect faces using cascade classifier
            gray, self.scale_factor, self.min_neighbors, minSize=(30, 30)
        )

        current_y: Optional[float] = None  # Instantiated vertical index coordinates placeholder variable item

        # Face target lists checks validation
        if len(faces) > 0:
            self.consecutive_failures = 0  # Clear consecutive tracking failure stats counters checks verification reset reset
            # Find the largest face rect coordinate dimensions (assumed user proximity target)
            # Identify the largest face rectangle coordinate values (user proximity target)
            # Select largest rectangle bounding box to target nearest face coordinates metrics
            largest_face = max(faces, key=lambda rect: rect[2] * rect[3])  # Select largest detected face rect
            (x, y, w, h) = largest_face  # Unpack face coordinate offsets boundary dimensions parameters tuple item values

            # Calculate center Y coordinates of the face rect
            center_y = y + (h // 2)  # Calculate face box center vertical position coordinate
            center_x = x + (w // 2)  # Calculate face box center horizontal position coordinate
            
            # Annotate visual bounding box rect layouts around face targets
            # Render color border boundaries layout parameters
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw green rectangle around face bounding
            # Render center point red dot indicator layout parameters
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)  # Draw red circle at face center point

            # Add target center coordinate vertical heights to smoothing buffer
            self.y_buffer.append(center_y)  # Append face center Y coordinate to buffer queue
            current_y = self._get_average_y()  # Compute moving average Y coordinate value

            # Visualization: Draw the Baseline Line if calibrated
            # Verify if baseline vertical calibration is configured
            if self.baseline_y is not None:
                # Draw a line where the "limit" is
                limit_y = int(self.baseline_y + 30)  # Calculate slouch limit Y line position
                cv2.line(frame, (0, limit_y), (frame.shape[1], limit_y), (0, 255, 255), 1)  # Render horizontal limit line
                cv2.putText(frame, "Limit", (10, limit_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)  # Annotate text label

        else:
            self.consecutive_failures += 1  # Increment sequential tracking failures tracker parameter counter
            if self.consecutive_failures % 30 == 0:
                self.logger.warning(f"No face detected for {self.consecutive_failures} frames.")
        return frame, current_y  # Return current frame and smoothed height values tuple

    def is_slouching(self, current_y: float, threshold_px: float) -> bool:  # Check if face Y position exceeds calibrated threshold check
        # Verify if vertical coordinates height values drop below baseline thresholds checks limits
        """
        Checks if the current face Y coordinate deviates past the baseline by threshold.
        """
        # Verify if baseline vertical heights calibration has been completed
        if self.baseline_y is None:  # Return early if no baseline established constraints check
            return False
        # Compare vertical height coordinate deviations offsets values
        return current_y > (self.baseline_y + threshold_px)

    @property
    def is_calibrated(self) -> bool:  # Property returning whether baseline Y has been calibrated check
        """Checks if the baseline Y has been established."""
        return self.baseline_y is not None

    @property
    def buffer_data(self) -> list:  # Property returning list copy of moving average buffer data list
        """Returns copy of elements in buffer."""
        return list(self.y_buffer)  # Convert double-ended queue to standard list copy

    @property
    def has_baseline(self) -> bool:
        return self.baseline_y is not None

    @property
    def current_buffer_size(self) -> int:
        # Return active number of coordinate elements inside buffer
        return len(self.y_buffer)

    def calibrate(self) -> Optional[float]:  # Establishes good posture baseline from buffer coordinates method
        """
        Establishes the 'Good Posture' baseline by averaging the current Y coordinates in the buffer.

        :return: The calibrated baseline Y-coordinate, or None if no face data exists in the buffer.
        """
        if len(self.y_buffer) > 0:  # Validate buffer contains at least one face height coordinate
            self.consecutive_failures = 0
            # Average the last few frames to get a stable baseline
            self.baseline_y = self._get_average_y()  # Set baseline Y to smoothed average
            self.logger.info(f"Calibration successful. Baseline established at Y = {self.baseline_y:.2f}")  # Log calibration success
            return self.baseline_y
        self.logger.warning("Calibration failed: no face detection history in buffer.")  # Log calibration failure
        return None



    def _get_average_y(self) -> float:
        if not self.y_buffer:  # Check if buffer is empty
            return 0.0
        return sum(self.y_buffer) / len(self.y_buffer)  # Calculate arithmetic mean Y float

    def reset_buffer(self) -> None:  # Clear smoothing buffer and reset calibration baseline method
        """
        Clears the moving average Y coordinate buffer, resets consecutive failures
        counter, and clears the baseline Y value.
        """
        self.y_buffer.clear()  # Purge all items from moving average buffer queue lists queue
        self.consecutive_failures = 0
        self.baseline_y = None  # Reset baseline Y coordinate value to None indicator tag indicator

