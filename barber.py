from threading import Thread, Semaphore
import threading
import time
import logging
import random
from Queue import Queue

logging.basicConfig(format="%(levelname)-5s on [%(threadName)-10s]: %(message)s", level=logging.DEBUG)

spawnDelay = 1
workDelay = 1
waitDelay = 2

class Barber(Thread):
	def __init__(self, seats):
		Thread.__init__(self)

		self.name = "Barber"

		self.asleep = False
		self.working = True
		self.closing = False
		self.seats = seats

		self.metLast = False

	def run(self):
		while True:
			# logging.info("is still working? {}".format(self.working))

			if self.closing:
				# logging.warning("is trying to close...")
				if self.metLast:
					self.working = False
					break

			if not self.asleep:
				client = self.seats.get()

				if client is None:
					self.asleep = True
					logging.debug("fell asleep...")
				else:
					logging.info("is working on {}".format(client.name))
					self.metLast = client.is_Last

					client.isWorkedOn = True
					logging.info("is done with {}".format(client.name))
					client.isServiced()
					client.join()

			# logging.warning("PASS {}".format(self.closing))			

			time.sleep(1)

		# logging.warning(threading.enumerate())
		logging.debug("is packing up...")


	def wake(self):
		self.asleep = False

	def close(self):
		# logging.warning("is supposed to be packing up...")
		self.closing = True

		# logging.warning("PASS {}".format(self.closing))


class Client(Thread):
	def __init__(self, number, name, waitlist, seats, is_Last):
		Thread.__init__(self)

		self.is_Last = is_Last

		self.name = "Cust No. " + str(number)
		self.CustName = name
		self.waitlist = waitlist
		self.seats = seats

		# Time while being worked on
		self.delay = random.random() * workDelay

		self.waitTime = random.random() * waitDelay
		self.waiting = 0

		# Queue wait time
		self.patience = random.randrange(1,6)

		self.onWait = True
		# self.isSeated = False
		self.isWorkedOn = False
		self.annoyed = False
		

	def run(self):
		while True:
			if self.isWorkedOn:
				self.onWait = False

				time.sleep(self.delay)
				logging.debug("is satisfied and left...")
				break

			if self.annoyed:
				logging.debug("got fed up and left.")
				break

			if self.onWait:
				available = self.waitlist.acquire(False)

				if available:
					logging.info("is now waiting...")
					self.onWait = False
					# self.isSeated = True
					self.seats.put(self)
				else:
					logging.info("will wait " + str(self.patience - self.waiting) + " more times.")
					self.wait()


			# logging.debug("is being worked on...")
			# time.sleep(delay)
	def isServiced(self):
		self.waitlist.release()

	def wait(self):
		if self.waiting >= self.patience:
			self.annoyed = True
		time.sleep(self.waitTime)
		self.waiting += 1

	# def name(self):
	# 	return self.name
		


class ClientManager(Thread):
	def __init__(self, clients, barber, waitlist, seats):
		Thread.__init__(self)

		self.name = "Counter"

		self.maxClient = clients
		self.clientNo = 0

		self.clientele = []

		self.waitlist = waitlist
		self.seats = seats
		self.worker = barber

	def run(self):
		while True:
			self.glean()

			if self.clientNo >= self.maxClient:
				# logging.warning("{} : Empty? {}".format(self.clientele, self.seats.empty()))

				if not self.clientele:
					self.worker.close()
					break

			# if len(self.clientele) > 0:
				# self.barber.wake()

			time.sleep(random.random() * spawnDelay)

			# logging.warning(str(self.clientNo) + " >= " + str(self.maxClient))
			chance = random.random()
			if chance >= 0.5 and not self.clientNo >= self.maxClient:
				newCust = self.spawn()
				self.clientele.append(newCust)
				newCust.start()


		logging.debug("has closed.")

	def glean(self):
		for client in self.clientele:
			if not client.isAlive():
				self.clientele.remove(client)

	def spawn(self):
		logging.info("A client appeared.")
		self.clientNo += 1

		if self.clientNo >= self.maxClient:
			return Client(self.clientNo, "Bob", self.waitlist, self.seats, True)
		else:
			return Client(self.clientNo, "Bob", self.waitlist, self.seats, False)
		

def main():
	seatLimit = 1
	custNo = 10

	logging.debug("Shop has opened.")

	waitlist = Semaphore(seatLimit)
	seats = Queue()
	worker = Barber(seats)
	reception = ClientManager(custNo, worker, waitlist, seats)

	worker.start()
	reception.start()

	# print threading.enumerate()

	reception.join()
	worker.join()

	logging.debug("Shop has closed.")


# Program Execution
main()