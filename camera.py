import cv2
from config import MOBILE_CAM_URL, USE_WEBCAM

def get_camera():
    """
    Returns a video capture object.
    - If USE_WEBCAM is True: uses laptop webcam
    - If False: uses mobile phone camera via IP Webcam app
    """
    if USE_WEBCAM:
        print("[INFO] Using laptop webcam...")
        cap = cv2.VideoCapture(0)
    else:
        print(f"[INFO] Connecting to mobile camera: {MOBILE_CAM_URL}")
        cap = cv2.VideoCapture(MOBILE_CAM_URL)

    if not cap.isOpened():
        print("[ERROR] Cannot open camera!")
        print("Tips:")
        print("  - For mobile: Make sure phone and laptop are on same WiFi")
        print("  - For mobile: Check IP address in IP Webcam app")
        print("  - Try changing USE_WEBCAM = True in config.py")
        exit(1)

    print("[INFO] Camera connected successfully!")
    return cap