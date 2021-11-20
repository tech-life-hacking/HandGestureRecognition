# Hand Gesture Recognition
This repository gives you Hand Gesture Recognition library for RaspberryPi or OpenCV AI Kit.

The detail is [my articles](https://www.techlife-hacking.com/?p=883).

![HandGestureRecognition](https://www.techlife-hacking.com/wp-content/uploads/2021/09/nn-1.gif)

# Devices
## RaspberryPi
RaspberryPi 4 Model B 8GB

OS : Ubuntu Server 21.04.2 LTS

USB Camera

## OpenCV AI Kit
Jetson Nano

OS : Ubuntu 18.04.6 LTS

OpenCV AI Kit OAK-D

# Concepts
At first, MediaPipe infers 21 hand landmarks from images captured with a USB camera.
![handlandmarks](https://www.techlife-hacking.com/wp-content/uploads/2021/09/hand_landmarks.png)

[MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)

And then, the 21 hand landmarks are classified to hand gestures by multilayered neural network. You can train the model and add your favorite hand gestures.
Please check at HandGestureRecognition.ipynb.

# Setup
## RaspberryPi
### Install build dependencies
```
sudo apt install -y cmake
sudo apt install -y protobuf-compiler
pip install cython
pip install numpy == 1.19.5
pip install pillow
```

### Install MediaPipe
```
git clone --recursive https://github.com/tech-life-hacking/HandGestureRecognition.git
cd HandGestureRecognition
pip install mediapipe-0.8-cp39-cp39-linux_aarch64.whl
```

### Install Tensorflow
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

## OpenCV AI Kit
### Install build dependencies
```
# Disable ZRAM:
sudo systemctl disable nvzramconfig
# Create 4GB swap file
sudo fallocate -l 4G /mnt/4GB.swap
sudo chmod 600 /mnt/4GB.swap
sudo mkswap /mnt/4GB.swap

sudo -H apt install -y python3-pip

#Download and install the dependency package
sudo wget -qO- http://docs.luxonis.com/_static/install_dependencies.sh | bash

#Clone github repository
git clone https://github.com/luxonis/depthai.git
cd depthai

echo "export OPENBLAS_CORETYPE=ARMV8" >> ~/.bashrc
python3 install_requirements.py
```
### Install Tensorflow
```
# dependency
sudo apt-get update
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran

# update pip
sudo apt-get install python3-pip
sudo pip3 install -U pip testresources setuptools==49.6.0

sudo pip3 install -U --no-deps numpy==1.19.4 future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 protobuf pybind11 cython pkgconfig

# tensorflow
sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v46 tensorflow
```

# Usage
After cloning this repository, excute example.

```
git clone --recursive https://github.com/tech-life-hacking/HandGestureRecognition.git
cd HandGestureRecognition
python example.py
```
Usage example

```python
import cv2
import scripts.hand as hand
import scripts.video as video

if __name__ == "__main__":

    # class of gestures for OAK
    class_names = ['LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    # class of gestures for Raspberry Pi
    # class_names = ['LEFTFINGER', 'LEFTOK', 'LEFTPAPER', 'LEFTSCISSORS', 'LEFTSTONE',
    #                 'RIGHTFINGER', 'RIGHTOK', 'RIGHTPAPER', 'RIGHTSCISSORS', 'RIGHTSTONE']

    # model path for OpenCV AI Kit
    model_path = "model/hands_OAK.tflite"

    # model path for Raspberry Pi
    # model_path = "model/hands.tflite"

    # For HandGestureRecognition for OpenCV AI Kit
    myhands = hand.Hand(hand.OAKCamera(class_names, model_path))
    videocap = video.VideoCap(video.OAKCamera())

    # For HandGestureRecognition for Raspberry Pi
    # myhands = hand.Hand(hand.RGBCamera(class_names, model_path))
    # videocap = video.VideoCap(video.RGBCamera())

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

```

# license
MIT License