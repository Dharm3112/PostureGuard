import unittest
from exceptions import PostureGuardException, CameraNotFoundError, ModelLoadError, LoggingConfigurationError, ConfigurationSaveError, InvalidResolutionError, InvalidThresholdError, InvalidDelayError, InvalidAlertFramesError, InvalidLogBytesError, InvalidBackupCountError, InvalidConfigFormatError, ConfigFileNotFoundError, ConfigWritePermissionError, StatsFileWriteError, StatsFileReadError, HistoryFileNotFoundError, GUIWindowInitializationError, WidgetBindingError, ThemeLoadingError, TooltipConfigurationError, SettingsDialogError, StatisticsWindowError, CameraStreamThreadError, FrameProcessingError, BaselineNotEstablishedError, SoundNotificationError, LoggerConfigResetError, CSVFormatMismatchError, GUIThemeKeyError, WidgetAlignmentError, MenuOptionIndexError, CameraReinitializationError, ResolutionSwitchError, VideoFrameEmptyError, AudioAlertTriggerError, NotificationServiceError, CSVFieldFormatError, CSVWriterAccessError, JSONBackupWriteError, JSONRestoreFallbackError, CanvasWidgetRenderError, DynamicTooltipTimeoutError, SettingsWindowDismissalError, DatabaseStatsRowFormatError, LogRotationIntervalError, SoundPlayerNotAvailableError, CalibrationBaselineMismatchError, CascadeModelFileFormatError, JSONSchemaValidationError, ConfigurationWriteConflictError, SystemNotificationPermissionError, CameraResourceReleaseError

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

        exc_cameraresourcereleaseerror = CameraResourceReleaseError("Test msg")
        self.assertEqual(exc_cameraresourcereleaseerror.error_code, "CameraResourceReleaseError")
        self.assertEqual(exc_cameraresourcereleaseerror.message, "Test msg")

        exc_systemnotificationpermissionerror = SystemNotificationPermissionError("Test msg")
        self.assertEqual(exc_systemnotificationpermissionerror.error_code, "SystemNotificationPermissionError")
        self.assertEqual(exc_systemnotificationpermissionerror.message, "Test msg")

        exc_configurationwriteconflicterror = ConfigurationWriteConflictError("Test msg")
        self.assertEqual(exc_configurationwriteconflicterror.error_code, "ConfigurationWriteConflictError")
        self.assertEqual(exc_configurationwriteconflicterror.message, "Test msg")

        exc_jsonschemavalidationerror = JSONSchemaValidationError("Test msg")
        self.assertEqual(exc_jsonschemavalidationerror.error_code, "JSONSchemaValidationError")
        self.assertEqual(exc_jsonschemavalidationerror.message, "Test msg")

        exc_cascademodelfileformaterror = CascadeModelFileFormatError("Test msg")
        self.assertEqual(exc_cascademodelfileformaterror.error_code, "CascadeModelFileFormatError")
        self.assertEqual(exc_cascademodelfileformaterror.message, "Test msg")

        exc_calibrationbaselinemismatcherror = CalibrationBaselineMismatchError("Test msg")
        self.assertEqual(exc_calibrationbaselinemismatcherror.error_code, "CalibrationBaselineMismatchError")
        self.assertEqual(exc_calibrationbaselinemismatcherror.message, "Test msg")

        exc_soundplayernotavailableerror = SoundPlayerNotAvailableError("Test msg")
        self.assertEqual(exc_soundplayernotavailableerror.error_code, "SoundPlayerNotAvailableError")
        self.assertEqual(exc_soundplayernotavailableerror.message, "Test msg")

        exc_logrotationintervalerror = LogRotationIntervalError("Test msg")
        self.assertEqual(exc_logrotationintervalerror.error_code, "LogRotationIntervalError")
        self.assertEqual(exc_logrotationintervalerror.message, "Test msg")

        exc_databasestatsrowformaterror = DatabaseStatsRowFormatError("Test msg")
        self.assertEqual(exc_databasestatsrowformaterror.error_code, "DatabaseStatsRowFormatError")
        self.assertEqual(exc_databasestatsrowformaterror.message, "Test msg")

        exc_settingswindowdismissalerror = SettingsWindowDismissalError("Test msg")
        self.assertEqual(exc_settingswindowdismissalerror.error_code, "SettingsWindowDismissalError")
        self.assertEqual(exc_settingswindowdismissalerror.message, "Test msg")

        exc_dynamictooltiptimeouterror = DynamicTooltipTimeoutError("Test msg")
        self.assertEqual(exc_dynamictooltiptimeouterror.error_code, "DynamicTooltipTimeoutError")
        self.assertEqual(exc_dynamictooltiptimeouterror.message, "Test msg")

        exc_canvaswidgetrendererror = CanvasWidgetRenderError("Test msg")
        self.assertEqual(exc_canvaswidgetrendererror.error_code, "CanvasWidgetRenderError")
        self.assertEqual(exc_canvaswidgetrendererror.message, "Test msg")

        exc_jsonrestorefallbackerror = JSONRestoreFallbackError("Test msg")
        self.assertEqual(exc_jsonrestorefallbackerror.error_code, "JSONRestoreFallbackError")
        self.assertEqual(exc_jsonrestorefallbackerror.message, "Test msg")

        exc_jsonbackupwriteerror = JSONBackupWriteError("Test msg")
        self.assertEqual(exc_jsonbackupwriteerror.error_code, "JSONBackupWriteError")
        self.assertEqual(exc_jsonbackupwriteerror.message, "Test msg")

        exc_csvwriteraccesserror = CSVWriterAccessError("Test msg")
        self.assertEqual(exc_csvwriteraccesserror.error_code, "CSVWriterAccessError")
        self.assertEqual(exc_csvwriteraccesserror.message, "Test msg")

        exc_csvfieldformaterror = CSVFieldFormatError("Test msg")
        self.assertEqual(exc_csvfieldformaterror.error_code, "CSVFieldFormatError")
        self.assertEqual(exc_csvfieldformaterror.message, "Test msg")

        exc_notificationserviceerror = NotificationServiceError("Test msg")
        self.assertEqual(exc_notificationserviceerror.error_code, "NotificationServiceError")
        self.assertEqual(exc_notificationserviceerror.message, "Test msg")

        exc_audioalerttriggererror = AudioAlertTriggerError("Test msg")
        self.assertEqual(exc_audioalerttriggererror.error_code, "AudioAlertTriggerError")
        self.assertEqual(exc_audioalerttriggererror.message, "Test msg")

        exc_videoframeemptyerror = VideoFrameEmptyError("Test msg")
        self.assertEqual(exc_videoframeemptyerror.error_code, "VideoFrameEmptyError")
        self.assertEqual(exc_videoframeemptyerror.message, "Test msg")

        exc_resolutionswitcherror = ResolutionSwitchError("Test msg")
        self.assertEqual(exc_resolutionswitcherror.error_code, "ResolutionSwitchError")
        self.assertEqual(exc_resolutionswitcherror.message, "Test msg")

        exc_camerareinitializationerror = CameraReinitializationError("Test msg")
        self.assertEqual(exc_camerareinitializationerror.error_code, "CameraReinitializationError")
        self.assertEqual(exc_camerareinitializationerror.message, "Test msg")

        exc_menuoptionindexerror = MenuOptionIndexError("Test msg")
        self.assertEqual(exc_menuoptionindexerror.error_code, "MenuOptionIndexError")
        self.assertEqual(exc_menuoptionindexerror.message, "Test msg")

        exc_widgetalignmenterror = WidgetAlignmentError("Test msg")
        self.assertEqual(exc_widgetalignmenterror.error_code, "WidgetAlignmentError")
        self.assertEqual(exc_widgetalignmenterror.message, "Test msg")

        exc_guithemekeyerror = GUIThemeKeyError("Test msg")
        self.assertEqual(exc_guithemekeyerror.error_code, "GUIThemeKeyError")
        self.assertEqual(exc_guithemekeyerror.message, "Test msg")

        exc_csvformatmismatcherror = CSVFormatMismatchError("Test msg")
        self.assertEqual(exc_csvformatmismatcherror.error_code, "CSVFormatMismatchError")
        self.assertEqual(exc_csvformatmismatcherror.message, "Test msg")

        exc_loggerconfigreseterror = LoggerConfigResetError("Test msg")
        self.assertEqual(exc_loggerconfigreseterror.error_code, "LoggerConfigResetError")
        self.assertEqual(exc_loggerconfigreseterror.message, "Test msg")

        exc_soundnotificationerror = SoundNotificationError("Test msg")
        self.assertEqual(exc_soundnotificationerror.error_code, "SoundNotificationError")
        self.assertEqual(exc_soundnotificationerror.message, "Test msg")

        exc_baselinenotestablishederror = BaselineNotEstablishedError("Test msg")
        self.assertEqual(exc_baselinenotestablishederror.error_code, "BaselineNotEstablishedError")
        self.assertEqual(exc_baselinenotestablishederror.message, "Test msg")

        exc_frameprocessingerror = FrameProcessingError("Test msg")
        self.assertEqual(exc_frameprocessingerror.error_code, "FrameProcessingError")
        self.assertEqual(exc_frameprocessingerror.message, "Test msg")

        exc_camerastreamthreaderror = CameraStreamThreadError("Test msg")
        self.assertEqual(exc_camerastreamthreaderror.error_code, "CameraStreamThreadError")
        self.assertEqual(exc_camerastreamthreaderror.message, "Test msg")

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

    def test_configfilelockerror(self) -> None:
        from exceptions import ConfigFileLockError
        exc = ConfigFileLockError("Test msg")
        self.assertEqual(exc.error_code, "ConfigFileLockError")
        self.assertEqual(exc.message, "Test msg")

    def test_loggerinitializationerror(self) -> None:
        from exceptions import LoggerInitializationError
        exc = LoggerInitializationError("Test msg")
        self.assertEqual(exc.error_code, "LoggerInitializationError")
        self.assertEqual(exc.message, "Test msg")

    def test_logfileopenerror(self) -> None:
        from exceptions import LogFileOpenError
        exc = LogFileOpenError("Test msg")
        self.assertEqual(exc.error_code, "LogFileOpenError")
        self.assertEqual(exc.message, "Test msg")

if __name__ == "__main__":
    unittest.main()
