# 🧘 PostureGuard

**PostureGuard** is a lightweight, real-time desktop application designed to help you maintain healthy posture while working at your computer. 

It acts as a private "digital health coach" that runs in the background. By using your webcam and Computer Vision, it establishes a baseline for your correct sitting position and alerts you if you slouch or drop your head for a sustained period.

> **Note:** This version is specifically optimized for **Python 3.10+** compatibility, removing heavy dependencies like MediaPipe in favor of efficient OpenCV Haar Cascades.

---

## 🚀 Features

* **Real-Time Monitoring:** Tracks vertical head movement at 30 FPS using local OpenCV face detection.
* **Multithreaded Camera Stream:** Utilizes a separate background grabber thread (`CameraStream`) to eliminate GUI stutter and latency.
* **Persistent Calibration:** Remembers your ideal calibration baseline coordinates between application runs so you only calibrate once.
* **Dynamic Settings Panel:** Configure webcam device index, video resolution, slouch pixels threshold, system frame timing, and refresh delays directly inside the GUI at runtime.
* **Privacy Focused:** All processing happens locally on your CPU. No images or video are ever sent to the cloud.
* **Smart Alerts:**
    * **Visual Status:** On-screen text changes dynamically from Green (Good) to Red (Slouching).
    * **System Notifications:** Desktop alerts pop up when poor posture is sustained for too long.
* **Posture Statistics Logs:** Periodically records posture metrics to `posture_history.csv` and displays a formatted aggregate statistics screen (percentages of good vs bad posture, average deviation).
* **Robust Logging:** Outputs status messages and error states to console and a rotating local log file (`posture_guard.log`).

---

## 🛠️ Project Structure

```text
PostureGuard/
│
├── assets/                 # Application icon assets (PNG/ICO)
├── tests/                  # Unit test suite verifying components
│   ├── test_posture_detector.py
│   └── test_config_manager.py
│
├── main.py                 # GUI, event loop, and camera grabber thread
├── posture_detector.py     # Core computer vision head tracking logic
├── config_manager.py       # JSON configuration reader/writer helper
├── logger_config.py        # Rotating console/file logger setup helper
├── exceptions.py           # Custom application runtime exception classes
├── stats.py                # CSV history statistics parsing engine
├── config.json.default     # Baseline template for system configuration
├── requirements.txt        # Third-party libraries
├── pyproject.toml          # Packaging metadata and tool configurations
├── run.bat / run.sh        # Windows and Unix-like launch scripts
└── README.md               # Documentation
```

---

## 💻 Installation

### Prerequisites

* Python 3.10 or higher
* A webcam

### Step 1: Clone or Download

Download this project folder to your local machine.

### Step 2: Set up Virtual Environment (Recommended)

Open your terminal in the project folder:

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (Mac/Linux)
source .venv/bin/activate
```

### Step 3: Install Dependencies

Install the required libraries (OpenCV, Pillow, Plyer, Numpy):

```bash
pip install -r requirements.txt
```

---

## 🎮 How to Use

1. **Run the Application:**
   * On Windows: double click `run.bat` or run:
     ```bash
     python main.py
     ```
   * On Linux/macOS: run `bash run.sh` or run:
     ```bash
     python main.py
     ```

2. **Calibrate:**
   Sit up straight in your ideal "healthy" posture. Click the **"Sit Straight & Calibrate"** button. The application will record this height baseline and save it to your local configuration.

3. **Custom Settings:**
   Click **"Settings"** to change webcam index, resolution, slouch threshold (default: 40 pixels), time to alert, and refresh delay. Saving settings automatically re-applies configurations and re-initializes the webcam if device index changes.

4. **Pause/Resume:**
   Click **"Pause"** to pause posture tracking when stepping away, and click **"Resume"** to restart monitoring.

5. **Track Progress:**
   Click **"Stats"** to open a display dialog analyzing your recorded posture metrics (good posture percentage, slouch events, average deviation).

---

## 🧪 Running Unit Tests

Verify project components using Python's built-in `unittest` runner:

```bash
python -m unittest discover -s tests
```

---

## 📜 License

This project is open-source and free to use for personal health and educational purposes.
