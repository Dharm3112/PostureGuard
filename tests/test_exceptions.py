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

    def test_logrotationlockerror(self) -> None:
        from exceptions import LogRotationLockError
        exc = LogRotationLockError("Test msg")
        self.assertEqual(exc.error_code, "LogRotationLockError")
        self.assertEqual(exc.message, "Test msg")

    def test_logformattingerror(self) -> None:
        from exceptions import LogFormattingError
        exc = LogFormattingError("Test msg")
        self.assertEqual(exc.error_code, "LogFormattingError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvheadermismatcherror(self) -> None:
        from exceptions import CSVHeaderMismatchError
        exc = CSVHeaderMismatchError("Test msg")
        self.assertEqual(exc.error_code, "CSVHeaderMismatchError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvencodingerror(self) -> None:
        from exceptions import CSVEncodingError
        exc = CSVEncodingError("Test msg")
        self.assertEqual(exc.error_code, "CSVEncodingError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvlineendingerror(self) -> None:
        from exceptions import CSVLineEndingError
        exc = CSVLineEndingError("Test msg")
        self.assertEqual(exc.error_code, "CSVLineEndingError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvtempfilecreationerror(self) -> None:
        from exceptions import CSVTempFileCreationError
        exc = CSVTempFileCreationError("Test msg")
        self.assertEqual(exc.error_code, "CSVTempFileCreationError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvbackuperror(self) -> None:
        from exceptions import CSVBackupError
        exc = CSVBackupError("Test msg")
        self.assertEqual(exc.error_code, "CSVBackupError")
        self.assertEqual(exc.message, "Test msg")

    def test_uielementnotfounderror(self) -> None:
        from exceptions import UIElementNotFoundError
        exc = UIElementNotFoundError("Test msg")
        self.assertEqual(exc.error_code, "UIElementNotFoundError")
        self.assertEqual(exc.message, "Test msg")

    def test_fontloadingerror(self) -> None:
        from exceptions import FontLoadingError
        exc = FontLoadingError("Test msg")
        self.assertEqual(exc.error_code, "FontLoadingError")
        self.assertEqual(exc.message, "Test msg")

    def test_imageassetloadingerror(self) -> None:
        from exceptions import ImageAssetLoadingError
        exc = ImageAssetLoadingError("Test msg")
        self.assertEqual(exc.error_code, "ImageAssetLoadingError")
        self.assertEqual(exc.message, "Test msg")

    def test_iconassetformaterror(self) -> None:
        from exceptions import IconAssetFormatError
        exc = IconAssetFormatError("Test msg")
        self.assertEqual(exc.error_code, "IconAssetFormatError")
        self.assertEqual(exc.message, "Test msg")

    def test_windowstaterestoreerror(self) -> None:
        from exceptions import WindowStateRestoreError
        exc = WindowStateRestoreError("Test msg")
        self.assertEqual(exc.error_code, "WindowStateRestoreError")
        self.assertEqual(exc.message, "Test msg")

    def test_threadstarttimeouterror(self) -> None:
        from exceptions import ThreadStartTimeoutError
        exc = ThreadStartTimeoutError("Test msg")
        self.assertEqual(exc.error_code, "ThreadStartTimeoutError")
        self.assertEqual(exc.message, "Test msg")

    def test_threadterminationerror(self) -> None:
        from exceptions import ThreadTerminationError
        exc = ThreadTerminationError("Test msg")
        self.assertEqual(exc.error_code, "ThreadTerminationError")
        self.assertEqual(exc.message, "Test msg")

    def test_cameracapturedevicebusyerror(self) -> None:
        from exceptions import CameraCaptureDeviceBusyError
        exc = CameraCaptureDeviceBusyError("Test msg")
        self.assertEqual(exc.error_code, "CameraCaptureDeviceBusyError")
        self.assertEqual(exc.message, "Test msg")

    def test_cameraaccessblockederror(self) -> None:
        from exceptions import CameraAccessBlockedError
        exc = CameraAccessBlockedError("Test msg")
        self.assertEqual(exc.error_code, "CameraAccessBlockedError")
        self.assertEqual(exc.message, "Test msg")

    def test_framebufferoverflowerror(self) -> None:
        from exceptions import FrameBufferOverflowError
        exc = FrameBufferOverflowError("Test msg")
        self.assertEqual(exc.error_code, "FrameBufferOverflowError")
        self.assertEqual(exc.message, "Test msg")

    def test_facecascadexmlcorrupterror(self) -> None:
        from exceptions import FaceCascadeXMLCorruptError
        exc = FaceCascadeXMLCorruptError("Test msg")
        self.assertEqual(exc.error_code, "FaceCascadeXMLCorruptError")
        self.assertEqual(exc.message, "Test msg")

    def test_modeldetectiontimeouterror(self) -> None:
        from exceptions import ModelDetectionTimeoutError
        exc = ModelDetectionTimeoutError("Test msg")
        self.assertEqual(exc.error_code, "ModelDetectionTimeoutError")
        self.assertEqual(exc.message, "Test msg")

    def test_smoothbufferemptyerror(self) -> None:
        from exceptions import SmoothBufferEmptyError
        exc = SmoothBufferEmptyError("Test msg")
        self.assertEqual(exc.error_code, "SmoothBufferEmptyError")
        self.assertEqual(exc.message, "Test msg")

    def test_calibratefacenotfounderror(self) -> None:
        from exceptions import CalibrateFaceNotFoundError
        exc = CalibrateFaceNotFoundError("Test msg")
        self.assertEqual(exc.error_code, "CalibrateFaceNotFoundError")
        self.assertEqual(exc.message, "Test msg")

    def test_calibratebaselinezeroerror(self) -> None:
        from exceptions import CalibrateBaselineZeroError
        exc = CalibrateBaselineZeroError("Test msg")
        self.assertEqual(exc.error_code, "CalibrateBaselineZeroError")
        self.assertEqual(exc.message, "Test msg")

    def test_configschemamismatcherror(self) -> None:
        from exceptions import ConfigSchemaMismatchError
        exc = ConfigSchemaMismatchError("Test msg")
        self.assertEqual(exc.error_code, "ConfigSchemaMismatchError")
        self.assertEqual(exc.message, "Test msg")

    def test_configkeynotfounderror(self) -> None:
        from exceptions import ConfigKeyNotFoundError
        exc = ConfigKeyNotFoundError("Test msg")
        self.assertEqual(exc.error_code, "ConfigKeyNotFoundError")
        self.assertEqual(exc.message, "Test msg")

    def test_logdirectorycreationerror(self) -> None:
        from exceptions import LogDirectoryCreationError
        exc = LogDirectoryCreationError("Test msg")
        self.assertEqual(exc.error_code, "LogDirectoryCreationError")
        self.assertEqual(exc.message, "Test msg")

    def test_logfilewritepermissionerror(self) -> None:
        from exceptions import LogFileWritePermissionError
        exc = LogFileWritePermissionError("Test msg")
        self.assertEqual(exc.error_code, "LogFileWritePermissionError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvcellformaterror(self) -> None:
        from exceptions import CSVCellFormatError
        exc = CSVCellFormatError("Test msg")
        self.assertEqual(exc.error_code, "CSVCellFormatError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvrowoverflowerror(self) -> None:
        from exceptions import CSVRowOverflowError
        exc = CSVRowOverflowError("Test msg")
        self.assertEqual(exc.error_code, "CSVRowOverflowError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvclosefileerror(self) -> None:
        from exceptions import CSVCloseFileError
        exc = CSVCloseFileError("Test msg")
        self.assertEqual(exc.error_code, "CSVCloseFileError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvtempfilerenameerror(self) -> None:
        from exceptions import CSVTempFileRenameError
        exc = CSVTempFileRenameError("Test msg")
        self.assertEqual(exc.error_code, "CSVTempFileRenameError")
        self.assertEqual(exc.message, "Test msg")

    def test_uiwidgetgeometryerror(self) -> None:
        from exceptions import UIWidgetGeometryError
        exc = UIWidgetGeometryError("Test msg")
        self.assertEqual(exc.error_code, "UIWidgetGeometryError")
        self.assertEqual(exc.message, "Test msg")

    def test_themekeynotfounderror(self) -> None:
        from exceptions import ThemeKeyNotFoundError
        exc = ThemeKeyNotFoundError("Test msg")
        self.assertEqual(exc.error_code, "ThemeKeyNotFoundError")
        self.assertEqual(exc.message, "Test msg")

    def test_hoverhighlightbindingerror(self) -> None:
        from exceptions import HoverHighlightBindingError
        exc = HoverHighlightBindingError("Test msg")
        self.assertEqual(exc.error_code, "HoverHighlightBindingError")
        self.assertEqual(exc.message, "Test msg")

    def test_tooltiprendererror(self) -> None:
        from exceptions import TooltipRenderError
        exc = TooltipRenderError("Test msg")
        self.assertEqual(exc.error_code, "TooltipRenderError")
        self.assertEqual(exc.message, "Test msg")

    def test_settingsmodaldismisserror(self) -> None:
        from exceptions import SettingsModalDismissError
        exc = SettingsModalDismissError("Test msg")
        self.assertEqual(exc.error_code, "SettingsModalDismissError")
        self.assertEqual(exc.message, "Test msg")

    def test_statisticsparseerror(self) -> None:
        from exceptions import StatisticsParseError
        exc = StatisticsParseError("Test msg")
        self.assertEqual(exc.error_code, "StatisticsParseError")
        self.assertEqual(exc.message, "Test msg")

    def test_threadpriorityadjustmenterror(self) -> None:
        from exceptions import ThreadPriorityAdjustmentError
        exc = ThreadPriorityAdjustmentError("Test msg")
        self.assertEqual(exc.error_code, "ThreadPriorityAdjustmentError")
        self.assertEqual(exc.message, "Test msg")

    def test_cameraframecaptureerror(self) -> None:
        from exceptions import CameraFrameCaptureError
        exc = CameraFrameCaptureError("Test msg")
        self.assertEqual(exc.error_code, "CameraFrameCaptureError")
        self.assertEqual(exc.message, "Test msg")

    def test_camerafpsrateerror(self) -> None:
        from exceptions import CameraFPSRateError
        exc = CameraFPSRateError("Test msg")
        self.assertEqual(exc.error_code, "CameraFPSRateError")
        self.assertEqual(exc.message, "Test msg")

    def test_framequeuelockerror(self) -> None:
        from exceptions import FrameQueueLockError
        exc = FrameQueueLockError("Test msg")
        self.assertEqual(exc.error_code, "FrameQueueLockError")
        self.assertEqual(exc.message, "Test msg")

    def test_facedetectioncoordinateserror(self) -> None:
        from exceptions import FaceDetectionCoordinatesError
        exc = FaceDetectionCoordinatesError("Test msg")
        self.assertEqual(exc.error_code, "FaceDetectionCoordinatesError")
        self.assertEqual(exc.message, "Test msg")

    def test_calibratebufferoverflowerror(self) -> None:
        from exceptions import CalibrateBufferOverflowError
        exc = CalibrateBufferOverflowError("Test msg")
        self.assertEqual(exc.error_code, "CalibrateBufferOverflowError")
        self.assertEqual(exc.message, "Test msg")

    def test_configpathresolutionerror(self) -> None:
        from exceptions import ConfigPathResolutionError
        exc = ConfigPathResolutionError("Test msg")
        self.assertEqual(exc.error_code, "ConfigPathResolutionError")
        self.assertEqual(exc.message, "Test msg")

    def test_configdirectoryaccesserror(self) -> None:
        from exceptions import ConfigDirectoryAccessError
        exc = ConfigDirectoryAccessError("Test msg")
        self.assertEqual(exc.error_code, "ConfigDirectoryAccessError")
        self.assertEqual(exc.message, "Test msg")

    def test_configencodingmismatcherror(self) -> None:
        from exceptions import ConfigEncodingMismatchError
        exc = ConfigEncodingMismatchError("Test msg")
        self.assertEqual(exc.error_code, "ConfigEncodingMismatchError")
        self.assertEqual(exc.message, "Test msg")

    def test_configbackupdeletionerror(self) -> None:
        from exceptions import ConfigBackupDeletionError
        exc = ConfigBackupDeletionError("Test msg")
        self.assertEqual(exc.error_code, "ConfigBackupDeletionError")
        self.assertEqual(exc.message, "Test msg")

    def test_configlocktimeouterror(self) -> None:
        from exceptions import ConfigLockTimeoutError
        exc = ConfigLockTimeoutError("Test msg")
        self.assertEqual(exc.error_code, "ConfigLockTimeoutError")
        self.assertEqual(exc.message, "Test msg")

    def test_logfilewritelockerror(self) -> None:
        from exceptions import LogFileWriteLockError
        exc = LogFileWriteLockError("Test msg")
        self.assertEqual(exc.error_code, "LogFileWriteLockError")
        self.assertEqual(exc.message, "Test msg")

    def test_loghandlercleanuperror(self) -> None:
        from exceptions import LogHandlerCleanupError
        exc = LogHandlerCleanupError("Test msg")
        self.assertEqual(exc.error_code, "LogHandlerCleanupError")
        self.assertEqual(exc.message, "Test msg")

    def test_logsymlinkcreationerror(self) -> None:
        from exceptions import LogSymlinkCreationError
        exc = LogSymlinkCreationError("Test msg")
        self.assertEqual(exc.error_code, "LogSymlinkCreationError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvheadervalidationerror(self) -> None:
        from exceptions import CSVHeaderValidationError
        exc = CSVHeaderValidationError("Test msg")
        self.assertEqual(exc.error_code, "CSVHeaderValidationError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvstreamclosederror(self) -> None:
        from exceptions import CSVStreamClosedError
        exc = CSVStreamClosedError("Test msg")
        self.assertEqual(exc.error_code, "CSVStreamClosedError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvfilelockerror(self) -> None:
        from exceptions import CSVFileLockError
        exc = CSVFileLockError("Test msg")
        self.assertEqual(exc.error_code, "CSVFileLockError")
        self.assertEqual(exc.message, "Test msg")

    def test_uifontregistryerror(self) -> None:
        from exceptions import UIFontRegistryError
        exc = UIFontRegistryError("Test msg")
        self.assertEqual(exc.error_code, "UIFontRegistryError")
        self.assertEqual(exc.message, "Test msg")

    def test_uiimagescaleerror(self) -> None:
        from exceptions import UIImageScaleError
        exc = UIImageScaleError("Test msg")
        self.assertEqual(exc.error_code, "UIImageScaleError")
        self.assertEqual(exc.message, "Test msg")

    def test_uiwidgetzordererror(self) -> None:
        from exceptions import UIWidgetZOrderError
        exc = UIWidgetZOrderError("Test msg")
        self.assertEqual(exc.error_code, "UIWidgetZOrderError")
        self.assertEqual(exc.message, "Test msg")

    def test_uimenupopulationerror(self) -> None:
        from exceptions import UIMenuPopulationError
        exc = UIMenuPopulationError("Test msg")
        self.assertEqual(exc.error_code, "UIMenuPopulationError")
        self.assertEqual(exc.message, "Test msg")

    def test_uithemeinvalidcolorerror(self) -> None:
        from exceptions import UIThemeInvalidColorError
        exc = UIThemeInvalidColorError("Test msg")
        self.assertEqual(exc.error_code, "UIThemeInvalidColorError")
        self.assertEqual(exc.message, "Test msg")

    def test_statscalculationdivisionbyzeroerror(self) -> None:
        from exceptions import StatsCalculationDivisionByZeroError
        exc = StatsCalculationDivisionByZeroError("Test msg")
        self.assertEqual(exc.error_code, "StatsCalculationDivisionByZeroError")
        self.assertEqual(exc.message, "Test msg")

    def test_statscsvdatacorruptionerror(self) -> None:
        from exceptions import StatsCSVDataCorruptionError
        exc = StatsCSVDataCorruptionError("Test msg")
        self.assertEqual(exc.error_code, "StatsCSVDataCorruptionError")
        self.assertEqual(exc.message, "Test msg")

    def test_cameraresolutionhardwaremismatcherror(self) -> None:
        from exceptions import CameraResolutionHardwareMismatchError
        exc = CameraResolutionHardwareMismatchError("Test msg")
        self.assertEqual(exc.error_code, "CameraResolutionHardwareMismatchError")
        self.assertEqual(exc.message, "Test msg")

    def test_camerabufferemptyerror(self) -> None:
        from exceptions import CameraBufferEmptyError
        exc = CameraBufferEmptyError("Test msg")
        self.assertEqual(exc.error_code, "CameraBufferEmptyError")
        self.assertEqual(exc.message, "Test msg")

    def test_cameradevicedisconnectionerror(self) -> None:
        from exceptions import CameraDeviceDisconnectionError
        exc = CameraDeviceDisconnectionError("Test msg")
        self.assertEqual(exc.error_code, "CameraDeviceDisconnectionError")
        self.assertEqual(exc.message, "Test msg")

    def test_modelweightfileloaderror(self) -> None:
        from exceptions import ModelWeightFileLoadError
        exc = ModelWeightFileLoadError("Test msg")
        self.assertEqual(exc.error_code, "ModelWeightFileLoadError")
        self.assertEqual(exc.message, "Test msg")

    def test_facecascademultidetectionerror(self) -> None:
        from exceptions import FaceCascadeMultiDetectionError
        exc = FaceCascadeMultiDetectionError("Test msg")
        self.assertEqual(exc.error_code, "FaceCascadeMultiDetectionError")
        self.assertEqual(exc.message, "Test msg")

    def test_calibratebaselineoutofboundserror(self) -> None:
        from exceptions import CalibrateBaselineOutOfBoundsError
        exc = CalibrateBaselineOutOfBoundsError("Test msg")
        self.assertEqual(exc.error_code, "CalibrateBaselineOutOfBoundsError")
        self.assertEqual(exc.message, "Test msg")

    def test_audioplaybackdevicenotfounderror(self) -> None:
        from exceptions import AudioPlaybackDeviceNotFoundError
        exc = AudioPlaybackDeviceNotFoundError("Test msg")
        self.assertEqual(exc.error_code, "AudioPlaybackDeviceNotFoundError")
        self.assertEqual(exc.message, "Test msg")

    def test_audiovolumeoutofboundserror(self) -> None:
        from exceptions import AudioVolumeOutOfBoundsError
        exc = AudioVolumeOutOfBoundsError("Test msg")
        self.assertEqual(exc.error_code, "AudioVolumeOutOfBoundsError")
        self.assertEqual(exc.message, "Test msg")

    def test_audioalertdurationerror(self) -> None:
        from exceptions import AudioAlertDurationError
        exc = AudioAlertDurationError("Test msg")
        self.assertEqual(exc.error_code, "AudioAlertDurationError")
        self.assertEqual(exc.message, "Test msg")

    def test_notificationiconnotfounderror(self) -> None:
        from exceptions import NotificationIconNotFoundError
        exc = NotificationIconNotFoundError("Test msg")
        self.assertEqual(exc.error_code, "NotificationIconNotFoundError")
        self.assertEqual(exc.message, "Test msg")

    def test_notificationpayloadformaterror(self) -> None:
        from exceptions import NotificationPayloadFormatError
        exc = NotificationPayloadFormatError("Test msg")
        self.assertEqual(exc.error_code, "NotificationPayloadFormatError")
        self.assertEqual(exc.message, "Test msg")

    def test_configautosaveerror(self) -> None:
        from exceptions import ConfigAutoSaveError
        exc = ConfigAutoSaveError("Test msg")
        self.assertEqual(exc.error_code, "ConfigAutoSaveError")
        self.assertEqual(exc.message, "Test msg")

    def test_configencryptionerror(self) -> None:
        from exceptions import ConfigEncryptionError
        exc = ConfigEncryptionError("Test msg")
        self.assertEqual(exc.error_code, "ConfigEncryptionError")
        self.assertEqual(exc.message, "Test msg")

    def test_loghandlerflusherror(self) -> None:
        from exceptions import LogHandlerFlushError
        exc = LogHandlerFlushError("Test msg")
        self.assertEqual(exc.error_code, "LogHandlerFlushError")
        self.assertEqual(exc.message, "Test msg")

    def test_logconsolecolorerror(self) -> None:
        from exceptions import LogConsoleColorError
        exc = LogConsoleColorError("Test msg")
        self.assertEqual(exc.error_code, "LogConsoleColorError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvlinereaderror(self) -> None:
        from exceptions import CSVLineReadError
        exc = CSVLineReadError("Test msg")
        self.assertEqual(exc.error_code, "CSVLineReadError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvfieldmismatcherror(self) -> None:
        from exceptions import CSVFieldMismatchError
        exc = CSVFieldMismatchError("Test msg")
        self.assertEqual(exc.error_code, "CSVFieldMismatchError")
        self.assertEqual(exc.message, "Test msg")

    def test_uiwidgetgeometryboundserror(self) -> None:
        from exceptions import UIWidgetGeometryBoundsError
        exc = UIWidgetGeometryBoundsError("Test msg")
        self.assertEqual(exc.error_code, "UIWidgetGeometryBoundsError")
        self.assertEqual(exc.message, "Test msg")

    def test_uithemeinvalidpaletteerror(self) -> None:
        from exceptions import UIThemeInvalidPaletteError
        exc = UIThemeInvalidPaletteError("Test msg")
        self.assertEqual(exc.error_code, "UIThemeInvalidPaletteError")
        self.assertEqual(exc.message, "Test msg")

    def test_uihovertimeouterror(self) -> None:
        from exceptions import UIHoverTimeoutError
        exc = UIHoverTimeoutError("Test msg")
        self.assertEqual(exc.error_code, "UIHoverTimeoutError")
        self.assertEqual(exc.message, "Test msg")

    def test_camerafpsoutofrangeerror(self) -> None:
        from exceptions import CameraFPSOutofRangeError
        exc = CameraFPSOutofRangeError("Test msg")
        self.assertEqual(exc.error_code, "CameraFPSOutofRangeError")
        self.assertEqual(exc.message, "Test msg")

    def test_camerawarmuptimeouterror(self) -> None:
        from exceptions import CameraWarmupTimeoutError
        exc = CameraWarmupTimeoutError("Test msg")
        self.assertEqual(exc.error_code, "CameraWarmupTimeoutError")
        self.assertEqual(exc.message, "Test msg")

    def test_modelconfigformaterror(self) -> None:
        from exceptions import ModelConfigFormatError
        exc = ModelConfigFormatError("Test msg")
        self.assertEqual(exc.error_code, "ModelConfigFormatError")
        self.assertEqual(exc.message, "Test msg")

    def test_facedetectionsmoothingerror(self) -> None:
        from exceptions import FaceDetectionSmoothingError
        exc = FaceDetectionSmoothingError("Test msg")
        self.assertEqual(exc.error_code, "FaceDetectionSmoothingError")
        self.assertEqual(exc.message, "Test msg")

    def test_calibratebaselineinvalidyerror(self) -> None:
        from exceptions import CalibratebaselineInvalidYError
        exc = CalibratebaselineInvalidYError("Test msg")
        self.assertEqual(exc.error_code, "CalibratebaselineInvalidYError")
        self.assertEqual(exc.message, "Test msg")

    def test_statsgraphgenerationerror(self) -> None:
        from exceptions import StatsGraphGenerationError
        exc = StatsGraphGenerationError("Test msg")
        self.assertEqual(exc.error_code, "StatsGraphGenerationError")
        self.assertEqual(exc.message, "Test msg")

    def test_statsdatacorrupterror(self) -> None:
        from exceptions import StatsDataCorruptError
        exc = StatsDataCorruptError("Test msg")
        self.assertEqual(exc.error_code, "StatsDataCorruptError")
        self.assertEqual(exc.message, "Test msg")

    def test_audiodevicemutederror(self) -> None:
        from exceptions import AudioDeviceMutedError
        exc = AudioDeviceMutedError("Test msg")
        self.assertEqual(exc.error_code, "AudioDeviceMutedError")
        self.assertEqual(exc.message, "Test msg")

    def test_audioformatunsupportederror(self) -> None:
        from exceptions import AudioFormatUnsupportedError
        exc = AudioFormatUnsupportedError("Test msg")
        self.assertEqual(exc.error_code, "AudioFormatUnsupportedError")
        self.assertEqual(exc.message, "Test msg")

    def test_notificationchannelcreationerror(self) -> None:
        from exceptions import NotificationChannelCreationError
        exc = NotificationChannelCreationError("Test msg")
        self.assertEqual(exc.error_code, "NotificationChannelCreationError")
        self.assertEqual(exc.message, "Test msg")

    def test_notificationactioncallbackerror(self) -> None:
        from exceptions import NotificationActionCallbackError
        exc = NotificationActionCallbackError("Test msg")
        self.assertEqual(exc.error_code, "NotificationActionCallbackError")
        self.assertEqual(exc.message, "Test msg")

    def test_configkeyvalidationerror(self) -> None:
        from exceptions import ConfigKeyValidationError
        exc = ConfigKeyValidationError("Test msg")
        self.assertEqual(exc.error_code, "ConfigKeyValidationError")
        self.assertEqual(exc.message, "Test msg")

    def test_configreadonlyerror(self) -> None:
        from exceptions import ConfigReadOnlyError
        exc = ConfigReadOnlyError("Test msg")
        self.assertEqual(exc.error_code, "ConfigReadOnlyError")
        self.assertEqual(exc.message, "Test msg")

    def test_loghandlerregistrationerror(self) -> None:
        from exceptions import LogHandlerRegistrationError
        exc = LogHandlerRegistrationError("Test msg")
        self.assertEqual(exc.error_code, "LogHandlerRegistrationError")
        self.assertEqual(exc.message, "Test msg")

    def test_logrotationfilecreationerror(self) -> None:
        from exceptions import LogRotationFileCreationError
        exc = LogRotationFileCreationError("Test msg")
        self.assertEqual(exc.error_code, "LogRotationFileCreationError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvheaderlengthmismatcherror(self) -> None:
        from exceptions import CSVHeaderLengthMismatchError
        exc = CSVHeaderLengthMismatchError("Test msg")
        self.assertEqual(exc.error_code, "CSVHeaderLengthMismatchError")
        self.assertEqual(exc.message, "Test msg")

    def test_csvdatatypesmismatcherror(self) -> None:
        from exceptions import CSVDataTypesMismatchError
        exc = CSVDataTypesMismatchError("Test msg")
        self.assertEqual(exc.error_code, "CSVDataTypesMismatchError")
        self.assertEqual(exc.message, "Test msg")

    def test_uiwidgetgeometrycoordinateserror(self) -> None:
        from exceptions import UIWidgetGeometryCoordinatesError
        exc = UIWidgetGeometryCoordinatesError("Test msg")
        self.assertEqual(exc.error_code, "UIWidgetGeometryCoordinatesError")
        self.assertEqual(exc.message, "Test msg")

    def test_uithemeinvalidfontcolorerror(self) -> None:
        from exceptions import UIThemeInvalidFontColorError
        exc = UIThemeInvalidFontColorError("Test msg")
        self.assertEqual(exc.error_code, "UIThemeInvalidFontColorError")
        self.assertEqual(exc.message, "Test msg")

    def test_uihovertooltipplacementerror(self) -> None:
        from exceptions import UIHoverTooltipPlacementError
        exc = UIHoverTooltipPlacementError("Test msg")
        self.assertEqual(exc.error_code, "UIHoverTooltipPlacementError")
        self.assertEqual(exc.message, "Test msg")

    def test_camerafpsinvalidboundserror(self) -> None:
        from exceptions import CameraFPSInvalidBoundsError
        exc = CameraFPSInvalidBoundsError("Test msg")
        self.assertEqual(exc.error_code, "CameraFPSInvalidBoundsError")
        self.assertEqual(exc.message, "Test msg")

if __name__ == "__main__":
    unittest.main()
