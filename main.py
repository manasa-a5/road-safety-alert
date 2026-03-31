import cv2
from camera import get_camera
from detector import detect_obstacles
from alert import draw_detections

def main():
    print("=" * 50)
    print("  Road Obstacle Detection System")
    print("  Press 'Q' to quit")
    print("=" * 50)

    # Connect to camera
    cap = get_camera()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("[ERROR] Failed to read frame. Check camera connection.")
            break

        # Resize for faster processing
        frame = cv2.resize(frame, (1280, 720))

        # Detect obstacles in current frame
        obstacles = detect_obstacles(frame)

        # Draw boxes and warnings on frame
        frame = draw_detections(frame, obstacles)

        # Show object count
        cv2.putText(frame, f"Objects: {len(obstacles)}", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

        # Display the frame
        cv2.imshow("Road Obstacle Detection", frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Quitting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



