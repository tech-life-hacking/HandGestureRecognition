import requests

headers = {
    'Authorization': 'cabbd03732853c5c97a38218d0f1757f946153fecc1848f6246439efd3bc1b5a7ab99e54a661419c5646ba987e064072',
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
        requests.post('https://api.switch-bot.com/v1.0/devices/C6EF7910CF12/commands',
                      headers=headers, data=turnon)


class SCISSORS(State):
    def operate(self):
        pass


class STONE(State):
    def operate(self):
        # turn off the light
        requests.post('https://api.switch-bot.com/v1.0/devices/C6EF7910CF12/commands',
                      headers=headers, data=turnoff)


class Context:
    def __init__(self):
        self.nodetected = NoDetected()
        self.paper = PAPER()
        self.scissors = SCISSORS()
        self.stone = STONE()
        self.state = self.nodetected

    def change_state(self, hand):
        if hand == "NoDetected":
            self.state = self.nodetected
        elif hand == "PAPER":
            self.state = self.paper
        elif hand == "SCISSORS":
            self.state = self.scissors
        elif hand == "STONE":
            self.state = self.stone
        else:
            raise ValueError("change_state method must be in {}".format(
                ["nodetected", "paper", "scissors", "stone"]))

    def operate(self):
        self.state.operate()
