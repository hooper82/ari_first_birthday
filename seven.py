from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import sevensegment


class Seven(object):
    def __init__(self):
        print("Initializing Seven...", end='')
        self._serial = spi(port=1, device=0, gpio=noop())
        self._max = max7219(self._serial)
        self._device = sevensegment(self._max)
        self._buffer = ''
        print("...Done!")

    def add(self, digit):
        print(digit)
        if digit in ['*', '#']:
            self._buffer = ''
        else:
            self._buffer = '{}{}'.format(digit, self._buffer)
            if len(self._buffer) > 8:
                self._buffer = self._buffer[:-1]
        self._update()

    def _update(self):
        self._device.text = self._buffer
