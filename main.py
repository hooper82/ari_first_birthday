from seven import Seven
from matrix import Matrix
from keypad import Keypad
from traffic import TrafficLights
from buttons import ButtonHandler

from time import sleep
from signal import pause


if __name__ == "__main__":
    seven = Seven()
    traffic = TrafficLights()
    matrix = Matrix()
    keypad = Keypad(seven.add)
    buttons = ButtonHandler(matrix.change_image, traffic.cycle)

    pause()
