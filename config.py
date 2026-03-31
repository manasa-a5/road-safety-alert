# ===== SETTINGS =====

# Your phone's IP address from IP Webcam app (change this!)
MOBILE_CAM_URL = "http://10.88.158.222:8080/video"

# Use 0 for laptop webcam instead of phone
USE_WEBCAM = False

# YOLO model (yolov8n = smallest/fastest, good for beginners)
MODEL_PATH = "yolov8n.pt"

# Warning distance threshold (bigger box = closer object)
DANGER_BOX_THRESHOLD = 0.25  # 25% of screen width = danger zone

# Objects to detect as obstacles
OBSTACLE_CLASSES = [
    "person", "car", "truck", "bus", "motorcycle",
    "bicycle", "dog", "cat", "horse", "cow",
    "traffic light", "stop sign", "suitcase"
]