# Face Tracking System with Servo (Raspberry Pi + YOLO)

## 📌 Overview
This project implements a real-time face tracking system using a **Raspberry Pi**, **Pi Camera**, **YOLO pose estimation**, and a **servo motor**.  

The system tracks the user’s face by detecting the nose position and dynamically rotating a servo to keep the face centered in the camera's field of view.



---

## 📑 Table of Contents
- [Hardware Used](#-hardware-used)
- [Software & Libraries](#-software-libraries)
- [LED Status Indicators](#-led-status)
- [How It Works](#-how-it-works)
- [Safety Precautions](#-safety)

---

## ⚙️ Hardware Used
* **Raspberry Pi** (Model 4 or 5 recommended)
* **Pi Camera** (Compatible with Picamera2)
* **Servo Motor** (SG90 or similar)
* **3 LEDs** (Green, Yellow, Red)
* **Resistors** (220Ω for LEDs)
* **External Power Supply** (Recommended for the servo)

---

## 🧠 Software & Libraries
The project is built with Python 3. Ensure you have the following installed:

* `OpenCV`: For image processing.
* `Picamera2`: For the camera interface.
* `Ultralytics YOLO`: For high-performance pose detection.
* `gpiozero` & `lgpio`: For GPIO pin control.

### Installation
```bash
pip install opencv-python ultralytics gpiozero lgpio

##🚦 LED StatusLEDMeaning🟢 GreenFace detected; Tracking active🟡 YellowFace recently lost; Searching...🔴 RedNo face detected🔄 How It WorksCapture: Grabs a frame from the Pi Camera.Detect: Runs YOLO pose detection to identify facial keypoints.Extract: Pinpoints the $(x, y)$ coordinates of the nose.Smooth: Averages the last few positions to prevent jittery movement.Calculate: Measures the "error" (distance) from the center of the frame.Move: Adjusts the servo angle to bring the nose back to the center.Update: Switches the LED indicators based on detection status.▶️ Run the ProjectTo start the tracking system, execute:Bashpython3 main.py

🛑 Safety[!CAUTION]Power Supply: Use an external power supply for the servo motor. Do not power the servo directly from the Raspberry Pi's 5V pins, as the current spikes can cause the Pi to reboot or damage the GPIO header.
Would you like me to help you write the **Python code (`main.py`)** to make this s
