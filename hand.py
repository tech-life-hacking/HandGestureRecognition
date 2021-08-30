import numpy as np
import csv
import tensorflow as tf


class Hand():
    def __init__(self):
        self.interprefer = tf.lite.Interpreter(
            model_path="hands.tflite")
        self.interprefer.allocate_tensors()
        self.input_details = self.interprefer.get_input_details()
        self.output_details = self.interprefer.get_output_details()
        self.class_names = ['LEFTFINGER', 'LEFTOK', 'LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE',
                            'RIGHTFINGER', 'RIGHTOK', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    def input(self, results):
        if results.hand_rects:
            self.__rotation = results.hand_rects[0].rotation
        if results.palm_detections:
            self.__width = results.palm_detections[0].location_data.relative_bounding_box.width
            self.__height = results.palm_detections[0].location_data.relative_bounding_box.height
        self.__xposition = np.array([])
        self.__yposition = np.array([])
        if results.multi_hand_landmarks:
            for handposition in results.multi_hand_landmarks[0].landmark:
                self.__xposition = np.concatenate(
                    [self.__xposition, np.array([handposition.x])])
                self.__yposition = np.concatenate(
                    [self.__yposition, np.array([handposition.y])])

    def offset(self):
        self.__xposition = self.__xposition - self.__xposition[0]
        self.__yposition = self.__yposition - self.__yposition[0]

    def adjust(self):
        self.__xposition = self.__xposition / self.__width
        self.__yposition = self.__yposition / self.__height

    def rotate(self):
        xs0 = []
        ys0 = []
        for x, y in zip(self.__xposition, self.__yposition):
            X = x * np.cos(self.__rotation) + y * np.sin(self.__rotation)
            Y = - x * np.sin(self.__rotation) + y * np.cos(self.__rotation)
            xs0.append(X)
            ys0.append(Y)
        self.__xposition = np.array(xs0)
        self.__yposition = np.array(ys0)

    def output(self):
        self.handposition = np.concatenate(
            (self.__xposition, self.__yposition))
        self.handposition = np.array(
            self.handposition, dtype='float32').reshape(1, 42, 1)

    def gesturerecognize(self):
        self.interprefer.set_tensor(
            self.input_details[0]['index'], self.handposition)
        self.interprefer.invoke()
        self.output_data = self.interprefer.get_tensor(
            self.output_details[0]['index'])
        kindofhands = self.class_names[np.argmax(self.output_data)]
        kindofhands = kindofhands.replace('LEFT', '').replace('RIGHT', '')
        if np.max(self.output_data) < 0.95:
            kindofhands = 'NoDetected'
        return kindofhands
