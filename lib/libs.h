import cv2
import time
import os
from collections import deque

from picamera2 import Picamera2
from ultralytics import YOLO
from gpiozero import AngularServo, LED
from gpiozero.pins.lgpio import LGPIOFactory
