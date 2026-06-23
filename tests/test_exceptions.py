import unittest
from exceptions import PostureGuardException, CameraNotFoundError, ModelLoadError, LoggingConfigurationError

class TestExceptions(unittest.TestCase):
    def test_exception_properties(self) -> None:
        exc = PostureGuardException("General error")
        self.assertEqual(exc.message, "General error")
        self.assertEqual(exc.error_code, "PostureGuardException")
        
        cam_exc = CameraNotFoundError(1)
        self.assertEqual(cam_exc.error_code, "CameraNotFoundError")
        self.assertIn("camera index 1", cam_exc.message)
        
        log_exc = LoggingConfigurationError("Config failed")
        self.assertEqual(log_exc.error_code, "LoggingConfigurationError")

if __name__ == "__main__":
    unittest.main()
