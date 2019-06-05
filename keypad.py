from pad4pi import rpi_gpio


KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"],
]

ROW_PINS = [22, 23, 25, 24] # BCM numbering
COL_PINS = [4, 17, 27] # BCM numbering


class Keypad(object):
	def __init__(self, callback):
		self._factory = rpi_gpio.KeypadFactory()
		self._keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
		self._keypad.registerKeyPressHandler(callback)
