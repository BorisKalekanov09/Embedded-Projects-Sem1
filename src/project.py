import cv2
import time
import os
from collections import deque

from picamera2 import Picamera2
from ultralytics import YOLO
from gpiozero import AngularServo, LED
from gpiozero.pins.lgpio import LGPIOFactory

# ---------------- LOGGING ----------------
LOG_FILE = "/home/boris/facetrack.log"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {msg}\n")

# ---------------- CONFIG ----------------
MODEL_PATH = "/home/boris/Downloads/Core Pose Estimation Collection/yolo11n-pose.pt"

GPIO_SERVO_PIN = 18
GPIO_GREEN_LED = 23
GPIO_YELLOW_LED = 24
GPIO_RED_LED = 25

SERVO_MIN_PULSE = 0.0005
SERVO_MAX_PULSE = 0.0024

INNER_ZONE = 0.15
BUFFER_SIZE = 15
SERVO_UPDATE_INTERVAL = 1.0

SERVO_MIN_ANGLE = 60
SERVO_MAX_ANGLE = 120
SERVO_CENTER = 90

NO_FACE_TIMEOUT = 3.0

# ---------------- INIT ----------------
log("Starting Face Tracking")

factory = LGPIOFactory()

servo = AngularServo(
    GPIO_SERVO_PIN,
    min_angle=0,
    max_angle=180,
    min_pulse_width=SERVO_MIN_PULSE,
    max_pulse_width=SERVO_MAX_PULSE,
    pin_factory=factory
)

servo.angle = SERVO_CENTER
current_angle = SERVO_CENTER
time.sleep(0.5)

led_green = LED(GPIO_GREEN_LED)
led_yellow = LED(GPIO_YELLOW_LED)
led_red = LED(GPIO_RED_LED)

led_green.off()
led_yellow.off()
led_red.off()

if not os.path.exists(MODEL_PATH):
    log("ERROR: YOLO model not found")
    raise FileNotFoundError("YOLO model missing")

model = YOLO(MODEL_PATH)

picam2 = Picamera2()
picam2.configure(
    picam2.create_preview_configuration(
        main={"size": (640, 480), "format": "RGB888"}
    )
)
picam2.start()

face_buffer = deque(maxlen=BUFFER_SIZE)
last_servo_update = time.time()
last_face_time = time.time()

log("Initialization complete")

# ---------------- MAIN LOOP ----------------
try:
    while True:
        frame = picam2.capture_array()
        results = model.predict(frame, verbose=False, conf=0.65, imgsz=320)

        face_x = None
        face_detected = False

        if results[0].keypoints is not None and len(results[0].keypoints.xyn) > 0:
            kp = results[0].keypoints.xyn[0]
            if len(kp) > 0:
                nose_x, _ = kp[0]
                if nose_x > 0:
                    face_x = nose_x.item()
                    face_detected = True
                    last_face_time = time.time()

        if face_x is not None:
            face_buffer.append(face_x)

        now = time.time()
        if now - last_servo_update >= SERVO_UPDATE_INTERVAL:
            last_servo_update = now

            if len(face_buffer) > 0:
                avg_face = sum(face_buffer) / len(face_buffer)
                error = 0.5 - avg_face

                target_angle = SERVO_CENTER + error * (SERVO_MAX_ANGLE - SERVO_CENTER)
                target_angle = max(SERVO_MIN_ANGLE, min(SERVO_MAX_ANGLE, target_angle))

                if abs(error) >= INNER_ZONE:
                    servo.angle = target_angle
                    current_angle = target_angle
                else:
                    servo.detach()

        time_since_last_face = time.time() - last_face_time

        if face_detected:
            led_green.on()
            led_yellow.off()
            led_red.off()
        elif time_since_last_face < NO_FACE_TIMEOUT:
            led_green.off()
            led_yellow.on()
            led_red.off()
        else:
            led_green.off()
            led_yellow.off()
            led_red.on()

        time.sleep(0.01)

except Exception as e:
    log(f"CRASH: {e}")

finally:
    log("Shutting down")
    servo.detach()
    led_green.off()
    led_yellow.off()
    led_red.off()
    picam2.stop()


