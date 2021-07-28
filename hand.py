import numpy as np


class Hand():
    def __init__(self):
        self.HANDLIST = ['PAPER', 'SCISSORS', 'STONE']
        self.LEFTHANDPOSITIONS = [
            [0.0, 0.0, 0.36737541618291625, -0.18290894823191042, 0.6377366403428999, -0.48281049801152287, 0.7912562511444323, -0.7641425113127971, 0.9194909414776343, -0.9424030117575998, 0.2408548756285135, -0.9561873761185778, 0.24598376130021463, -1.3515599992670038, 0.23514011115196934, -1.5949397532953848, 0.21797693485828062, -1.8170520416154825, -0.015459012310190978, -0.9705708054966384, -0.08678487501982604, -
             1.412422431802454, -0.13924860206263773, -1.6892486204511776, -0.19584682464018338, -1.920016625111712, -0.22977605724019598, -0.8949040579177211, -0.3422484033497341, -1.294767142900135, -0.39923393548926833, -1.5536842410838971, -0.44553222831829586, -1.7746466119836455, -0.4209672290953173, -0.7415944094710522, -0.603126440451748, -0.9992435367323711, -0.7063336227024328, -1.1672060741622161, -0.7942954290123301, -1.328176969069337],
            [0.0, 0.0, 0.2675504304854559, -0.1158067403562683, 0.4153492476680784, -0.3944032131084789, 0.20897198427065672, -0.5871133469065045, -0.06549042225571913, -0.7406254580738699, 0.2675278302864339, -1.0301610162975514, 0.3793890631197357, -1.4006859279913733, 0.4429550718450191, -1.6412263803758114, 0.4800589266474446, -1.8686696571553412, -0.007541151121975471, -1.0360093282223828, -0.12197423309524277, -
             1.4573339254603372, -0.22134664272475363, -1.752811277004678, -0.31075587724946496, -2.0139459642555186, -0.21949090856585723, -0.912368995693968, -0.30590391033416825, -1.1026678254064246, -0.16496680806158573, -0.8207033323274561, -0.06330697252615089, -0.6061605639472615, -0.39254354135378017, -0.7267847913788045, -0.4535102248228483, -0.9093621395295771, -0.3218405041767766, -0.7271081546192296, -0.21111596578702288, -0.5510031028573358],
            [0.0, 0.0, 0.2798034637274148, -0.20129220354476796, 0.44505851992474815, -0.5269220675160896, 0.321644856449514, -0.8580645501731523, 0.034642472091825444, -0.9650807478414828, 0.22810068902633013, -0.8527997278423987, 0.2556676301290506, -1.1109821282950414, 0.2635491836854518, -0.7999391406959171, 0.25399193691850325, -0.6809812720132892, 0.005575333982035996, -0.8398481703274341, -0.011124324970631372, -1.083301606931175,
             0.05714236908741541, -0.6988437077282074, 0.06290402962466465, -0.6153959721710884, -0.20748257169637344, -0.7687707953249943, -0.23439430809349693, -0.9942709797096089, -0.11887972242043943, -0.6311975786028979, -0.10958164886784101, -0.5196342036965905, -0.4324081006161278, -0.6441390280558005, -0.41575919896464986, -0.8564463191517062, -0.30592325601870546, -0.6227523708774112, -0.29556823379700126, -0.49956109121301695]
        ]
        self.RIGHTHANDPOSITIONS = [
            [0.0, 0.0, -0.4065502436774542, -0.17537035401724466, -0.6873548181913601, -0.5003831313615763, -0.8637532499217431, -0.7953405559455203, -1.0609895590837037, -0.9725676810253951, -0.2795384046384235, -1.0392162152785485, -0.3674369978885755, -1.4443148207866152, -0.3814706235060696, -1.6954927328569245, -0.38050312110381207, -1.9136195327035304, 0.015449838918870903, -1.0683568409493214, 0.06876878637875936, -
             1.5479192106086543, 0.11161859564937024, -1.8541891926504852, 0.1638623705227336, -2.1234671818792763, 0.2659923940681936, -1.0033557687099497, 0.3905206707094844, -1.4457348369447212, 0.47538526123521146, -1.7328892303203567, 0.5551249053326315, -1.9835886884901597, 0.4953009371288086, -0.851706245522274, 0.7094149900972143, -1.1462154616685958, 0.8451121391576757, -1.3361387741790665, 0.9724361887100912, -1.5176846113818971],
            [0.0, 0.0, -0.34594716756151106, -0.11933582036681638, -0.50474206578673, -0.4866495048931125, -0.21304817717718233, -0.6943005948992473, 0.09359751610781997, -0.815639367238733, -0.31632370523793857, -1.219400932606088, -0.4654214093620227, -1.6739100630852664, -0.5437831492691143, -1.9789802501025744, -0.581745322173234, -2.258722459372187, 0.02379790574696322, -1.2395074412265596, 0.12030511555334404, -
             1.723129357080311, 0.19950056316993559, -2.092320072969509, 0.2809589972924909, -2.39753490444815, 0.29173533311038813, -1.0880767149972752, 0.42170282926442215, -1.3849186518500292, 0.25142411133087095, -1.0300720086564448, 0.10450417169053444, -0.7355448478187534, 0.5099355041287194, -0.8424288827662301, 0.5659448328447906, -1.0128028791733887, 0.40599015060566124, -0.7425628921973408, 0.2518602178401019, -0.5196583538589759],
            [0.0, 0.0, -0.29984732629494604, -0.2128856334911129, -0.4748674319094661, -0.5748889494680642, -0.3582607581681472, -0.9125129403223764, -0.08842604297624151, -1.0265704710450905, -0.2121987488686729, -0.9208233201259498, -0.2137975910138804, -1.191349456814182, -0.2670568329442856, -0.8931807093708769, -0.25616067445626295, -0.7625940808910769, 0.009048410749099206, -0.881834140954769, 0.03614447927964157, -
             1.1608077183166425, -0.07280662382913825, -0.7734086208024326, -0.06626311547138722, -0.6596208518399547, 0.2322152202872369, -0.7817396365790164, 0.2691078690704186, -1.040981144635001, 0.108999502915894, -0.6679268378774196, 0.10454609216544122, -0.5342725830162934, 0.46714206223846577, -0.6350620393601069, 0.4578182559750268, -0.8731673018437295, 0.30800500725309865, -0.6401007281111998, 0.2839293718535011, -0.5139236047291029]
        ]

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
        self.handposition = []
        for x, y in zip(self.__xposition, self.__yposition):
            self.handposition.append(x)
            self.handposition.append(y)

    def cosineDistanceMatching(self, reference):
        cosineSimilarity = np.dot(self.handposition, reference) / \
            (np.linalg.norm(self.handposition) * np.linalg.norm(reference))
        distance = 2 * (1 - cosineSimilarity)
        return np.sqrt(distance)

    def recognize(self, results):
        self.scores = []
        if results.multi_handedness[0].classification[0].index == 0:
            for LEFTHANDPOSITION in self.LEFTHANDPOSITIONS:
                self.scores.append(
                    self.cosineDistanceMatching(LEFTHANDPOSITION))
        else:
            for RIGHTHANDPOSITION in self.RIGHTHANDPOSITIONS:
                self.scores.append(
                    self.cosineDistanceMatching(RIGHTHANDPOSITION))

        if min(self.scores) < 0.1:
            return self.HANDLIST[self.scores.index(min(self.scores))]
        else:
            return 'NoDetected'