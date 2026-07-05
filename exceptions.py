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

class ConfigurationSaveError(PostureGuardException):
    """Exception raised when configuration file writing fails due to permission or OS errors."""
    pass
