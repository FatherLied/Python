import threading
import time
import logging

logging.basicConfig(format="%(levelname)s: [%(threadName)-10s] %(message)s", level=logging.DEBUG)

forks = []
names = []
threads = []

# To make additions easy
def fill(lockCount, *args):
    # pool = ["Aristotle", "Kant", "Buddha", "Russel", "Marx"]
    # forkNo = 5
    # names = pool
    names.extend(args)

    for i in range(0, lockCount):
        forks.append(threading.Lock())

class thinkerThread(threading.Thread):
    def __init__(self, name, num):
        threading.Thread.__init__(self)

        self.name = name
        self.num = num
        self.done = False

    def run(self):
        rightFork = forks[self.num % len(forks)]
        leftFork = forks[(self.num+1) % len(forks)]

        with rightFork:
            logging.debug(" picks the right Fork [" + str(self.num % len(forks)) + "]")
            
            with leftFork:
                logging.debug(" picks the left Fork [" + str((self.num+1) % len(forks)) + "]")
                logging.debug(" started eating...")

                self.done = True

                logging.debug(" drops the left Fork [" + str((self.num+1) % len(forks)) + "]")

            if not self.done:
                logging.info(" can't get left Fork (" + str((self.num+1) % len(forks)) + ")")

            logging.debug(" drops the right Fork [" + str(self.num % len(forks)) + "]")

        if not self.done:
            logging.debug(" continued thinking...")
        else:
            logging.debug(" leaves...")

        time.sleep(1)


def main():
    fill(5, "Aristotle", "Kant", "Buddha", "Russel", "Marx")

    for i in range(0, len(names)):
        # pass
        actor = thinkerThread(names[i], i)
        threads.append(actor)
    
    for actor in threads:
        actor.start()

    for actor in threads:
        actor.join()

    logging.debug("Everyone is full.")

main()