# 🤚🔊 Hand Gesture Volume Control

Control your system's volume using **hand gestures** detected via your webcam. This Python project uses **MediaPipe** for real-time hand tracking, **OpenCV** for video processing, and **Pycaw** to interface with Windows system audio.

---

## 📸 Demo

https://github.com/your-username/gesture-volume-control/assets/demo.gif  
*(Add your own GIF or video here demonstrating the volume control in action.)*

---

## 🛠️ Features

- Real-time hand tracking using **MediaPipe**
- Detects thumb and index finger distance
- Maps finger distance to system volume
- Visual volume bar overlay using OpenCV
- Works with any standard webcam
- Smooth and responsive volume control

---

## 📦 Requirements

- Python 3.7+
- Windows OS (required for Pycaw)
- Webcam

### 🔧 Install dependencies:

```bash
pip install opencv-python mediapipe pycaw comtypes numpy
