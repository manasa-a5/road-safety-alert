import cv2
import os

# Try to load pygame for audio (optional)
try:
    import pygame
    pygame.mixer.init()
    AUDIO_AVAILABLE = True
except:
    AUDIO_AVAILABLE = False
    print("[WARNING] pygame not working, no audio alerts")

last_alert_time = 0

def play_audio_alert():
    """Plays a beep sound if obstacle is detected"""
    global last_alert_time
    import time
    current_time = time.time()

    # Only beep every 2 seconds (not constantly)
    if AUDIO_AVAILABLE and (current_time - last_alert_time) > 2:
        sound_path = "sounds/alert.wav"
        if os.path.exists(sound_path):
            pygame.mixer.Sound(sound_path).play()
        last_alert_time = current_time

def draw_detections(frame, obstacles):
    """
    Draws bounding boxes and warning labels on the frame.
    - Green box = detected but safe distance
    - Red box = DANGER! too close
    """
    danger_detected = False

    for obj in obstacles:
        x1, y1, x2, y2 = obj["box"]
        label = obj["label"]
        conf = obj["confidence"]
        is_danger = obj["is_danger"]

        if is_danger:
            color = (0, 0, 255)   # Red for danger
            danger_detected = True
            warning_text = f"⚠ DANGER: {label}"
        else:
            color = (0, 255, 0)    # Green for safe
            warning_text = f"{label} ({conf:.0%})"

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        # Draw label background
        (tw, th), _ = cv2.getTextSize(warning_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(frame, (x1, y1 - th - 8), (x1 + tw + 4, y1), color, -1)

        # Draw label text
        cv2.putText(frame, warning_text, (x1 + 2, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Big red warning at top if danger
    if danger_detected:
        cv2.rectangle(frame, (0, 0), (frame.shape[1], 50), (0, 0, 200), -1)
        cv2.putText(frame, "⚠ WARNING: OBSTACLE AHEAD!", (10, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        play_audio_alert()

    return frame