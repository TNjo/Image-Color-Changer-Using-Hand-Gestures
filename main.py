import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.8)
cap = cv2.VideoCapture(0)  # 0 for webcam

left_threshold = 490
right_threshold = 150

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # with draw

    if len(hands) == 2:
        left_hand = hands[1]
        right_hand = hands[0]

        left_position = left_hand["lmList"][8][0] if left_hand["lmList"] else None
        right_position = right_hand["lmList"][8][0] if right_hand["lmList"] else None

        if left_position is not None and left_position >= left_threshold:
            print("turn left")
            pyautogui.press('left')  # Simulate pressing the left arrow key

        if right_position is not None and right_position <= right_threshold:
            print("turn right")
            pyautogui.press('right')  # Simulate pressing the right arrow key

    cv2.line(img, (right_threshold, 0), (right_threshold, 480), (255, 0, 255), 3)
    cv2.line(img, (left_threshold, 0), (left_threshold, 480), (255, 0, 255), 3)

    cv2.imshow('Filter', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
