import numpy as np
import tensorflow as tf
import csv

class Hand():
    def __init__(self, devices):
        self.devices = devices

    def input(self, hands):
        self.devices.input(hands)

    def offset(self):
        self.devices.offset()

    def adjust(self):
        self.devices.adjust()

    def rotate(self):
        self.devices.rotate()

    def output(self):
        self.devices.output()

    def record(self):
        self.devices.record()

    def recognize(self):
        return self.devices.recognize()

    def run(self, hands):
        if hands:
            self.input(hands)
            self.offset()
            self.adjust()
            self.rotate()
            self.output()
            self.record()
            return self.recognize()
        else:
            return 'NoDetected'

class Devices:
    def input(self, hands):
        raise NotImplementedError()

class OAKCamera(Devices):
    def __init__(self, class_names, model_path):
        f = open('handlandmarks.csv', 'w')
        self.writer = csv.writer(f)
        self.interprefer = tf.lite.Interpreter(model_path=model_path)
        self.interprefer.allocate_tensors()
        self.input_details = self.interprefer.get_input_details()
        self.output_details = self.interprefer.get_output_details()
        self.class_names = class_names

    def input(self, hands):
        for hand in hands:
            self.__rotation = hand.rotation
            self.__width = hand.rect_w_a
            self.__height = hand.rect_h_a
            self.__xposition = hand.landmarks[:,0]
            self.__yposition = hand.landmarks[:,1]

    def offset(self):
        self.__xposition = self.__xposition - self.__xposition[0]
        self.__yposition = self.__yposition - self.__yposition[0]

    def adjust(self):
        self.__xposition = self.__xposition / self.__width
        self.__yposition = self.__yposition / self.__height

    def rotate(self):
        R = np.array([[np.cos(self.__rotation), np.sin(self.__rotation)],
                      [-np.sin(self.__rotation),  np.cos(self.__rotation)]])
        self.__xposition, self.__yposition = np.dot(R, (self.__xposition, self.__yposition))

    def output(self):
        self.handposition = np.concatenate(
            (self.__xposition, self.__yposition))
        self.handposition = np.array(
            self.handposition, dtype='float32').reshape(1, 42, 1)

    def record(self):
        tmp = np.array(self.handposition).reshape(42)
        self.writer.writerow(tmp)

    def recognize(self):
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

class RGBCamera(Devices):
    def __init__(self, class_names, model_path):
        f = open('handlandmarks.csv', 'w')
        self.writer = csv.writer(f)
        self.interprefer = tf.lite.Interpreter(model_path=model_path)
        self.interprefer.allocate_tensors()
        self.input_details = self.interprefer.get_input_details()
        self.output_details = self.interprefer.get_output_details()
        self.class_names = class_names

    def input(self, hands):
        if hands.hand_rects:
            self.__rotation = hands.hand_rects[0].rotation
        if hands.palm_detections:
            self.__width = hands.palm_detections[0].location_data.relative_bounding_box.width
            self.__height = hands.palm_detections[0].location_data.relative_bounding_box.height
        self.__xposition = np.array([])
        self.__yposition = np.array([])
        if hands.multi_hand_landmarks:
            for handposition in hands.multi_hand_landmarks[0].landmark:
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
        R = np.array([[np.cos(self.__rotation), np.sin(self.__rotation)],
                      [-np.sin(self.__rotation),  np.cos(self.__rotation)]])
        self.__xposition, self.__yposition = np.dot(R, (self.__xposition, self.__yposition))

    def output(self):
        self.handposition = np.concatenate(
            (self.__xposition, self.__yposition))
        self.handposition = np.array(
            self.handposition, dtype='float32').reshape(1, 42, 1)

    def record(self):
        tmp = np.array(self.handposition).reshape(42)
        self.writer.writerow(tmp)

    def recognize(self):
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