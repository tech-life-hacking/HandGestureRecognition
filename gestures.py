import requests
import socket

headers = {
    'Authorization': '',
    'Content-Type': 'application/json',
}

turnon = '{"command": "turnOn"}'
turnoff = '{"command": "turnOff"}'


class State():
    def operate(self):
        raise NotImplementedError("operate is abstractmethod")


class NoDetected(State):
    def operate(self):
        pass


class PAPER(State):
    def operate(self):
        # turn on the light
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(b'PAPER', ('192.168.11.15', 50010))


class OK(State):
    def operate(self):
        pass


class FINGER(State):
    def operate(self):
        pass


class STONE(State):
    def operate(self):
        # turn off the light
        # requests.post(
        #     'https://maker.ifttt.com/trigger/roomba/with/key/7YWtJuaW7ZLXpa6Wnc6R4zSUalOCw1UHeFkLC7hpbh')
        pass


class Context:
    def __init__(self):
        self.nodetected = NoDetected()
        self.paper = PAPER()
        self.ok = OK()
        self.finger = FINGER()
        self.stone = STONE()
        self.state = self.nodetected

    def change_state(self, hand):
        if hand == "NoDetected":
            self.state = self.nodetected
        elif hand == "PAPER":
            self.state = self.paper
        elif hand == "OK":
            self.state = self.ok
        elif hand == "FINGER":
            self.state = self.finger
        elif hand == "STONE":
            self.state = self.stone
        else:
            # raise ValueError("change_state method must be in {}".format(
            #     ["nodetected", "paper", "scissors", "stone"]))
            pass

    def operate(self):
        self.state.operate()
