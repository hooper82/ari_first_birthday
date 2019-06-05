from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import sevensegment


class Seven(object):
    def __init__(self):
        self._serial = spi(port=1, device=0, gpio=noop())
        self._max = max7219(self._serial)
        self._device = sevensegment(self._max)

    def add(self, digit):
        print(digit)
        if digit in ['*', '#']:
            self._device.text = ''
        else:
            self._device.text += digit
