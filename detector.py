from ultralytics import YOLO
from config import MODEL_PATH, OBSTACLE_CLASSES, DANGER_BOX_THRESHOLD
import cv2

# Load model once
model = YOLO(MODEL_PATH)

def detect_obstacles(frame):
    """
    Takes a video frame, runs YOLO, returns list of detected obstacles.
    Each obstacle is a dict with: label, confidence, box, is_danger
    """
    height, width = frame.shape[:2]
    results = model(frame, verbose=False)[0]  # Run detection

    obstacles = []

    for box in results.boxes:
        # Get class name
        class_id = int(box.cls[0])
        label = model.names[class_id]

        # Only care about obstacle objects
        if label not in OBSTACLE_CLASSES:
            continue

        confidence = float(box.conf[0])
        if confidence < 0.4:  # Skip low confidence detections
            continue

        # Get bounding box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        box_width = x2 - x1

        # Check if object is dangerously close
        # (if its box takes up more than 25% of screen width)
        is_danger = (box_width / width) > DANGER_BOX_THRESHOLD

        obstacles.append({
            "label": label,
            "confidence": confidence,
            "box": (x1, y1, x2, y2),
            "is_danger": is_danger
        })

    return obstacles