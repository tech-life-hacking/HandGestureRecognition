import numpy as np
import csv
import tensorflow as tf


class Hand():
    def __init__(self):
        # self.HANDLIST = ['FINGER', 'OK', 'PAPER', 'SCISSORS', 'STONE']
        # self.LEFTHANDPOSITIONS = [
        #     [0.0, 0.0, 0.36737541618291625, -0.18290894823191042, 0.6377366403428999, -0.48281049801152287, 0.7912562511444323, -0.7641425113127971, 0.9194909414776343, -0.9424030117575998, 0.2408548756285135, -0.9561873761185778, 0.24598376130021463, -1.3515599992670038, 0.23514011115196934, -1.5949397532953848, 0.21797693485828062, -1.8170520416154825, -0.015459012310190978, -0.9705708054966384, -0.08678487501982604, -
        #      1.412422431802454, -0.13924860206263773, -1.6892486204511776, -0.19584682464018338, -1.920016625111712, -0.22977605724019598, -0.8949040579177211, -0.3422484033497341, -1.294767142900135, -0.39923393548926833, -1.5536842410838971, -0.44553222831829586, -1.7746466119836455, -0.4209672290953173, -0.7415944094710522, -0.603126440451748, -0.9992435367323711, -0.7063336227024328, -1.1672060741622161, -0.7942954290123301, -1.328176969069337],
        #     [0.0, 0.0, 0.2675504304854559, -0.1158067403562683, 0.4153492476680784, -0.3944032131084789, 0.20897198427065672, -0.5871133469065045, -0.06549042225571913, -0.7406254580738699, 0.2675278302864339, -1.0301610162975514, 0.3793890631197357, -1.4006859279913733, 0.4429550718450191, -1.6412263803758114, 0.4800589266474446, -1.8686696571553412, -0.007541151121975471, -1.0360093282223828, -0.12197423309524277, -
        #      1.4573339254603372, -0.22134664272475363, -1.752811277004678, -0.31075587724946496, -2.0139459642555186, -0.21949090856585723, -0.912368995693968, -0.30590391033416825, -1.1026678254064246, -0.16496680806158573, -0.8207033323274561, -0.06330697252615089, -0.6061605639472615, -0.39254354135378017, -0.7267847913788045, -0.4535102248228483, -0.9093621395295771, -0.3218405041767766, -0.7271081546192296, -0.21111596578702288, -0.5510031028573358],
        #     [0.0, 0.0, 0.2798034637274148, -0.20129220354476796, 0.44505851992474815, -0.5269220675160896, 0.321644856449514, -0.8580645501731523, 0.034642472091825444, -0.9650807478414828, 0.22810068902633013, -0.8527997278423987, 0.2556676301290506, -1.1109821282950414, 0.2635491836854518, -0.7999391406959171, 0.25399193691850325, -0.6809812720132892, 0.005575333982035996, -0.8398481703274341, -0.011124324970631372, -1.083301606931175,
        #      0.05714236908741541, -0.6988437077282074, 0.06290402962466465, -0.6153959721710884, -0.20748257169637344, -0.7687707953249943, -0.23439430809349693, -0.9942709797096089, -0.11887972242043943, -0.6311975786028979, -0.10958164886784101, -0.5196342036965905, -0.4324081006161278, -0.6441390280558005, -0.41575919896464986, -0.8564463191517062, -0.30592325601870546, -0.6227523708774112, -0.29556823379700126, -0.49956109121301695]
        # ]
        # self.RIGHTHANDPOSITIONS = [
        #     [0, -0.30364503, -0.50316195, -0.4136144,  -0.18213823, -0.24833239, -0.24052994, -0.18767046, -0.11826258,  0.00548296,  0.0030643,  -0.0934442, -0.15852555,  0.22908349,  0.20802173,  0.08287175,  0.00694382,  0.43787863,  0.4169985,  0.29126317,  0.21066545,  0,         -0.12546063, -0.43849027,
        #      -0.6725374,  -0.75350828, -0.99563787, -1.44149605, -1.71199974, -1.9498062, -0.93181082, -1.18743718, -0.8390069,  -0.58478785, -0.81119974, -0.94357239, -0.61874117, -0.42129559, -0.64730769, -0.77197218, -0.5606491,  -0.42704337],
        #     [0, -0.35729372, -0.61877781, -0.81937621, -0.85528008, -0.18017512, -0.40541736, -0.63838555, -0.78819714,  0.00463914, -0.05866422, -0.16229481, -0.27067311,  0.18866174,  0.21307012,  0.21894709,  0.19175749,  0.36656215,  0.51940752,  0.60795857,  0.66100422,  0,         -0.06119439, -0.24847864,
        #      -0.45135933, -0.66721456, -0.71342024, -0.98987984, -0.97511441, -0.86376891, -0.85812527, -1.31652746, -1.64992074, -1.91854415, -0.88115809, -1.35007253, -1.68624432, -1.95777387, -0.81005683, -1.18046424, -1.4298637,  -1.64683903],
        #     [0, -0.33762172, -0.57709453, -0.72751395, -0.90688905, -0.2504477, -0.31500387, -0.33260753, -0.33591219, -0.00776457, 0.03670644, 0.0740793, 0.11728305,  0.2020647,   0.3023084,   0.37537799,  0.43942141,  0.39169187, 0.5623902, 0.6649898,   0.75245408,  0, -0.11463453, -0.34836233,
        #      -0.55928401, -0.6943019, -0.83793113, -1.17593276, -1.38314772, -1.57641771, - 0.8658976, -1.27571144, -1.53202178, -1.75970667, -0.80806397, -1.17844868, -1.42301011, -1.64119776, -0.67533406, -0.93888215, -1.11194388, -1.27672789],
        #     [0, -0.30353763, -0.44348635, -0.20374256, 0.048129, -0.2561267, -0.36048314, -0.41739498, -0.44010472, 0.02882524, 0.16636072, 0.27306616, 0.38657897,  0.24502631, 0.3440515, 0.16975029, 0.04121588, 0.42155605, 0.45708156, 0.30301791, 0.17078381,  0, -0.15461168, -0.47363237,
        #      -0.63481177, -0.71876374, -1.05570308, -1.46222662, -1.72058763, -1.9527538, -1.04733937, -1.47560776, -1.76976815, -2.00491401, -0.90174553, -1.10487095, -0.81467815, -0.57695921, -0.69498091, -0.82524302, -0.61924549, -0.44497842],
        #     [0, -0.30087134, -0.47781306, -0.36402681, -0.0859803, -0.20819545, -0.1916385, -0.25994651, -0.25432158, 0.00794581, 0.04119504, -0.07028176, -0.04895059, 0.22389706, 0.26491464, 0.10545027, 0.11699408, 0.453208, 0.44884113, 0.29889874, 0.28666465,  0, -0.23734573, -0.60225024,
        #      -0.94764222, -1.00701176, -0.90619689, -1.19256152, -0.89105143, -0.78822157, -0.85692739, -1.14937228, -0.77134694, -0.68963559, -0.75521513, -1.02649163, -0.6669053, -0.563528, -0.61202025, -0.85924619, -0.62124359, -0.51044383]
        # ]
        self.f = open("handlandmarks.csv", "w")
        self.writer = csv.writer(self.f)
        # self.__xwristlist = np.empty((1, 16))
        # self.__ywristlist = np.empty((1, 16))
        self.interprefer = tf.lite.Interpreter(
            model_path="hands.tflite")
        self.interprefer.allocate_tensors()
        self.input_details = self.interprefer.get_input_details()
        self.output_details = self.interprefer.get_output_details()
        self.class_names = ['LEFTFINGER', 'LEFTOK', 'LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE',
                            'RIGHTFINGER', 'RIGHTOK', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']
        # self.class_names = ['CIRCLE', 'NONE']

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
            # self.__xwristlist = np.append(
            #     self.__xwristlist, self.__xposition[0])
            # self.__xwristlist = np.delete(self.__xwristlist, 0, 0)
            # self.__ywristlist = np.append(
            #     self.__ywristlist, self.__yposition[0])
            # self.__ywristlist = np.delete(self.__ywristlist, 0, 0)
            # self.wristlist = np.vstack([self.__xwristlist, self.__ywristlist])
            # self.wristlist = np.array(
            #     self.wristlist, dtype='float32').reshape(1, 2, 16)

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
        # kindofhands = np.argmax(self.output_data)
        kindofhands = kindofhands.replace('LEFT', '').replace('RIGHT', '')
        if np.max(self.output_data) < 0.95:
            kindofhands = 'NoDetected'
        return kindofhands

    def motionrecognize(self):
        self.interprefer.set_tensor(
            self.input_details[0]['index'], self.wristlist)
        self.interprefer.invoke()
        self.output_data = self.interprefer.get_tensor(
            self.output_details[0]['index'])
        kindofhands = self.class_names[np.argmax(self.output_data)]
        # kindofhands = kindofhands.replace('LEFT', '').replace('RIGHT', '')
        # if np.max(self.output_data) < 0.9:
        #     kindofhands = 'NoDetected'
        return kindofhands

    def record(self, kindofhands):
        tmp = np.array(self.handposition).reshape(42)
        tmp = np.append(tmp, int(kindofhands))
        self.writer.writerow(tmp)

    def cosineDistanceMatching(self, reference):
        cosineSimilarity = np.dot(self.handposition, reference) / \
            (np.linalg.norm(self.handposition) * np.linalg.norm(reference))
        distance = 2 * (1 - cosineSimilarity)
        return np.sqrt(distance)

    def recognize0(self, results):
        self.scores = []
        self.handposition = np.array(self.handposition).reshape(42)
        if results.multi_handedness[0].classification[0].index == 0:
            for LEFTHANDPOSITION in self.LEFTHANDPOSITIONS:
                self.scores.append(
                    self.cosineDistanceMatching(LEFTHANDPOSITION))
        else:
            for RIGHTHANDPOSITION in self.RIGHTHANDPOSITIONS:
                self.scores.append(
                    self.cosineDistanceMatching(RIGHTHANDPOSITION))

        if min(self.scores) < 0.1:
            # return self.HANDLIST[self.scores.index(min(self.scores))]
            return self.scores.index(min(self.scores))
        else:
            return 5
