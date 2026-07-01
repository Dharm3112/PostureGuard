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

class ConfigurationSaveError(PostureGuardException):
    """Exception raised when configuration file writing fails due to permission or OS errors."""
    pass
