import os
import json
import shutil
from typing import Any, Dict


class ConfigManager:
    """
    Manages local application configuration JSON files.
    Copies default settings, reads config parameters, and handles runtime updates.
    """
    DEFAULT_CONFIG_FILE = "config.json.default"
    LOCAL_CONFIG_FILE = "config.json"
    
    # Key Constants
    CAMERA_INDEX = "camera_index"
    SLOUCH_THRESHOLD = "slouch_threshold_px"
    TIME_TO_ALERT = "time_to_alert_frames"
    FRAME_DELAY = "frame_delay_ms"
    CAMERA_WIDTH = "camera_width"
    CAMERA_HEIGHT = "camera_height"
    SAVE_HISTORY = "save_history"
    SAVED_BASELINE_Y = "saved_baseline_y"

    def __init__(self) -> None:
        """
        Initializes the ConfigManager, ensuring that a local config.json exists.
        Loads the config into an in-memory dictionary.
        """
        self.config_data: Dict[str, Any] = {}
        self._ensure_config_exists()
        self.load()

    def _ensure_config_exists(self) -> None:
        """
        Helper method to copy config.json.default to config.json if the latter is missing.
        """
        if not os.path.exists(self.LOCAL_CONFIG_FILE):
            if os.path.exists(self.DEFAULT_CONFIG_FILE):
                shutil.copy(self.DEFAULT_CONFIG_FILE, self.LOCAL_CONFIG_FILE)
            else:
                # Fallback internal defaults if config.json.default is also missing
                self.config_data = {
                    "camera_index": 0,
                    "slouch_threshold_px": 40,
                    "time_to_alert_frames": 50,
                    "frame_delay_ms": 15,
                    "camera_width": 640,
                    "camera_height": 480,
                    "save_history": True,
                    "saved_baseline_y": None
                }
                self._save_to_file()

    def load(self) -> None:
        """
        Loads configuration dictionary from the local file.
        """
        try:
            with open(self.LOCAL_CONFIG_FILE, "r") as f:
                self.config_data = json.load(f)
                if not isinstance(self.config_data, dict):
                    raise ValueError("Config format invalid, must be a dictionary")
        except (json.JSONDecodeError, OSError, ValueError):
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
        width = self.config_data.get(self.CAMERA_WIDTH, 640)
        height = self.config_data.get(self.CAMERA_HEIGHT, 480)
        if not isinstance(width, int) or not isinstance(height, int):
            return False
        if not (160 <= width <= 3840) or not (120 <= height <= 2160):
            return False
        return True

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves a configuration value.
        """
        return self.config_data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Sets a configuration value and saves changes to file.
        """
        self.config_data[key] = value
        self._save_to_file()

    def _save_to_file(self) -> None:
        """
        Saves current config dictionary to JSON file.
        """
        try:
            with open(self.LOCAL_CONFIG_FILE, "w") as f:
                json.dump(self.config_data, f, indent=2)
        except OSError:
            pass

    def reset_to_defaults(self) -> None:
        """
        Resets configurations to the default template.
        """
        if os.path.exists(self.DEFAULT_CONFIG_FILE):
            shutil.copy(self.DEFAULT_CONFIG_FILE, self.LOCAL_CONFIG_FILE)
            self.load()
        else:
            self.config_data = {
                "camera_index": 0,
                "slouch_threshold_px": 40,
                "time_to_alert_frames": 50,
                "frame_delay_ms": 15,
                "camera_width": 640,
                "camera_height": 480,
                "save_history": True,
                "saved_baseline_y": None
            }
            self._save_to_file()

