import cv2
import scripts.hand as hand
import scripts.video as video

if __name__ == "__main__":

    # class of gestures
    class_names = ['LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    # class_names = ['LEFTFINGER', 'LEFTOK', 'LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE',
    #                 'RIGHTFINGER', 'RIGHTOK', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    # model path
    model_path = "model/hands_OAK.tflite"

    # For HandGestureRecognition
    myhands = hand.Hand(hand.OAKCamera(class_names, model_path))
    videocap = video.VideoCap(video.OAKCamera())
    frame_size = videocap.get_cameraframesize()

    while True:

        frame, hands = videocap.capture()

        try:
            # Recognize gestures
            myhands.run(hands)
            kind_of_hands = myhands.get_gestures()
            wrist = myhands.get_wrist()
            frame_center = myhands.get_frame_center()
            cv2.putText(frame, kind_of_hands,
                        (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
        except:
            pass

        videocap.show(frame)
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):
            break

    videocap.exit()