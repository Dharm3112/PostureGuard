class PostureGuardException(Exception):
    """
    Base exception class for PostureGuard errors.
    All custom exceptions in PostureGuard inherit from this base class.
    """
    def __init__(self, message: str = "An error occurred within PostureGuard.") -> None:
        self.message = message
        super().__init__(self.message)

    @property
    def error_code(self) -> str:
        return self.__class__.__name__


class CameraNotFoundError(PostureGuardException):
    """Exception raised when the configured webcam cannot be initialized or accessed."""
    def __init__(self, camera_index: int, message: str = "Webcam camera feed could not be opened.") -> None:
        self.camera_index = camera_index
        self.message = f"Error: camera index {camera_index} is unavailable. {message}"
        super().__init__(self.message)


class ModelLoadError(PostureGuardException):
    """Exception raised when the OpenCV Haar Cascade face classifier xml cannot be loaded."""
    def __init__(self, model_name: str = "haarcascade_frontalface_default.xml", message: str = "Classifier model failed to load.") -> None:
        self.model_name = model_name
        self.message = f"Error: Haar cascade model '{model_name}' could not be loaded. {message}"
        super().__init__(self.message)


class CalibrationError(PostureGuardException):
    """Exception raised when a calibration request is invalid or baseline cannot be established."""
    pass

class LoggingConfigurationError(PostureGuardException):
    """Exception raised when logging parameters are misconfigured or file write fails."""
    pass

class InvalidResolutionError(PostureGuardException):
    """Exception raised when camera resolution is not supported or out of bounds."""
    pass

class InvalidThresholdError(PostureGuardException):
    """Exception raised when slouch threshold value is out of bounds."""
    pass

class InvalidDelayError(PostureGuardException):
    """Exception raised when frame delay is negative or too large."""
    pass

class InvalidAlertFramesError(PostureGuardException):
    """Exception raised when alert frames limit value is invalid."""
    pass

class InvalidLogBytesError(PostureGuardException):
    """Exception raised when log max bytes is out of bounds."""
    pass

class InvalidBackupCountError(PostureGuardException):
    """Exception raised when log backup count value is out of bounds."""
    pass

class InvalidConfigFormatError(PostureGuardException):
    """Exception raised when config file format is invalid (not a dict)."""
    pass

class ConfigFileNotFoundError(PostureGuardException):
    """Exception raised when local config file is missing and default is not found."""
    pass

class ConfigWritePermissionError(PostureGuardException):
    """Exception raised when writing config file fails due to permission error."""
    pass

class StatsFileWriteError(PostureGuardException):
    """Exception raised when writing stats file fails due to permission or OS errors."""
    pass

class StatsFileReadError(PostureGuardException):
    """Exception raised when stats file reading fails due to OS errors."""
    pass

class HistoryFileNotFoundError(PostureGuardException):
    """Exception raised when posture history CSV file is not found."""
    pass

class GUIWindowInitializationError(PostureGuardException):
    """Exception raised when main Tkinter root window fails to load."""
    pass

class WidgetBindingError(PostureGuardException):
    """Exception raised when layout event bindings initialization fails."""
    pass

class ThemeLoadingError(PostureGuardException):
    """Exception raised when visual custom theme properties lookup fails."""
    pass

class TooltipConfigurationError(PostureGuardException):
    """Exception raised when hover dynamic helpers tooltip binding fails."""
    pass

class SettingsDialogError(PostureGuardException):
    """Exception raised when configuration dialog modal initialization fails."""
    pass

class StatisticsWindowError(PostureGuardException):
    """Exception raised when statistics modal window setup fails."""
    pass

class CameraStreamThreadError(PostureGuardException):
    """Exception raised when background frame capture daemon thread setup fails."""
    pass

class FrameProcessingError(PostureGuardException):
    """Exception raised when OpenCV frame annotation or parsing operations fail."""
    pass

class BaselineNotEstablishedError(PostureGuardException):
    """Exception raised when calibration status lookup fails on active checks."""
    pass

class SoundNotificationError(PostureGuardException):
    """Exception raised when plyer desktop status notification calls fail."""
    pass

class LoggerConfigResetError(PostureGuardException):
    """Exception raised when logging handlers cleanup operations fail."""
    pass

class CSVFormatMismatchError(PostureGuardException):
    """Exception raised when statistics log rows contains invalid headers."""
    pass

class GUIThemeKeyError(PostureGuardException):
    """Exception raised when theme dictionary does not contain requested visual keys."""
    pass

class WidgetAlignmentError(PostureGuardException):
    """Exception raised when main control layout elements alignment fails."""
    pass

class MenuOptionIndexError(PostureGuardException):
    """Exception raised when option dropdown menus indexes selections are out of range."""
    pass

class CameraReinitializationError(PostureGuardException):
    """Exception raised when re-instantiating camera feed device fails."""
    pass

class ResolutionSwitchError(PostureGuardException):
    """Exception raised when setting new width/height properties fails."""
    pass

class VideoFrameEmptyError(PostureGuardException):
    """Exception raised when stream returns empty frame array bytes."""
    pass

class AudioAlertTriggerError(PostureGuardException):
    """Exception raised when play sound warning checks trigger fails."""
    pass

class NotificationServiceError(PostureGuardException):
    """Exception raised when plyer desktop warnings background task fail."""
    pass

class CSVFieldFormatError(PostureGuardException):
    """Exception raised when csv parsing checks fails due to row fields data mismatch."""
    pass

class CSVWriterAccessError(PostureGuardException):
    """Exception raised when appending records to history files fails due to permission errors."""
    pass

class JSONBackupWriteError(PostureGuardException):
    """Exception raised when writing backup template parameters fails."""
    pass

class JSONRestoreFallbackError(PostureGuardException):
    """Exception raised when loading default configuration values fallback fails."""
    pass

class CanvasWidgetRenderError(PostureGuardException):
    """Exception raised when drawing OpenCV frame bytes on Tkinter canvas widget fails."""
    pass

class DynamicTooltipTimeoutError(PostureGuardException):
    """Exception raised when rendering dynamic tooltip status indicators timed out."""
    pass

class SettingsWindowDismissalError(PostureGuardException):
    """Exception raised when disposing settings popup modal windows fails."""
    pass

class DatabaseStatsRowFormatError(PostureGuardException):
    """Exception raised when statistics details parsing gets corrupt logs rows data."""
    pass

class LogRotationIntervalError(PostureGuardException):
    """Exception raised when logging directory rolls files encounters bounds limits errors."""
    pass

class SoundPlayerNotAvailableError(PostureGuardException):
    """Exception raised when default audio alarm triggers cannot find speaker hardware devices."""
    pass

class CalibrationBaselineMismatchError(PostureGuardException):
    """Exception raised when target coordinate indices values mismatch custom thresholds ranges."""
    pass

class CascadeModelFileFormatError(PostureGuardException):
    """Exception raised when loaded cascade model classifier XML structure gets parser errors."""
    pass

class JSONSchemaValidationError(PostureGuardException):
    """Exception raised when configuration JSON document does not match expected schema schemas."""
    pass

class ConfigurationWriteConflictError(PostureGuardException):
    """Exception raised when saving parameters configs file locks matches concurrent edits."""
    pass

class SystemNotificationPermissionError(PostureGuardException):
    """Exception raised when requesting desktop warning popup triggers gets permissions denied."""
    pass

class CameraResourceReleaseError(PostureGuardException):
    """Exception raised when closing capture video stream interfaces fails to release webcam hardware resources."""
    pass

class ConfigurationSaveError(PostureGuardException):
    """Exception raised when configuration file writing fails due to permission or OS errors."""
    pass


class ConfigFileLockError(PostureGuardException):
    """Exception raised when configuration file is locked by another process."""
    pass


class LoggerInitializationError(PostureGuardException):
    """Exception raised when logger initialization encounters critical filesystem errors."""
    pass


class LogFileOpenError(PostureGuardException):
    """Exception raised when logging directory exists but log file cannot be opened for writing."""
    pass


class LogRotationLockError(PostureGuardException):
    """Exception raised when rotating log files encounters a system lock."""
    pass


class LogFormattingError(PostureGuardException):
    """Exception raised when log formatter template parameters fail to compile."""
    pass


class CSVHeaderMismatchError(PostureGuardException):
    """Exception raised when CSV stats file headers do not match expected schema."""
    pass


class CSVEncodingError(PostureGuardException):
    """Exception raised when CSV file encoding contains invalid characters."""
    pass


class CSVLineEndingError(PostureGuardException):
    """Exception raised when CSV file contains inconsistent or corrupt line endings."""
    pass


class CSVTempFileCreationError(PostureGuardException):
    """Exception raised when temporary CSV file for stats recovery cannot be created."""
    pass


class CSVBackupError(PostureGuardException):
    """Exception raised when creating backup copies of history CSV logs fails."""
    pass


class UIElementNotFoundError(PostureGuardException):
    """Exception raised when Tkinter UI elements lookup by name or reference fails."""
    pass


class FontLoadingError(PostureGuardException):
    """Exception raised when custom system fonts fail to load or compile."""
    pass


class ImageAssetLoadingError(PostureGuardException):
    """Exception raised when visual graphic asset files cannot be loaded."""
    pass


class IconAssetFormatError(PostureGuardException):
    """Exception raised when visual window icon file format is corrupted."""
    pass


class WindowStateRestoreError(PostureGuardException):
    """Exception raised when restoring window coordinates or minimized status fails."""
    pass


class ThreadStartTimeoutError(PostureGuardException):
    """Exception raised when background frame stream daemon thread fails to start in time."""
    pass


class ThreadTerminationError(PostureGuardException):
    """Exception raised when camera capture background thread cannot be joined."""
    pass


class CameraCaptureDeviceBusyError(PostureGuardException):
    """Exception raised when camera device is already opened or locked by another app."""
    pass


class CameraAccessBlockedError(PostureGuardException):
    """Exception raised when OS security policies deny access to the camera hardware."""
    pass


class FrameBufferOverflowError(PostureGuardException):
    """Exception raised when queue buffer size of camera stream frames exceeds limits."""
    pass


class FaceCascadeXMLCorruptError(PostureGuardException):
    """Exception raised when loaded cascade model classifier XML structure is corrupt."""
    pass


class ModelDetectionTimeoutError(PostureGuardException):
    """Exception raised when face classifier detection model takes too long to run."""
    pass


class SmoothBufferEmptyError(PostureGuardException):
    """Exception raised when moving average posture coordinate buffer has no elements."""
    pass


class CalibrateFaceNotFoundError(PostureGuardException):
    """Exception raised when calibration baseline cannot locate face features in buffer."""
    pass


class CalibrateBaselineZeroError(PostureGuardException):
    """Exception raised when calibration baseline Y is zero or negative."""
    pass


class ConfigSchemaMismatchError(PostureGuardException):
    """Exception raised when configuration JSON structure violates validation schemas."""
    pass


class ConfigKeyNotFoundError(PostureGuardException):
    """Exception raised when a required parameter key is missing from configuration dictionary."""
    pass


class LogDirectoryCreationError(PostureGuardException):
    """Exception raised when local logging directory cannot be created."""
    pass


class LogFileWritePermissionError(PostureGuardException):
    """Exception raised when log files cannot be modified due to insufficient OS privileges."""
    pass


class CSVCellFormatError(PostureGuardException):
    """Exception raised when posture logs cell parsing gets corrupt fields data."""
    pass


class CSVRowOverflowError(PostureGuardException):
    """Exception raised when row size of history CSV logs exceeds system limits."""
    pass


class CSVCloseFileError(PostureGuardException):
    """Exception raised when CSV stats file stream cannot be closed cleanly."""
    pass


class CSVTempFileRenameError(PostureGuardException):
    """Exception raised when temporary CSV file for stats recovery cannot be renamed."""
    pass


class UIWidgetGeometryError(PostureGuardException):
    """Exception raised when setting width or height geometry coordinates fails."""
    pass


class ThemeKeyNotFoundError(PostureGuardException):
    """Exception raised when visual custom theme dictionary lookup misses requested keys."""
    pass


class HoverHighlightBindingError(PostureGuardException):
    """Exception raised when hover highlights mouse bindings fail to initialize."""
    pass


class TooltipRenderError(PostureGuardException):
    """Exception raised when drawing dynamic tooltip status label bubbles fails."""
    pass


class SettingsModalDismissError(PostureGuardException):
    """Exception raised when setting window modal cannot be disposed cleanly."""
    pass


class StatisticsParseError(PostureGuardException):
    """Exception raised when parsing posture history stats calculations fails."""
    pass


class ThreadPriorityAdjustmentError(PostureGuardException):
    """Exception raised when configuring thread runtime priority levels encounters OS errors."""
    pass


class CameraFrameCaptureError(PostureGuardException):
    """Exception raised when reading image frame arrays from webcam feed fails."""
    pass


class CameraFPSRateError(PostureGuardException):
    """Exception raised when camera capture stream frames per second setup is invalid."""
    pass


class FrameQueueLockError(PostureGuardException):
    """Exception raised when frame buffer thread queues acquire lock timeouts."""
    pass


class FaceDetectionCoordinatesError(PostureGuardException):
    """Exception raised when processed bounding box coordinates return NaN or invalid bounds."""
    pass


class CalibrateBufferOverflowError(PostureGuardException):
    """Exception raised when face calibration moving average buffer size gets memory bounds errors."""
    pass


class ConfigPathResolutionError(PostureGuardException):
    """Exception raised when absolute path lookup for configuration file fails."""
    pass


class ConfigDirectoryAccessError(PostureGuardException):
    """Exception raised when configuration folder is inaccessible due to OS permissions."""
    pass


class ConfigEncodingMismatchError(PostureGuardException):
    """Exception raised when config file encoding does not match standard UTF-8."""
    pass


class ConfigBackupDeletionError(PostureGuardException):
    """Exception raised when removing deprecated configuration backup files fails."""
    pass


class ConfigLockTimeoutError(PostureGuardException):
    """Exception raised when waiting to acquire configuration file lock times out."""
    pass


class LogFileWriteLockError(PostureGuardException):
    """Exception raised when log files cannot be written due to thread concurrency issues."""
    pass


class LogHandlerCleanupError(PostureGuardException):
    """Exception raised when closing log file descriptors encounters system errors."""
    pass


class LogSymlinkCreationError(PostureGuardException):
    """Exception raised when creating symbolic links to active log files fails."""
    pass


class CSVHeaderValidationError(PostureGuardException):
    """Exception raised when parsed CSV files does not match standard column headers."""
    pass


class CSVStreamClosedError(PostureGuardException):
    """Exception raised when appending rows to CSV files on a closed stream."""
    pass


class CSVFileLockError(PostureGuardException):
    """Exception raised when writing history records encounters file system locks."""
    pass


class UIFontRegistryError(PostureGuardException):
    """Exception raised when registering custom Segoe UI fonts with Tkinter core fails."""
    pass


class UIImageScaleError(PostureGuardException):
    """Exception raised when scaling icon or preview image assets fails."""
    pass


class UIWidgetZOrderError(PostureGuardException):
    """Exception raised when adjusting widget stacking order or window focus fails."""
    pass


class UIMenuPopulationError(PostureGuardException):
    """Exception raised when populating settings dropdown options menu fails."""
    pass


class UIThemeInvalidColorError(PostureGuardException):
    """Exception raised when visual custom theme colors contain invalid hex formats."""
    pass


class StatsCalculationDivisionByZeroError(PostureGuardException):
    """Exception raised when posture calculation values are divided by zero."""
    pass


class StatsCSVDataCorruptionError(PostureGuardException):
    """Exception raised when statistics parser detects corrupted float coordinates."""
    pass


class CameraResolutionHardwareMismatchError(PostureGuardException):
    """Exception raised when configured width or height is unsupported by hardware."""
    pass


class CameraBufferEmptyError(PostureGuardException):
    """Exception raised when camera capture stream returns empty frame queues."""
    pass


class CameraDeviceDisconnectionError(PostureGuardException):
    """Exception raised when active webcam capture stream disconnects unexpectedly."""
    pass


class ModelWeightFileLoadError(PostureGuardException):
    """Exception raised when face classifier model weights file has invalid read access."""
    pass


class FaceCascadeMultiDetectionError(PostureGuardException):
    """Exception raised when face detector gets overwhelmed with too many face coordinates."""
    pass


class CalibrateBaselineOutOfBoundsError(PostureGuardException):
    """Exception raised when calibrated baseline coordinates fall out of image canvas bounds."""
    pass


class AudioPlaybackDeviceNotFoundError(PostureGuardException):
    """Exception raised when alert plays warnings but no sound output device is connected."""
    pass


class AudioVolumeOutOfBoundsError(PostureGuardException):
    """Exception raised when system alert volume configuration is out of range."""
    pass


class AudioAlertDurationError(PostureGuardException):
    """Exception raised when audio play alert duration parameters are invalid."""
    pass


class NotificationIconNotFoundError(PostureGuardException):
    """Exception raised when system warning notification icon asset path is missing."""
    pass


class NotificationPayloadFormatError(PostureGuardException):
    """Exception raised when plyer desktop notification body contains malformed details."""
    pass


class ConfigAutoSaveError(PostureGuardException):
    """Exception raised when auto-saving configuration parameters to disk fails."""
    pass


class ConfigEncryptionError(PostureGuardException):
    """Exception raised when encrypting configuration file parameters fails."""
    pass


class LogHandlerFlushError(PostureGuardException):
    """Exception raised when flushing active logger handler streams fails."""
    pass


class LogConsoleColorError(PostureGuardException):
    """Exception raised when setting colorized output formatting on console stdout fails."""
    pass


class CSVLineReadError(PostureGuardException):
    """Exception raised when statistics reader gets file read error at specific line."""
    pass


class CSVFieldMismatchError(PostureGuardException):
    """Exception raised when CSV logs parser detects row fields count mismatch."""
    pass


class UIWidgetGeometryBoundsError(PostureGuardException):
    """Exception raised when desktop app window dimensions exceed screen bounds."""
    pass


class UIThemeInvalidPaletteError(PostureGuardException):
    """Exception raised when visual custom theme colors contain invalid hex formats."""
    pass


class UIHoverTimeoutError(PostureGuardException):
    """Exception raised when hover highlights tooltip elements fail to draw in time."""
    pass


class CameraFPSOutofRangeError(PostureGuardException):
    """Exception raised when webcam capture stream target FPS bounds are invalid."""
    pass


class CameraWarmupTimeoutError(PostureGuardException):
    """Exception raised when webcam initialization stream warmup takes too long."""
    pass


class ModelConfigFormatError(PostureGuardException):
    """Exception raised when loaded Haar cascade configuration structure has invalid keys."""
    pass


class FaceDetectionSmoothingError(PostureGuardException):
    """Exception raised when posture detector smoothing queue gets infinite coordinate values."""
    pass


class CalibratebaselineInvalidYError(PostureGuardException):
    """Exception raised when calibrated posture baseline Y falls on screen margins."""
    pass


class StatsGraphGenerationError(PostureGuardException):
    """Exception raised when statistics plotter engine fails to draw graphs."""
    pass


class StatsDataCorruptError(PostureGuardException):
    """Exception raised when posture records logs have invalid timestamps."""
    pass


class AudioDeviceMutedError(PostureGuardException):
    """Exception raised when playing posture alerts warning but audio output device is muted."""
    pass


class AudioFormatUnsupportedError(PostureGuardException):
    """Exception raised when warning sound file format is unsupported by audio playback library."""
    pass


class NotificationChannelCreationError(PostureGuardException):
    """Exception raised when creating desktop notification notification channel channel fails."""
    pass


class NotificationActionCallbackError(PostureGuardException):
    """Exception raised when user interaction action callback on system notification fails."""
    pass


class ConfigKeyValidationError(PostureGuardException):
    """Exception raised when setting configuration parameter checks violates runtime validation bounds."""
    pass


class ConfigReadOnlyError(PostureGuardException):
    """Exception raised when updating read-only configuration parameter settings."""
    pass


class LogHandlerRegistrationError(PostureGuardException):
    """Exception raised when registering custom handler to active logger stream fails."""
    pass


class LogRotationFileCreationError(PostureGuardException):
    """Exception raised when generating next log rotation backup file fails."""
    pass


class CSVHeaderLengthMismatchError(PostureGuardException):
    """Exception raised when stats CSV row fields length mismatches headers length."""
    pass


class CSVDataTypesMismatchError(PostureGuardException):
    """Exception raised when CSV parser gets string types instead of integer deviation pixels."""
    pass


class UIWidgetGeometryCoordinatesError(PostureGuardException):
    """Exception raised when setting dashboard widgets X or Y grid coordinates fails."""
    pass


class UIThemeInvalidFontColorError(PostureGuardException):
    """Exception raised when visual custom theme active foreground colors are invalid."""
    pass


class UIHoverTooltipPlacementError(PostureGuardException):
    """Exception raised when hover highlights tooltip labels bounds are out of window boundaries."""
    pass


class CameraFPSInvalidBoundsError(PostureGuardException):
    """Exception raised when webcam capture stream rate limits bounds are out of hardware range."""
    pass


class CameraReinitializationTimeoutError(PostureGuardException):
    """Exception raised when re-instantiating camera device takes too long to warm up."""
    pass


class ModelCascadeCorruptError(PostureGuardException):
    """Exception raised when loaded cascade model classifier XML structure gets corrupt values."""
    pass


class FaceDetectionSmoothingEmptyError(PostureGuardException):
    """Exception raised when posture detector smoothing queue returns zero center Y coordinates."""
    pass


class CalibrateBaselineOutOfBoundsError(PostureGuardException):
    """Exception raised when calibrated posture baseline center Y is out of canvas bounds."""
    pass


class StatsGraphPlotterFormatError(PostureGuardException):
    """Exception raised when stats graph plotter engine gets invalid coordinates formats."""
    pass


class StatsDataTimestampFormatError(PostureGuardException):
    """Exception raised when posture records logs have invalid datetime strings format."""
    pass


class DatabaseConnectionTimeoutError(PostureGuardException):
    """Exception raised when opening connection to database for stats persistence times out."""
    pass


class DatabaseQueryExecutionError(PostureGuardException):
    """Exception raised when executing database query for statistics history fails."""
    pass
