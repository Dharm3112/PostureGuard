# Changelog

All notable changes to this project will be documented in this file.

## [1.8.0] - 2026-07-13

### Added
- **Extended Diagnostics Exceptions:** Added 25 diagnostic exception classes covering file locks, system permissions, capture timeouts, assets corruption, and buffer states.
- **Robust Exception Coverage:** Added 25 unit test cases verifying correct initialization, error codes, and message bindings for all diagnostic exceptions.
- **System Config and Logger Comments:** Added inline annotations inside `config_manager.py` and `logger_config.py` clarifying stream configurations.

### Changed
- **Codebase Health Check:** Validated the application test suite on each incremental update.


## [1.7.0] - 2026-07-11

### Added
- **Stream Exception Models:** Declared 12 specialized exception subclasses for OpenCV canvas failures, speaker hardware errors, and notification permissions.
- **Detailed Layout Comments:** Added inline annotations inside `main.py` and `posture_detector.py` explaining camera stream captures, top-level protocol settings, and face coordinate evaluations.

### Changed
- **Unit Test Coverage:** Added unit test validation checks for all new exceptions.


## [1.6.0] - 2026-07-05

### Added
- **Dynamic File Exceptions:** Declared 12 specialized exception subclasses for stats files reads, config restores, and JSON backups.
- **Detailed Layout Comments:** Added inline annotations inside `main.py` and `posture_detector.py` explaining dropdown selections, coordinate buffer counts, and color parameters mapping.

### Changed
- **Unit Test Coverage:** Added unit test validation checks for all new exceptions.


## [1.5.0] - 2026-07-04

### Added
- **GUI Exception System:** Declared 12 specialized exception subclasses for specific GUI and camera thread components.
- **Detailed Layout Comments:** Added inline explanations inside `main.py` and `posture_detector.py` documenting frame rendering, buttons grid parameters, and stats modals layout configurations.

### Changed
- **Unit Test Coverage:** Added unit test suites verifying messages and class mapping properties for all new exceptions.


## [1.4.0] - 2026-07-02

### Added
- **Configuration Parameter Constraints:** Improved validator inline documentations and added range check validations.
- **Multithreading Stream Documentation:** Expanded detailed technical comments on background `CameraStream` daemon properties.
- **Tkinter Layout Comments:** Added inline annotations explaining Tkinter center window properties, colors palette constants, and rescheduling delay configurations.

### Changed
- **Unit Test Coverage:** Added unit tests verifying validation boundaries for frame delay, alert threshold frames, and log settings.


## [1.3.0] - 2026-06-25

### Added
- **Hover Status Bar Descriptions:** Buttons update the status bar helper text dynamically on hover transitions.
- **Config Path Retrieval Method:** Added `get_config_filepath()` helper to fetch the configuration JSON path.
- **Buffer Reset Capabilities:** Added `reset_buffer()` to clean the posture tracker's active buffers.
- **Configuration Save Exception:** Introduced `ConfigurationSaveError` custom class to handle configuration writing issues.

### Changed
- **Type Annotations in Stats Engine:** Expanded type hint clarity and safety inside statistics parsing functions.


## [1.2.0] - 2026-06-23

### Added
- **Hover Highlights on Buttons:** Enhances UI navigation feedback visual details.
- **Quit Confirmations Dialogs:** Prevents accidental closures of the app tracker.
- **Centralized Layout paddings:** Cleaner UI alignment definitions constants.
- **Log rotation parameter loading:** Dynamic configs load rotation limits parameter bounds checks.
- **Stats File Reset Capability:** Clear logs instantly without manually searching directory logs.


## [1.1.0] - 2026-06-22

### Added
- **Configuration Parameter Validation:** Added checks for slouch thresholds, camera widths/heights, and frame timings.
- **Robust Exception Logging:** Custom exceptions are fully documented and file logs capture write errors.
- **Unit Test Suites:** Expanded unittest coverages for configs, statistics calculators, and detector geometries.
- **Keyboard Shortcuts:** Added `Ctrl+C` for clean closure and `Ctrl+L` for instant calibration trigger.


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
