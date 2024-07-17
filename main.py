import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random
import mediapipe

cap = cv2.VideoCapture(0)  # This is initializing the camera
cap.set(3, 640)  # Here we are setting a fixed size (width to 640) in every case be it with a pc or webcam
cap.set(3, 480)  # Setting a fixed height

detector = HandDetector(maxHands=1)  # This helps detect the hand

