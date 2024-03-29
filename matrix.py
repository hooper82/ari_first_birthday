from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import show_message, text

from random import choice


IMAGES = {
    'solid_heart' : [[0x00, 0x1c, 0x3e, 0x7e, 0xfc, 0x7e, 0x3e, 0x1c]],
    'creature1'   : [[0x86, 0x59, 0xf4, 0x2c, 0x2c, 0xf4, 0x59, 0x86]],
    'bunny'       : [[0x40, 0xe3, 0xd6, 0x78, 0x78, 0xd6, 0xe3, 0x40]],
    'octopus'     : [[0x8c, 0xde, 0x77, 0xff, 0xff, 0x77, 0xde, 0x8c]],
    'rocket'      : [[0x60, 0x38, 0x3e, 0xff, 0x3e, 0x38, 0x60, 0x00]],
    'smiley'      : [[0x3c, 0x42, 0xad, 0xa1, 0xad, 0x91, 0x42, 0x3c]],
    'snowflake1'  : [[0x00, 0x10, 0x54, 0x38, 0xef, 0x38, 0x54, 0x10]],
    'snowflake2'  : [[0x10, 0x38, 0x54, 0xee, 0x54, 0x38, 0x10, 0x00]],
    'pattern1'    : [[0x66, 0xc3, 0x99, 0x24, 0x24, 0x99, 0xc3, 0x66]],
    'pattern2'    : [[0x7e, 0xdb, 0x99, 0xe7, 0xe7, 0x99, 0xdb, 0x7e]],
    'pattern3'    : [[0xe7, 0xa5, 0xdb, 0x24, 0x24, 0xdb, 0xa5, 0xe7]],
    'man'         : [[0x00, 0x00, 0x38, 0xfa, 0xfa, 0x38, 0x00, 0x00]],
    'empty_heart' : [[0x06, 0x19, 0x61, 0x82, 0x82, 0x61, 0x19, 0x06]],
    'cross'       : [[0x81, 0x42, 0x24, 0x18, 0x18, 0x24, 0x42, 0x81]],
    'diamond'     : [[0x18, 0x24, 0x42, 0x81, 0x81, 0x42, 0x24, 0x18]],
}


class Matrix(object):
    def __init__(self):
        print("Initializing Matrix...", end='')
        self._serial = spi(port=0, device=0, gpio=noop())
        self._device = max7219(self._serial, rotate=1)
        self._current_image_name = None
        print("...Done!")
        self.happy_birthday()
        self.change_image()

    def happy_birthday(self):
        print('Saying Happy Birthday...', end='')
        msg = "Happy Birthday Ari!"
        show_message(self._device, msg, fill="white", scroll_delay=0.05)
        print('..Done!')

    def change_image(self):
        print('changing image')
        image_names = list(IMAGES.keys())
        if self._current_image_name in image_names:
            image_names.remove(self._current_image_name)

        self._current_image_name = choice(image_names)
        self._draw_image(self._current_image_name)

    def _draw_image(self, image_name):
        image = IMAGES[image_name]
        with canvas(self._device) as draw:
            text(draw, (0, 0), "\0", fill="white", font=image)
