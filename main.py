import hand
import gestures
import cv2
import mediapipe as mp
import numpy as np
import time


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)
    myhands = hand.Hand()
    state = gestures.Context()
    while cap.isOpened():
        success, image = cap.read()
        for i in range(10):
            success2, image2 = cap.read()

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        # Draw the hand annotations on the image.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            myhands.input(results)
            myhands.offset()
            myhands.adjust()
            myhands.rotate()
            myhands.output()
            kindofhands = myhands.recognize(results)
            state.change_state(kindofhands)
            state.operate()
            if kindofhands != 'NoDetected':
                time.sleep(5)
    cap.release()
