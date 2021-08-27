import hand
import gestures
import cv2
import mediapipe as mp
import numpy as np
import time


class Templete():
    def run(self):
        j = 0
        t = 0
        while cap.isOpened():
            success, image = cap.read()
            for i in range(5):
                success2, image2 = cap.read()

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            j += 1
            if j % 5 == 0:
                kindofhands = self.handrecognition(image)
                if kindofhands == 'SCISSORS':
                    t = 30
                elif t > 0:
                    t -= 1
                    self.change_state(kindofhands)
                    self.operate()
                    self.sleep(kindofhands)
                else:
                    pass

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            cv2.imshow('MediaPipe Hands', image)
            # out.write(image)
            if cv2.waitKey(5) & 0xFF == 27:
                break

    def handrecognition(self, image):
        pass

    def change_state(self, kindofhands):
        pass

    def operate(self):
        pass

    def sleep(self, kindofhands):
        pass


class main(Templete):
    def handrecognition(self, image):
        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        results = hands.process(small_image)

        # Draw the hand annotations on the image.
        if results.multi_hand_landmarks:
            myhands.input(results)
            myhands.offset()
            myhands.adjust()
            myhands.rotate()
            myhands.output()
            kindofhands = myhands.gesturerecognize()
            cv2.putText(image, kindofhands,
                            (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
            for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            return kindofhands
        else:
            return 'NoDetected'

    def change_state(self, kindofhands):
        state.change_state(kindofhands)

    def operate(self):
        state.operate()

    def sleep(self, kindofhands):
        if kindofhands != 'NoDetected':
            time.sleep(5)


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
    # fps = int(cap.get(cv2.CAP_PROP_FPS))
    # w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('output.avi', fourcc, 20, (w, h))

    main().run()

    cap.release()
