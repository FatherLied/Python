# / Requests
# Parser - BeautifulSoup
import requests
import collections
from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup
from Queue import Queue
import threading
import time
import os
import logging

logging.basicConfig(format="%(levelname)-7s:[%(threadName)-10s] %(message)s", level=logging.DEBUG)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Credits go to Stackoverflow mate
t = time.strftime("%Y-%m-%d")
folderPath = "Gallery/{}".format(t)

try:
    if not os.path.exists(folderPath):
        logging.info(">> Making directory [/{}]...".format(folderPath))

        os.makedirs(folderPath)

        logging.info(">> ...directory made.")
    else:
        logging.info(">> Directory exists...")
except Exception as e:
    logging.info(">> ERROR: {}".format(e))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # Get image from home
# # r = requests.get('https://xkcd.com/')
# r = requests.get('https://c.xkcd.com/random/comic/')
# soup = BeautifulSoup(r.text, 'html.parser')
# selector = '#comic img'
# img = soup.select(selector)[0]


# # Get image from image url
# image_url = 'https:' + img.attrs['src']
# r = requests.get(image_url)
# filename = img.attrs['src'].split('/')[-1]
# i = Image.open(StringIO(r.content))
# i.save("{}/{}".format(folderPath, filename))



# Build gallery for 50 images

# import requests
# r = requests.get('https://c.xkcd.com/random/comic/')
# print r.status_code
# print r.url

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Ported Code

# [from: http://code.activestate.com/recipes/576694/]
class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]
            return True
        else:
            return False

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

# [from: https://stackoverflow.com/questions/16506429/check-if-element-is-already-in-a-queue]
class OrderedSetQueue(Queue):
    def __init__(self, maxsize, itemLimit):
        Queue.__init__(self, maxsize)

        self.itemLimit = itemLimit
        self.itemCount = 0

    def _init(self, maxsize):
        self.queue = OrderedSet()

    def _put(self, item):
        if self.itemCount >= self.itemLimit:
            print "False"
            return False

        if self.queue.add(item):
            self.itemCount += 1
            print "True"
            return True
        else:
            print "False"
            return False
    def _get(self):
        # self.itemCount += 1
        return self.queue.pop()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GlobalResource(threading.Thread):
    # Global Killswitch
    running = True

    @classmethod
    def die(cls):
        cls.running = False

    def __init__(self):
        threading.Thread.__init__(self)


class Crawler(GlobalResource):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, urlCache):
        GlobalResource.__init__(self)
        
        self.workLoad = []
        self.urlCache = urlCache

        pass

    def run(self):
        while self.running:
            r = requests.get('https://c.xkcd.com/random/comic/')
            soup = BeautifulSoup(r.text, 'html.parser')
            selector = '#comic img'
            img = soup.select(selector)[0]

            image_url = 'https:' + img.attrs['src']

            if urlCache.qSize() < 50:

                # Do something

                pass

            pass

class Parser(GlobalResource):

    lastFound = False

    @classmethod
    def sawLast(cls):
        cls.lastFound = False

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self):
        # GlobalResource.__init__(self)
        
        self.workLoad = []

        pass

    def run(self):
        while self.running:
            pass

# Test Thread
class SetChecker(GlobalResource):

    def __init__(self, setQueue, setInput):
        GlobalResource.__init__(self)
        
        self.setQueue = setQueue
        self.setInput = setInput
        

    def run(self):
        i = 0

        while self.running:
            if i < len(self.setInput):
                self.setQueue.put(self.setInput[i])
                i += 1

            pass


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():

    size = 50
    urlQueue = OrderedSetQueue(0,9)

    a = SetChecker(urlQueue, ["a", "b", "c"])
    b = SetChecker(urlQueue, ["1", "2", "3", "4"])
    c = SetChecker(urlQueue, ["d", "d", "e", "f"])

    a.start()
    b.start()
    c.start()

    time.sleep(1)
    a.die()

    a.join()
    b.join()
    c.join()

    print urlQueue.qsize()

    print "\n"

    print urlQueue.get()
    print urlQueue.get()
    print urlQueue.get()
    print urlQueue.get()
    print urlQueue.get()
    print urlQueue.get()
    print urlQueue.get()
    print urlQueue.get()
    print urlQueue.get()

    # urlQueue.put("b")

    pass

######

main()