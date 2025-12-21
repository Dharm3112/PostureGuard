
# 🧘 PostureGuard

**PostureGuard** is a lightweight, real-time desktop application designed to help you maintain healthy posture while working at your computer. 

It acts as a private "digital health coach" that runs in the background. By using your webcam and Computer Vision, it establishes a baseline for your correct sitting position and alerts you if you slouch or drop your head for a sustained period.

> **Note:** This "Lite" version is specifically optimized for **Python 3.13+** compatibility, removing heavy dependencies like MediaPipe in favor of efficient OpenCV Haar Cascades.

---

## 🚀 Features

* **Real-Time Monitoring:** Uses OpenCV face detection to track vertical head movement at 30 FPS.
* **Privacy Focused:** All processing happens locally on your CPU. No images or video are ever sent to the cloud.
* **Adaptive Calibration:** "One-click" calibration allows the system to learn *your* specific desk setup and height.
* **Smart Alerts:**
    * **Visual Status:** On-screen text changes from Green (Good) to Red (Slouching).
    * **Desktop Notifications:** Native system notifications (Windows/Mac/Linux) pop up if you ignore bad posture for too long.
* **Jitter Smoothing:** Includes a buffer system to prevent false alarms from tiny movements.

---

## 🛠️ Project Structure

```text
PostureGuard/
│
├── main.py                 # Entry point: GUI, Event Loop, and Alert Logic
├── posture_detector.py     # Core Logic: OpenCV Face Detection & Math
├── requirements.txt        # List of dependencies
└── README.md               # Documentation

```

---

## 💻 Installation

### Prerequisites

* Python 3.10 or higher (Fully compatible with **Python 3.13**)
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
```bash
python main.py

```


2. **Position Yourself:**
Sit comfortably in your chair. Ensure your webcam can see your face. You should see a **Green Box** drawn around your face.
3. **Calibrate:**
Sit up straight in your ideal "healthy" posture. Click the **"Sit Straight & Calibrate"** button.
* *What happens?* The system records your face's Y-coordinate (height) and draws a yellow "Limit Line" below your chin.


4. **Work:**
Minimize the window or leave it open.
* If you slouch (your face drops below the yellow line) for more than **3 seconds**, the status will turn **RED** and you will receive a system notification.



---

## ⚙️ Customization (Optional)

You can tweak the sensitivity by editing `main.py`:

* **Make it stricter:** Decrease `self.slouch_threshold` (default is `40` pixels).
```python
self.slouch_threshold = 25  # Alerts with smaller movements

```


* **Change Alert Timing:** Edit `self.TIME_TO_ALERT` (default is `50` frames).
```python
self.TIME_TO_ALERT = 90     # Wait ~3 seconds before alerting

```



---

## 🔧 Troubleshooting

**1. "Calibration Failed: No face detected"**

* Ensure your room is well-lit.
* Remove obstructions (masks, hands) from your face.
* Make sure no other app (Zoom, Teams) is using the webcam.

**2. False Alarms (Alerting when I'm straight)**

* Re-calibrate! If you shifted your chair or moved your laptop, your "baseline" is wrong. Click "Calibrate" again.

**3. Application crashes immediately**

* Ensure you have installed the requirements: `pip install -r requirements.txt`.

---

## 📜 License

This project is open-source and free to use for personal health and educational purposes.
[LICENSE](https://github.com/Dharm3112/PostureGuard/blob/main/LICENSE)

---

<p align="center">
  <b>PostureGuard</b> • Created by <a href="https://github.com/Dharm3112"><b>Dharm Patel</b></a>
</p>
