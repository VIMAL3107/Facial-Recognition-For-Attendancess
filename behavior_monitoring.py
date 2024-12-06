import cv2
import time

def monitor_behavior(face_detected, last_detected_time, max_no_face_time=30):
    if not face_detected:
        current_time = time.time()
        if current_time - last_detected_time > max_no_face_time:
            return "No face detected for too long"
    return "Monitoring"
