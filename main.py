from seven import Seven
from matrix import Matrix
from keypad import Keypad


if __name__ == "__main__":
    seven = Seven()
    matrix = Matrix()
    keypad = Keypad(seven.add)

    sleep(30)