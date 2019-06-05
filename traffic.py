from gpiozero import LED


class TrafficLights(object):
	def __init__(self):
		print("Initializing Traffic Lights...", end='')
		self._green = LED(13)
		self._orange = LED(6)
		self._red = LED(5)
		print("...Done!")

		self._test()

	def _test(self):
		print('Testing Traffic Lights...', end='')
		for l in [self._green, self._orange, self._red]:
			l.on()
			sleep(0.1)
			l.off()
		print('...Done!')

	def cycle(self):
		pass
