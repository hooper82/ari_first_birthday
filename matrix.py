from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import show_message, text


IMAGE_1 = [
    [0x81, 0x42, 0x24, 0x18, 0x18, 0x24, 0x42, 0x81]
]
IMAGE_2 = [
    [0x18, 0x24, 0x42, 0x81, 0x81, 0x42, 0x24, 0x18]
]


class Matrix(object):
    def __init__(self):
        print("Initializing Matrix...", end='')
        self._serial = spi(port=0, device=0, gpio=noop())
        self._device = max7219(self._serial)
        self._current_image = None
        print("...Done!")
        self.happy_birthday()

    def happy_birthday(self):
        print('saying hello')
        msg = "Happy Birthday Ari!"
        show_message(self._device, msg, fill="white", scroll_delay=0.05)
        self.change_image()

    def change_image(self):
        print('changing image')
        if self._current_image is None:
            self._current_image = IMAGE_1
        elif self._current_image == IMAGE_1:
            self._current_image = IMAGE_2
        else:
            self._current_image = IMAGE_1

        self._draw_image(self._current_image)

    def _draw_image(self, image):
        with canvas(self._device) as draw:
            text(draw, (0, 0), "\0", fill="white", font=image)

        if digit in ['*', '#']:
            self._device.text = ''
        else:
            self._device.text += digit
