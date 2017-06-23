import threading
import time
import os
import logging

logging.basicConfig(format="%(levelname)-7s:[%(threadName)-10s] \n %(message)s", level=logging.DEBUG)

class Test(threading.Thread):
	running = True

	@classmethod
	def die(cls):
		cls.running = False

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while self.running:
			# logging.debug("Hi")
			pass

def main():
	logging.debug("test")

	head = Test()

	threads = [head]

	head.start()

	for i in range(0,100):
		a = Test()

		threads.append(a)
		a.start()

	logging.info(threading.enumerate())

	time.sleep(5)

	head.die()

	for thread in threads:
		thread.join()

	logging.info(threading.enumerate())

	pass

main()