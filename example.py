import hand
import cv2
import mediapipe as mp
# For recording
# import csv

if __name__ == "__main__":

    # class of gestures
    class_names = ['LEFTFINGER', 'LEFTOK', 'LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE',
                    'RIGHTFINGER', 'RIGHTOK', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']
    # model path
    model_path = "model/hands.tflite"

    # For webcam input
    cap = cv2.VideoCapture(0)

    # MediaPipe Library
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.9,
        min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    # For recording
    # f = open('handlandmarks.csv', 'w')
    # writer = csv.writer(f)

    # For HandGestureRecognition
    myhands = hand.Hand(class_names, model_path)

    while cap.isOpened():

        # Capture images
        success, image = cap.read()

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # Resize the image size
        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)

        # hand images to handlandmarks
        results = hands.process(small_image)

        # Recognize gestures
        kind_of_hands = myhands.run(results)

        # For recording
        # record handlandmarks
        # myhands.record(results, writer)

        # For RaspberryPi
        # print a kind of hands
        print(kind_of_hands)

        # For PC
        # Draw the hand annotations on the image.
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # if results.multi_hand_landmarks:
        #     for hand_landmarks in results.multi_hand_landmarks:
        #         mp_drawing.draw_landmarks(
        #             image, hand_landmarks,
        #             mp_hands.HAND_CONNECTIONS,
        #             mp_drawing_styles.get_default_hand_landmarks_style(),
        #             mp_drawing_styles.get_default_hand_connections_style())
        #         cv2.putText(image, kind_of_hands,
        #             (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
        # cv2.imshow('MediaPipe Hands', image)
        # if cv2.waitKey(5) & 0xFF == 27:
        #     break

    cap.release()
    # For recording
    # f.close()