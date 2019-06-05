from seven import Seven
from matrix import Matrix
from keypad import Keypad
from traffic import TrafficLights

from time import sleep


if __name__ == "__main__":
    seven = Seven()
    traffic = TrafficLights()
    matrix = Matrix()
    keypad = Keypad(seven.add)

    while True:
        traffic.cycle()
        sleep(1)