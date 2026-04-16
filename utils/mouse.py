import cv2
import mediapipe as mp
import pyautogui

# 화면 크기 가져오기
screen_w, screen_h = pyautogui.size()

# MediaPipe 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# 웹캠 열기
cap = cv2.VideoCapture(0)

def is_fist(hand_landmarks):
    # 손가락 끝 landmark index
    tips = [8, 12, 16, 20]

    folded = 0
    for tip in tips:
        # tip이 바로 아래 관절보다 아래에 있으면 접힌 상태
        if hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y:
            folded += 1

    return folded >= 3  # 대부분 접히면 주먹

clicked = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # 좌우 반전
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # 손 그리기
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 검지 끝 (index finger tip)
            index_finger = hand_landmarks.landmark[8]

            # 화면 좌표로 변환
            mouse_x = int(index_finger.x * screen_w)
            mouse_y = int(index_finger.y * screen_h)

            pyautogui.moveTo(mouse_x, mouse_y)

            # 주먹 감지
            if is_fist(hand_landmarks):
                if not clicked:
                    pyautogui.click()
                    clicked = True
            else:
                clicked = False

    cv2.imshow("Motion Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
