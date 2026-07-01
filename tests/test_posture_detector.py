import unittest
import numpy as np
from posture_detector import PostureDetector


class TestPostureDetector(unittest.TestCase):
    """
    Tests for the PostureDetector class.
    """
    def setUp(self) -> None:
        # Set buffer boundaries parameter limit
        self.detector = PostureDetector(buffer_size=5)

    # Test calibration status transitions checks
    def test_is_calibrated(self) -> None:
        """Verifies is_calibrated behavior."""
        self.assertFalse(self.detector.is_calibrated)
        self.detector.baseline_y = 150.0
        self.assertTrue(self.detector.is_calibrated)

    def test_consecutive_failures_reset_on_calibrate(self) -> None:
        """Verifies that calibration resets consecutive failures count."""
        self.detector.consecutive_failures = 10
        self.detector.y_buffer.append(100.0)
        self.detector.calibrate()
        self.assertEqual(self.detector.consecutive_failures, 0)

    def test_initialization(self) -> None:
        """Verifies buffer limits and baseline Y defaults on setup."""
        self.assertEqual(self.detector.y_buffer.maxlen, 5)
        self.assertIsNone(self.detector.baseline_y)

    def test_calibrate_empty_buffer(self) -> None:
        """Verifies calibrate returns None if buffer is empty."""
        self.assertIsNone(self.detector.calibrate())

    def test_calibrate_with_buffer(self) -> None:
        """Verifies calibrate averages buffer contents properly."""
        self.detector.y_buffer.append(100.0)
        self.detector.y_buffer.append(102.0)
        self.detector.y_buffer.append(98.0)
        baseline = self.detector.calibrate()
        self.assertEqual(baseline, 100.0)
        self.assertEqual(self.detector.baseline_y, 100.0)

    def test_is_slouching(self) -> None:
        """Checks slouch detection method behaves correctly based on threshold offsets."""
        self.detector.baseline_y = 100.0
        # Slouch threshold is 30px
        self.assertTrue(self.detector.is_slouching(135.0, 30.0))
        self.assertFalse(self.detector.is_slouching(120.0, 30.0))
        self.assertFalse(self.detector.is_slouching(80.0, 30.0))

    def test_buffer_boundary(self) -> None:
        """Verifies buffer sliding average calculation and max size preservation."""
        for val in [10, 20, 30, 40, 50, 60]:
            self.detector.y_buffer.append(val)
        self.assertEqual(len(self.detector.y_buffer), 5)
        # Average of 20, 30, 40, 50, 60 = 40.0
        self.assertEqual(self.detector._get_average_y(), 40.0)

    def test_empty_frame_handling(self) -> None:
        """Verifies process_frame handles empty/invalid images gracefully."""
        empty_frame = np.zeros((0, 0, 0), dtype=np.uint8)
        frame, current_y = self.detector.process_frame(empty_frame)
        self.assertIsNone(current_y)

    def test_process_frame_no_face(self) -> None:
        """Checks frame processing does not crash and returns None when no face is present."""
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        processed_frame, current_y = self.detector.process_frame(frame)
        self.assertEqual(processed_frame.shape, (100, 100, 3))
        self.assertIsNone(current_y)

    def test_reset_buffer(self) -> None:
        """Verifies reset_buffer clears buffer, baseline_y, and failures count."""
        self.detector.y_buffer.append(120.0)
        self.detector.baseline_y = 110.0
        self.detector.consecutive_failures = 5
        self.detector.reset_buffer()
        self.assertEqual(len(self.detector.y_buffer), 0)
        self.assertIsNone(self.detector.baseline_y)
        self.assertEqual(self.detector.consecutive_failures, 0)

if __name__ == "__main__":
    unittest.main()
