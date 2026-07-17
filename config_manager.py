import os
import json
import shutil
from typing import Any, Dict


class ConfigManager:
    """
    Manages local application configuration JSON files.
    Copies default settings, reads config parameters, and handles runtime updates.
    """
    DEFAULT_CONFIG_FILE = "config.json.default"  # Default configuration template filename
    LOCAL_CONFIG_FILE = "config.json"  # Active local configuration filename
    
    # Key Constants
    CAMERA_INDEX = "camera_index"
    SLOUCH_THRESHOLD = "slouch_threshold_px"
    TIME_TO_ALERT = "time_to_alert_frames"
    FRAME_DELAY = "frame_delay_ms"
    CAMERA_WIDTH = "camera_width"
    CAMERA_HEIGHT = "camera_height"
    SAVE_HISTORY = "save_history"
    SAVED_BASELINE_Y = "saved_baseline_y"
    
    SCALE_FACTOR = "scale_factor"
    MIN_NEIGHBORS = "min_neighbors"
    
    DEFAULT_SETTINGS = {  # Internal default settings database schema mapping dictionary
        "camera_index": 0,
        "slouch_threshold_px": 40,
        "time_to_alert_frames": 50,
        "frame_delay_ms": 15,
        "camera_width": 640,
        "camera_height": 480,
        "save_history": True,
        "saved_baseline_y": None,
        "scale_factor": 1.1,  # Default scale factor multiplier for Haar cascades
        "min_neighbors": 5,
        "log_max_bytes": 1048576,
        "log_backup_count": 3
    }

    def __init__(self, initial_config: Dict[str, Any] = None) -> None:
        """
        Initializes the ConfigManager, ensuring that a local config.json exists.
        Loads the config into an in-memory dictionary.
        """
        self.config_data: Dict[str, Any] = {}  # Initialize empty dictionary cache storage
        if initial_config is not None:  # Validate presence of initial configuration map inputs
            self.config_data = initial_config.copy()
        else:
            self._ensure_config_exists()  # Verify local config file path initialization state
            self.load()  # Load parameters settings dictionary from active JSON storage

    def _ensure_config_exists(self) -> None:
        """
        Helper method to copy config.json.default to config.json if the latter is missing.
        """
        if not os.path.exists(self.LOCAL_CONFIG_FILE):
            if os.path.exists(self.DEFAULT_CONFIG_FILE):
                shutil.copy(self.DEFAULT_CONFIG_FILE, self.LOCAL_CONFIG_FILE)
            else:
                # Fallback internal defaults if config.json.default is also missing
                self.config_data = self.DEFAULT_SETTINGS.copy()
                self._save_to_file()

    def load(self) -> None:
        """
        Loads configuration dictionary from the local file.
        """
        try:  # Attempt open stream to serialize settings back to JSON
            with open(self.LOCAL_CONFIG_FILE, "r") as f:
                self.config_data = json.load(f)
                if not isinstance(self.config_data, dict):
                    raise ValueError("Config format invalid, must be a dictionary")
        except (json.JSONDecodeError, OSError, ValueError):  # Fallback to default setup on parsing issues
            if os.path.exists(self.DEFAULT_CONFIG_FILE):
                try:
                    shutil.copy(self.DEFAULT_CONFIG_FILE, self.LOCAL_CONFIG_FILE)
                    with open(self.LOCAL_CONFIG_FILE, "r") as f:
                        self.config_data = json.load(f)
                except Exception:
                    self.reset_to_defaults()
            else:
                self.reset_to_defaults()

    def validate_config(self) -> bool:
        """
        Validates whether current configuration values are within acceptable bounds.
        :return: True if configuration values are valid, False otherwise.
        """
        if not isinstance(self.config_data, dict):
            return False
        # Extract target camera screen width setting resolution parameter bounds check
        width = self.config_data.get(self.CAMERA_WIDTH, 640)
        # Extract target camera screen height settings parameter bounds limit check
        height = self.config_data.get(self.CAMERA_HEIGHT, 480)
        if not isinstance(width, int) or not isinstance(height, int):  # Ensure resolution parameters are clean integers
            return False
        if not (160 <= width <= 3840) or not (120 <= height <= 2160):
            return False
        # Extract target posture slouch deviation threshold pixels limit parameter value check
        slouch_th = self.config_data.get(self.SLOUCH_THRESHOLD, 40)
        if not isinstance(slouch_th, (int, float)) or not (5 <= slouch_th <= 500):  # Check threshold bounds range constraints
            return False
        # Extract target system frame refresh delay setting parameter in milliseconds
        frame_delay = self.config_data.get(self.FRAME_DELAY, 15)
        # Extract target slouch alert duration frame threshold limits parameter bounds
        alert_frames = self.config_data.get(self.TIME_TO_ALERT, 50)
        if not isinstance(frame_delay, int) or not isinstance(alert_frames, int):  # Verify framing delay variables type safety
            return False
        # Validate frame delay and alert frames constraints threshold values in range check
        if not (1 <= frame_delay <= 1000) or not (5 <= alert_frames <= 2000):
            return False
        # Retrieve maximum log size in bytes dynamically from configuration limits
        log_bytes = self.config_data.get("log_max_bytes", 1048576)
        # Retrieve max backup files count threshold constraint from configurations parameter
        log_backups = self.config_data.get("log_backup_count", 3)
        if not isinstance(log_bytes, int) or not isinstance(log_backups, int):  # Verify logging threshold integer types
            return False
        # Validate log bytes and backups settings parameter constraints range validation checks
        if not (1024 <= log_bytes <= 104857600) or not (0 <= log_backups <= 20):
            return False
        return True

    def get(self, key: str, default: Any = None) -> Any:  # Retrieve target setting by configuration key mapping
        """
        Retrieves a configuration value.
        """
        return self.config_data.get(key, default)  # Retrieve config key safely from internal memory map

    def set(self, key: str, value: Any) -> None:  # Set target configuration parameter value and commit changes
        """
        Sets a configuration value and saves changes to file.
        """
        self.config_data[key] = value  # Assign updated setting value to internal cache map
        self._save_to_file()

    def _save_to_file(self) -> None:
        """
        Saves current config dictionary to JSON file.
        """
        try:
            with open(self.LOCAL_CONFIG_FILE, "w") as f:
                json.dump(self.config_data, f, indent=2)
        except OSError:
            from logger_config import setup_logger
            setup_logger().error("Failed to write config data to local file.")  # Print file writing fallback errors

    def reset_to_defaults(self) -> bool:
        """
        Resets configurations to the default template.
        """
        try:
            from logger_config import setup_logger
            logger = setup_logger()
            logger.info("Resetting configuration parameters to factory defaults...")  # Print logging message on factory reset triggers
            if os.path.exists(self.DEFAULT_CONFIG_FILE):
                shutil.copy(self.DEFAULT_CONFIG_FILE, self.LOCAL_CONFIG_FILE)
                self.load()
            else:
                self.config_data = self.DEFAULT_SETTINGS.copy()
                self._save_to_file()
            return True
        except Exception:
            return False

    def get_config_filepath(self) -> str:  # Get canonical absolute pathname for active configuration settings
        """
        Returns the absolute path of the configuration file.
        """
        return os.path.abspath(self.LOCAL_CONFIG_FILE)

