import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Webcam
cap = cv2.VideoCapture(0)

def fingers_up(landmarks):
    fingers = []
    fingers.append(landmarks[4].x < landmarks[3].x)  # Thumb (for right hand)
    fingers.append(landmarks[8].y < landmarks[6].y)  # Index
    fingers.append(landmarks[12].y < landmarks[10].y)  # Middle
    fingers.append(landmarks[16].y < landmarks[14].y)  # Ring
    fingers.append(landmarks[20].y < landmarks[18].y)  # Pinky
    return fingers
    
# Calculate Euclidean distance
def distance(lm1, lm2, w, h):
    x1, y1 = int(lm1.x * w), int(lm1.y * h)
    x2, y2 = int(lm2.x * w), int(lm2.y * h)
    return math.hypot(x2 - x1, y2 - y1)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(hand_landmarks.landmark)

            # Distances between fingertips
            d_thumb_index = distance(hand_landmarks.landmark[4], hand_landmarks.landmark[8], w, h)
            d_index_middle = distance(hand_landmarks.landmark[8], hand_landmarks.landmark[12], w, h)
            d_middle_ring = distance(hand_landmarks.landmark[12], hand_landmarks.landmark[16], w, h)
            d_ring_pinky = distance(hand_landmarks.landmark[16], hand_landmarks.landmark[20], w, h)

            gesture = "Unknown"

            # Define gesture based on finger distances
            if d_thumb_index < 36 and d_index_middle < 36 and d_middle_ring < 36 and d_ring_pinky < 36 and fingers == [False, False, False, False, False]:
                gesture = "Fist"
            elif d_thumb_index > 60 and d_index_middle > 43 and d_middle_ring > 41 and d_ring_pinky > 41 and fingers == [True, True, True, True, True]:
                gesture = "Open Palm"
            elif d_thumb_index > 60 and d_index_middle > 45 and d_middle_ring > 100 and d_ring_pinky < 40 and fingers == [False, True, True, False, False]:
                gesture = "Victory"
            elif d_thumb_index > 60 and d_index_middle > 41 and d_middle_ring < 41 and d_ring_pinky < 41 and fingers == [False, True, False, False, False]:
                gesture = "One Finger"
            elif d_thumb_index > 60 and d_index_middle > 43 and d_middle_ring > 41 and d_ring_pinky > 100 and fingers == [False, True, True, True, False]:
                gesture = "Three Fingers"
            elif d_thumb_index > 60 and d_index_middle > 43 and d_middle_ring > 41 and d_ring_pinky > 41 and fingers == [False, True, True, True, True]:
                gesture = "Four Fingers"
            elif d_thumb_index > 80 and d_index_middle < 40 and d_middle_ring < 41 and d_ring_pinky > 66: #and fingers == [True, True, False, False, True]:
                gesture = "Call"
            elif d_thumb_index > 80 and d_index_middle > 40 and d_middle_ring < 41 and d_ring_pinky > 60 and fingers == [True, True, False, False, True]:
                gesture = "Rock"
            elif d_thumb_index > 80 and d_index_middle > 40 and d_middle_ring < 41 and d_ring_pinky > 40 and fingers == [False, True, False, False, True]:
                gesture = "SpiderMan"
            elif d_thumb_index > 106 and d_index_middle < 40 and d_middle_ring < 41 and d_ring_pinky < 41:
                gesture = "Thumbs Up"
            elif d_thumb_index < 36 and d_index_middle > 100 and d_middle_ring > 42 and d_ring_pinky > 40:
                gesture = "Noice"
            elif d_thumb_index > 145 and d_index_middle > 41 and d_middle_ring < 41 and d_ring_pinky < 41 and fingers == [True, True, False, False, False]:
                gesture = "Gun"    

            x = int(hand_landmarks.landmark[0].x * w)
            y = int(hand_landmarks.landmark[0].y * h)
            cv2.putText(frame, f"Gesture: {gesture}", (x - 50, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Hand Gesture Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("Hand Gesture Detection", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()