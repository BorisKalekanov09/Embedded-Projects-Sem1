# 🎯 Face Tracking System with Servo

## 📌 Overview

A real-time face tracking system that uses a **Pi Camera**, **YOLO pose estimation**, and a **servo motor** to keep the user's face centered in frame — automatically.

The system detects the nose keypoint, calculates its offset from the frame center, and rotates the servo to correct it. LED indicators provide live visual feedback on tracking status.

---

## 📑 Table of Contents

- Hardware Used  
- Software & Libraries  
- How It Works  
- LED Status Indicators  
- Running the Project  
- Safety Precautions

---

## ⚙️ Hardware Used

| Component | Details |
|---|---|
| 🖥️ Raspberry Pi | Model 4 or 5 recommended |
| 📷 Pi Camera | Compatible with Picamera2 |
| 🔧 Servo Motor | SG90 or similar |
| 💡 LEDs | Green, Yellow, Red |
| ⚡ Resistors | 220Ω for each LED |
| 🔌 Power Supply | External supply recommended for servo |

---

## 🧠 Software & Libraries

Built with **Python 3**. Install all dependencies with:

```bash
pip install opencv-python ultralytics gpiozero lgpio
```

| Library | Purpose |
|---|---|
| `opencv-python` | Image processing & frame capture |
| `picamera2` | Pi Camera interface |
| `ultralytics` | YOLO pose estimation |
| `gpiozero` + `lgpio` | GPIO and servo control |

---

## 🔄 How It Works

```
📷 Capture  →  🧠 Detect  →  📍 Extract  →  〰️ Smooth  →  📐 Calculate  →  🔧 Move  →  💡 Update
```

1. **Capture** — Grabs a live frame from the Pi Camera
2. **Detect** — Runs YOLO pose estimation to find facial keypoints
3. **Extract** — Pinpoints the `(x, y)` coordinates of the nose
4. **Smooth** — Averages recent positions to eliminate jitter
5. **Calculate** — Measures the error (offset from frame center)
6. **Move** — Adjusts servo angle to re-center the nose
7. **Update** — Switches LED indicators based on detection state

---

## 🚦 LED Status Indicators

| LED | Status | Meaning |
|---|---|---|
| 🟢 Green | `TRACKING` | Face detected — servo actively following |
| 🟡 Yellow | `SEARCHING` | Face recently lost — holding last position |
| 🔴 Red | `IDLE` | No face detected |

---

## ▶️ Running the Project

```bash
python3 main.py
```

---

## 🛑 Safety Precautions

> [!CAUTION]
> **Power Supply Warning:** Always use an **external power supply** for the servo motor.
>
> Powering the servo directly from the Raspberry Pi's 5V pins can cause:
> - Unexpected **reboots** due to current spikes
> - Permanent **damage to the GPIO header**
>
> Use a dedicated 5V supply capable of at least **1A** for the servo.

---

## 📁 Project Structure

```
face-tracker/
├── main.py          # Entry point — starts the tracking loop
├── README.md        # This file
└── requirements.txt # Python dependencies
```

---

[Full guide](https://core-electronics.com.au/guides/raspberry-pi/getting-started-with-yolo-pose-estimation-on-the-raspberry-pi/)
