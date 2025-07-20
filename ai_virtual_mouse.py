import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math
import os

# Optional: suppress TensorFlow Lite logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Initialize modules
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Create named window and set it always on top
cv2.namedWindow("AI Virtual Mouse", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("AI Virtual Mouse", cv2.WND_PROP_TOPMOST, 1)

# Smoothing variables
prev_x, prev_y = 0, 0
smoothening = 6

# State variables
dragging = False
scroll_start_y = None

def get_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

            # Get coordinates of key fingers
            lm = hand_landmarks.landmark
            index_tip = int(lm[8].x * w), int(lm[8].y * h)
            thumb_tip = int(lm[4].x * w), int(lm[4].y * h)
            middle_tip = int(lm[12].x * w), int(lm[12].y * h)
            ring_tip = int(lm[16].x * w), int(lm[16].y * h)

            # Cursor movement (Index finger only)
            screen_x = np.interp(index_tip[0], (0, w), (0, screen_width))
            screen_y = np.interp(index_tip[1], (0, h), (0, screen_height))
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening
            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Left Click (Thumb + Index)
            if get_distance(index_tip, thumb_tip) < 30:
                pyautogui.click()
                cv2.putText(frame, "Left Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Right Click (Thumb + Middle)
            elif get_distance(middle_tip, thumb_tip) < 30:
                pyautogui.click(button='right')
                cv2.putText(frame, "Right Click", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Gesture detection
            close_index_middle = get_distance(index_tip, middle_tip) < 25
            thumb_closed = get_distance(thumb_tip, ring_tip) < 30

            # Drag and Hold
            if close_index_middle and not thumb_closed:
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
                cv2.putText(frame, "Dragging", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

            # Scroll
            if close_index_middle and thumb_closed:
                if scroll_start_y is None:
                    scroll_start_y = index_tip[1]
                direction = index_tip[1] - scroll_start_y
                if abs(direction) > 15:
                    pyautogui.scroll(-30 if direction > 0 else 30)
                    scroll_text = "Scroll Down" if direction > 0 else "Scroll Up"
                    cv2.putText(frame, scroll_text, (10, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    scroll_start_y = index_tip[1]
            else:
                scroll_start_y = None

    cv2.imshow("AI Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("AI Virtual Mouse", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
