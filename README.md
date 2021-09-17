# Hand Gesture Recognition
This repository gives you Hand Gesture Recognition library for RaspberryPi.

The detail is [my articles](https://www.techlife-hacking.com/?p=883).

![HandGestureRecognition](https://www.techlife-hacking.com/wp-content/uploads/2021/09/nn-1.gif)

# Devices
RaspberryPi 4 Model B 8GB

Ubuntu Server 21.04.2 LTS

# Concepts
At first, MediaPipe infers 21 hand landmarks from images captured with a USB camera.
![handlandmarks](https://www.techlife-hacking.com/wp-content/uploads/2021/09/hand_landmarks.png)

[MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)

And then, the 21 hand landmarks are classified to hand gestures by multilayered neural network. You can train the model and add your favorite hand gestures.
Please check at HandGestureRecognition.ipynb.

# Setup

## Install build dependencies
```
sudo apt install -y cmake
sudo apt install -y protobuf-compiler
pip install cython
pip install numpy == 1.19.5
pip install pillow
```

## Install MediaPipe
```
git clone https://github.com/tech-life-hacking/HandGestureRecognition.git
cd HandGestureRecognition
pip install mediapipe-0.8-cp39-cp39-linux_aarch64.whl
```

## Install Tensorflow
Prebuilt binary of Tensorflow Lite for RaspberryPi is prepared by [PINTO0309](https://github.com/PINTO0309/Tensorflow-bin).

```
sudo apt-get -y install libhdf5-dev curl python3-protobuf
 python3-termcolor python3-yaml python3-pydot python3-pyasn1 
 python3-pyasn1-modules python3-rsa python3-markdown python3-cachetools 
 python3-future python3-dill python3-tqdm python3-pil python3-wheel python3-setuptools 
 python3-matplotlib python3-h5py python3-scipy python3-grpcio python3-requests-oauthlib 
 python3-werkzeug python3-wrapt build-dep h5py grpc

git clone https://github.com/PINTO0309/Tensorflow-bin.git
cd Tensorflow-bin
sudo bash tensorflow-2.6.0-cp39-none-linux_aarch64_numpy1195_download.sh
pip install tensorflow-2.6.0-cp39-none-linux_aarch64.whl
```

# Usage
After cloning this repository, excute example.

```
python example.py
```
Usage example

```python
import hand
import cv2
import mediapipe as mp

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

    # For RaspberryPi
    # print a kind of hands
    print(kind_of_hands)

cap.release()
```

# license
MIT License