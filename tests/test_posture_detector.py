import unittest
import numpy as np
from posture_detector import PostureDetector


class TestPostureDetector(unittest.TestCase):
    """
    Tests for the PostureDetector class.
    """
    def setUp(self) -> None:
        self.detector = PostureDetector(buffer_size=5)

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

    def test_process_frame_no_face(self) -> None:
        """Checks frame processing does not crash and returns None when no face is present."""
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        processed_frame, current_y = self.detector.process_frame(frame)
        self.assertEqual(processed_frame.shape, (100, 100, 3))
        self.assertIsNone(current_y)


if __name__ == "__main__":
    unittest.main()
