import cv2

class VideoCap():
    def __init__(self, devices):
        self.devices = devices

    def capture(self):
        return self.devices.capture()

    def show(self, frame):
        self.devices.show(frame)

    def exit(self):
        self.devices.exit()

class Devices:
    def capture(self):
        raise NotImplementedError()

    def show(self, frame):
        raise NotImplementedError()

class OAKCamera(Devices):
    def __init__(self):
        import os
        import sys
        sys.path.append(os.path.join(os.path.dirname(__file__), './../depthai_hand_tracker'))
        from HandTrackerRenderer import HandTrackerRenderer
        from HandTrackerEdge import HandTracker
        self.tracker = HandTracker(stats=True)
        self.renderer = HandTrackerRenderer(self.tracker)
        self.hands = []

    def capture(self):
        self.frame, self.hands, self.bag = self.tracker.next_frame()
        return self.frame, self.hands

    def show(self, frame):
        self.frame = self.renderer.draw(self.frame, self.hands, self.bag)
        cv2.imshow('MediaPipe Hands', self.frame)

    def exit(self):
        self.tracker.exit()
        self.renderer.exit()

class RGBCamera(Devices):
    def __init__(self):
        import mediapipe as mp
        # For webcam input
        self.cap = cv2.VideoCapture(0)

        # MediaPipe Library
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.9,
            min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

    def capture(self):
        # Capture images
        success, self.frame = self.cap.read()

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        self.frame = cv2.cvtColor(cv2.flip(self.frame, 1), cv2.COLOR_BGR2RGB)

        # Resize the image size
        small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)

        # hand images to handlandmarks
        self.results = self.hands.process(small_frame)
        return self.frame, self.results

    def show(self, frame):
        # Draw the hand annotations on the image.
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    self.frame, hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style())
        cv2.imshow('MediaPipe Hands', self.frame)

    def exit(self):
        self.cap.release()
        cv2.destroyAllWindows()