from gpiozero import LED


class TrafficLights(object):
	def __init__(self):
		self._green = LED(13)
		self._orange = LED(6)
		self._red = LED(5)

		self._test()

	def _test(self):
		for l in [self._green, self._orange, self._red]:
			l.on()
			sleep(0.1)
			l.off()

	def cycle(self):
		pass
