from seven import Seven
from matrix import Matrix
from keypad import Keypad
from traffic import TrafficLights

from time import sleep


if __name__ == "__main__":
    seven = Seven()
    matrix = Matrix()
    traffic = TrafficLights()
    keypad = Keypad(seven.add)

    while True:
        sleep(1)