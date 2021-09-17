# HandGestureRecognition
Hand Gesture Recognition using MediaPipe

![demo](https://www.techlife-hacking.com/wp-content/uploads/2021/09/nn-1.gif)
# Setup

## Install build dependencies
```
sudo apt install -y cmake
sudo apt install -y protobuf-compiler
pip install cython
pip install numpy == 1.19.5
pip install pillow
```

## Get sources
```
git clone https://github.com/tech-life-hacking/HandGestureRecognition.git
cd HandGestureRecognition
```
## Install mediapipe
```
pip install mediapipe-0.8-cp39-cp39-linux_aarch64.whl
```

## Install tensorflow
Prebuilt binary of Tensorflow Lite for RaspberryPi is prepared by [PINTO0309](https://github.com/PINTO0309/Tensorflow-bin).

```
sudo apt-get -y install libhdf5-dev curl python3-protobuf python3-termcolor python3-yaml python3-pydot python3-pyasn1 python3-pyasn1-modules python3-rsa python3-markdown python3-cachetools python3-future python3-dill python3-tqdm python3-pil python3-wheel python3-setuptools python3-matplotlib python3-h5py python3-scipy python3-grpcio python3-requests-oauthlib python3-werkzeug python3-wrapt build-dep h5py grpc

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

# license
MIT License