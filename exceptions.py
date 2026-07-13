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
