from gpiozero import Button


class ButtonHandler(object):
	def __init__(self, matrix_button_callback, traffic_button_callback):
		print("Initializing Button Handler...", end='')
		self._matrix_button = Button(26)
		self._matrix_button.when_pressed = matrix_button_callback
		self._traffic_button = Button(12)
		self._traffic_button.when_pressed = traffic_button_callback
		print("...Done!")