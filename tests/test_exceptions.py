import unittest
from exceptions import PostureGuardException, CameraNotFoundError, ModelLoadError, LoggingConfigurationError, ConfigurationSaveError, InvalidResolutionError, InvalidThresholdError, InvalidDelayError, InvalidAlertFramesError, InvalidLogBytesError, InvalidBackupCountError

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

        save_exc = ConfigurationSaveError("Save failed")
        self.assertEqual(save_exc.error_code, "ConfigurationSaveError")
        self.assertEqual(save_exc.message, "Save failed")

        exc_invalidbackupcounterror = InvalidBackupCountError("Test msg")
        self.assertEqual(exc_invalidbackupcounterror.error_code, "InvalidBackupCountError")
        self.assertEqual(exc_invalidbackupcounterror.message, "Test msg")

        exc_invalidlogbyteserror = InvalidLogBytesError("Test msg")
        self.assertEqual(exc_invalidlogbyteserror.error_code, "InvalidLogBytesError")
        self.assertEqual(exc_invalidlogbyteserror.message, "Test msg")

        exc_invalidalertframeserror = InvalidAlertFramesError("Test msg")
        self.assertEqual(exc_invalidalertframeserror.error_code, "InvalidAlertFramesError")
        self.assertEqual(exc_invalidalertframeserror.message, "Test msg")

        exc_invaliddelayerror = InvalidDelayError("Test msg")
        self.assertEqual(exc_invaliddelayerror.error_code, "InvalidDelayError")
        self.assertEqual(exc_invaliddelayerror.message, "Test msg")

        exc_invalidthresholderror = InvalidThresholdError("Test msg")
        self.assertEqual(exc_invalidthresholderror.error_code, "InvalidThresholdError")
        self.assertEqual(exc_invalidthresholderror.message, "Test msg")

        exc_invalidresolutionerror = InvalidResolutionError("Test msg")
        self.assertEqual(exc_invalidresolutionerror.error_code, "InvalidResolutionError")
        self.assertEqual(exc_invalidresolutionerror.message, "Test msg")

if __name__ == "__main__":
    unittest.main()
