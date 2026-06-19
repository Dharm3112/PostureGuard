# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-19

### Added
- **Asynchronous Camera Capture:** Integrated background `CameraStream` thread to run frame capture in parallel, keeping Tkinter GUI responsive.
- **Dynamic Configuration Management:** Implemented `ConfigManager` to read, modify, and save configurations dynamically in a local JSON config.
- **Interactive Settings GUI:** Added a dynamic settings panel allowing configurations for Webcam Index, Resolution size, Slouch pixel threshold, Time to alert, and Frame refresh rate.
- **Persisted Calibration:** Calibrated baseline Y coordinates are now saved in settings and loaded on startup.
- **Posture History Tracking:** Periodically logs timestamp, deviation pixels, and state (Good vs Slouching) to `posture_history.csv`.
- **History Statistics Overview:** Added a detailed stats window parsing the history logs and calculating overall metrics (Good % vs Slouching %, average deviation, total count).
- **Custom Application Exceptions:** Created `CameraNotFoundError` and `ModelLoadError` for cleaner error catching and graphical notification handling.
- **Rotating File Logger:** Configured console and rotating file logger (`posture_guard.log`) utilizing Python's `RotatingFileHandler`.
- **Application Assets:** Created and configured posture-themed window icon assets (`icon.ico`, `icon.png`).
- **Comprehensive Unit Tests:** Created tests directory containing unittest suites verifying `PostureDetector` calibration and `ConfigManager` read/write hooks.
- **Project Packaging Config:** Integrated `pyproject.toml` definition defining project dependencies, GUI entry points, and developer lint tools.
- **CI Pipelines:** Configured GitHub Actions workflow for automated multi-Python-version unittest runs and style syntax verification.
- **Developer Documentation:** Created `CONTRIBUTING.md` defining team rules, type hint standards, and branch policies.

### Changed
- **Type Hints and Documentation:** Fully refactored `posture_detector.py` and `main.py` adding PEP-257 docstrings and static type annotations.
- **GUI Redesign:** Upgraded Tkinter elements to support a beautiful flat dark-mode color theme with customized Segoe UI typography and margins.
- **Clean Entrypoint:** Refactored main entrypoint loops to execute using standard `main()` methods.
- **Git Hygiene:** Created `.gitignore` excluding user configurations, cache files, and logs.
