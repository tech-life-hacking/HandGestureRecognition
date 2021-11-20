import hand
import cv2
import video

if __name__ == "__main__":

    # class of gestures
    class_names = ['LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    # class_names = ['LEFTFINGER', 'LEFTOK', 'LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE',
    #                 'RIGHTFINGER', 'RIGHTOK', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    # model path
    model_path = "model/hands.tflite"

    # For HandGestureRecognition
    myhands = hand.Hand(hand.OAKCamera(class_names, model_path))
    videocap = video.VideoCap(video.OAKCamera())

    while True:

        frame, hands = videocap.capture()

        try:
            # Recognize gestures
            kind_of_hands = myhands.run(hands)
            cv2.putText(frame, kind_of_hands,
                        (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
        except IndexError:
            pass

        videocap.show(frame)
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):
            break

    videocap.exit()