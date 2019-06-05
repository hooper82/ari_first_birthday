from gpiozero import LED
from time import sleep


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
		if self._green.is_lit:
			self._green.off()
			self._orange.on()
		elif self.orange.is_lit:
			self._orange.off()
			self._red.on()
		elif self._red.is_lit:
			self._red.off()
		else:
			self._green.on()
