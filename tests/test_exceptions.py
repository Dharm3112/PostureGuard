import unittest
from exceptions import PostureGuardException, CameraNotFoundError, ModelLoadError, LoggingConfigurationError, ConfigurationSaveError, InvalidResolutionError, InvalidThresholdError, InvalidDelayError, InvalidAlertFramesError, InvalidLogBytesError, InvalidBackupCountError, InvalidConfigFormatError, ConfigFileNotFoundError, ConfigWritePermissionError, StatsFileWriteError, StatsFileReadError, HistoryFileNotFoundError, GUIWindowInitializationError, WidgetBindingError, ThemeLoadingError, TooltipConfigurationError, SettingsDialogError, StatisticsWindowError

class TestExceptions(unittest.TestCase):
    def test_exception_properties(self) -> None:
        """Verifies message mapping and class name code parameters for all exception types."""
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

        exc_statisticswindowerror = StatisticsWindowError("Test msg")
        self.assertEqual(exc_statisticswindowerror.error_code, "StatisticsWindowError")
        self.assertEqual(exc_statisticswindowerror.message, "Test msg")

        exc_settingsdialogerror = SettingsDialogError("Test msg")
        self.assertEqual(exc_settingsdialogerror.error_code, "SettingsDialogError")
        self.assertEqual(exc_settingsdialogerror.message, "Test msg")

        exc_tooltipconfigurationerror = TooltipConfigurationError("Test msg")
        self.assertEqual(exc_tooltipconfigurationerror.error_code, "TooltipConfigurationError")
        self.assertEqual(exc_tooltipconfigurationerror.message, "Test msg")

        exc_themeloadingerror = ThemeLoadingError("Test msg")
        self.assertEqual(exc_themeloadingerror.error_code, "ThemeLoadingError")
        self.assertEqual(exc_themeloadingerror.message, "Test msg")

        exc_widgetbindingerror = WidgetBindingError("Test msg")
        self.assertEqual(exc_widgetbindingerror.error_code, "WidgetBindingError")
        self.assertEqual(exc_widgetbindingerror.message, "Test msg")

        exc_guiwindowinitializationerror = GUIWindowInitializationError("Test msg")
        self.assertEqual(exc_guiwindowinitializationerror.error_code, "GUIWindowInitializationError")
        self.assertEqual(exc_guiwindowinitializationerror.message, "Test msg")

        exc_historyfilenotfounderror = HistoryFileNotFoundError("Test msg")
        self.assertEqual(exc_historyfilenotfounderror.error_code, "HistoryFileNotFoundError")
        self.assertEqual(exc_historyfilenotfounderror.message, "Test msg")

        exc_statsfilereaderror = StatsFileReadError("Test msg")
        self.assertEqual(exc_statsfilereaderror.error_code, "StatsFileReadError")
        self.assertEqual(exc_statsfilereaderror.message, "Test msg")

        exc_statsfilewriteerror = StatsFileWriteError("Test msg")
        self.assertEqual(exc_statsfilewriteerror.error_code, "StatsFileWriteError")
        self.assertEqual(exc_statsfilewriteerror.message, "Test msg")

        exc_configwritepermissionerror = ConfigWritePermissionError("Test msg")
        self.assertEqual(exc_configwritepermissionerror.error_code, "ConfigWritePermissionError")
        self.assertEqual(exc_configwritepermissionerror.message, "Test msg")

        exc_configfilenotfounderror = ConfigFileNotFoundError("Test msg")
        self.assertEqual(exc_configfilenotfounderror.error_code, "ConfigFileNotFoundError")
        self.assertEqual(exc_configfilenotfounderror.message, "Test msg")

        exc_invalidconfigformaterror = InvalidConfigFormatError("Test msg")
        self.assertEqual(exc_invalidconfigformaterror.error_code, "InvalidConfigFormatError")
        self.assertEqual(exc_invalidconfigformaterror.message, "Test msg")

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
