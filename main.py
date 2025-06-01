import cv2
import pyautogui
from hand_tracker import HandTracker
from gesture_controller import GestureController

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    controller = GestureController(*pyautogui.size())

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('g'):
            enabled = controller.toggle_gesture()

        landmarks = tracker.get_landmarks(frame)

        if landmarks and controller.gesture_enabled:
            index_x, index_y = int(landmarks[8].x * w), int(landmarks[8].y * h)
            controller.move_mouse(index_x, index_y, w, h)
            controller.handle_gestures(landmarks, w, h)

        # Visual overlay for status and instructions
        status_text = f'Gesture Mode: {"ON" if controller.gesture_enabled else "OFF"}'
        cv2.putText(frame, status_text, (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.putText(frame, "Press 'g' to Toggle Gestures | 'q' to Quit", (10, h - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

        cv2.imshow("Virtual Mouse", frame)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
