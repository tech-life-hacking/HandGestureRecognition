import hand
import gestures
import cv2
import mediapipe as mp
import numpy as np

class Time():
    def __init__(self):
        self.skiptime = 5
        self.threshold = 15
        self.timer = self.threshold

    def set_timer(self):
        self.timer = 0

    def count(self):
        self.timer += 1
        if self.timer > self.threshold:
            self.timer = 0

class Templete():
    def run(self):
        while cap.isOpened():
            success, image = cap.read()
            for i in range(5):
                success2, image2 = cap.read()

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            signalacceptedtimer.count()
            if signalacceptedtimer.timer % signalacceptedtimer.skiptime == 0:
                small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
                results = hands.process(small_image)
                kindofhands = self.handrecognition(results)
                if kindofhands == 'OK':
                    timemanagement.set_timer()
                elif timemanagement.timer < timemanagement.threshold:
                    timemanagement.count()
                    self.change_state(kindofhands)
                    self.operate()
                else:
                    pass

            #     self.drawing(image, results, kindofhands)

            # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            # cv2.imshow('MediaPipe Hands', image)
            # if cv2.waitKey(5) & 0xFF == 27:
            #     break


    def handrecognition(self):
        pass

    def change_state(self):
        pass

    def operate(self):
        pass

    def drawing(self):
        pass

class main(Templete):
    def handrecognition(self, results):
        if results.multi_hand_landmarks:
            myhands.input(results)
            myhands.offset()
            myhands.adjust()
            myhands.rotate()
            myhands.output()
            kindofhands = myhands.gesturerecognize()
            return kindofhands
        else:
            return 'NoDetected'

    def change_state(self, kindofhands):
        state.change_state(kindofhands)

    def operate(self):
        state.operate()

    def drawing(self, image, results, kindofhands):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.putText(image, kindofhands,
                            (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)
    myhands = hand.Hand()
    state = gestures.Context()
    timemanagement = Time()
    signalacceptedtimer = Time()

    main().run()

    cap.release()
