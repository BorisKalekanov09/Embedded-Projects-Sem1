# Embedded-Projects-Sem1
# Face Tracking System with Servo (Raspberry Pi + YOLO)

## 📌 Overview
This project implements a real-time face tracking system using a Raspberry Pi, Pi Camera, YOLO pose estimation, and a servo motor.  
The system tracks the user’s face by detecting the nose position and rotating a servo to keep the face centered.

---

## ⚙️ Hardware Used
- Raspberry Pi  
- Pi Camera (Picamera2)  
- Servo motor  
- 3 LEDs (Green, Yellow, Red)  
- External power supply for servo (recommended)

---

## 🧠 Software & Libraries
- Python 3  
- OpenCV  
- Picamera2  
- Ultralytics YOLO  
- gpiozero  
- lgpio  

Install dependencies:
```bash
pip install opencv-python ultralytics gpiozero lgpio
🚦 LED Status
LED	Meaning
🟢 Green	Face detected
🟡 Yellow	Face recently lost
🔴 Red	No face detected

🔄 How It Works
Capture frame from camera
Run YOLO pose detection
Extract nose position
Average last positions
Calculate error from center
Move servo
Update LEDs

▶️ Run
python3 main.py

🛑 Safety

Use external power for the servo

Do not power servo directly from Raspberry Pi
