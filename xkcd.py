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

# Get image from home
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
        self.processed = 0
        self.completed = 0

    def _init(self, maxsize):
        self.queue = OrderedSet()

    def _put(self, item):
        if self.isFull():
            return False

        if self.queue.add(item):
            self.itemCount += 1
            return True
        else:
            return False

    def take(self):

        if not self.isEmpty():
            return self.get()
        else:
            return None

    def _get(self):
        self.processed += 1
        return self.queue.pop()

    def scrape_done(self):
        self.completed += 1

    def isFull(self):
        if self.itemCount >= self.itemLimit:
            return True
        else:
            return False

    def isEmpty(self):
        if self.processed >= self.itemCount:
            return True
        else:
            return False

    def isMaxed(self):
        if self.processed >= self.itemLimit:
            return True
        else:
            return False

    def isComplete(self):
        if self.completed >= self.itemLimit:
            return True
        else:
            return False



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GlobalResource(threading.Thread):
    # Global Killswitch
    running = True
    idNo = 1

    @classmethod
    def die(cls):
        cls.running = False

    @classmethod
    def incrementID(cls):
        cls.idNo += 1



    def __init__(self):
        threading.Thread.__init__(self)


class Crawler(GlobalResource):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, urlCache, isDeath):
        GlobalResource.__init__(self)
        
        self.workLoad = []
        self.urlCache = urlCache
        if not isDeath:
            self.name = "Crawler-{}".format(self.idNo)
            self.incrementID()
        else:
            self.name = "Crawler-X"

        self.isDeath = isDeath

        pass

    def run(self):
        while self.running:
            if not self.isDeath:
                if not self.urlCache.isFull():
                    r = requests.get('https://c.xkcd.com/random/comic/')
                    time.sleep(1)

                    image_url = r.url
                    logging.info("Crawler Found: {}".format(image_url))

                    self.urlCache.put(image_url)

                if self.urlCache.isFull():
                    break
                logging.info("[{} {} {}]".format(self.urlCache.itemCount,
                                                 self.urlCache.processed,
                                                 self.urlCache.completed))
        logging.warning("PROCESS TERMINATED [CRAWLER]")

class Parser(GlobalResource):

    lastFound = False

    @classmethod
    def sawLast(cls):
        cls.lastFound = False

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, urlCache, isDeath):
        GlobalResource.__init__(self)
        
        self.urlCache = urlCache
        if not isDeath:
            self.name = "Parser-{}".format(self.idNo)
            self.incrementID()
        else:
            self.name = "Parser-X"

        self.isDeath = isDeath

        pass

    def run(self):
        while self.running:
            if not self.isDeath:
                if self.urlCache.isComplete():
                    break

                image_url = self.urlCache.take()

                if image_url is not None:
                    logging.info("Parser Got: {}".format(image_url))

                    r = requests.get(image_url)
                    soup = BeautifulSoup(r.content, 'html.parser')
                    selector = '#comic img'
                    img = soup.select(selector)[0]


                    # Get image from image url
                    image_url = 'https:' + img.attrs['src']
                    r = requests.get(image_url)
                    filename = img.attrs['src'].split('/')[-1]
                    i = Image.open(StringIO(r.content))
                    i.save("{}/{}".format(folderPath, filename))

                    self.urlCache.scrape_done()

                    logging.info("[{} {} {}]".format(self.urlCache.itemCount,
                                                     self.urlCache.processed,
                                                     self.urlCache.completed))

        logging.warning("PROCESS TERMINATED [PARSER]")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def main():
    size = 50
    threadLimit = 10
    urlCache = OrderedSetQueue(0, size)

    activeThreads = []

    def glean(threads):
        for thread in threads:
            if not thread.isAlive():
                threads.remove(thread)

    for i in range(0, threadLimit/2):
        crawlerTail = Crawler(urlCache, False)
        activeThreads.append(crawlerTail)

        crawlerTail.start()

    for i in range(0, threadLimit/2):
        parserTail = Parser(urlCache, False)
        activeThreads.append(parserTail)

        parserTail.start()

    while True:
        if urlCache.isComplete():
            break

        glean(activeThreads)

        if len(activeThreads) < threadLimit:
            if not urlCache.isFull():
                crawlerTail = Crawler(urlCache, False)
                activeThreads.append(crawlerTail)

                crawlerTail.start()
            else:
                parserTail = Parser(urlCache, False)
                activeThreads.append(parserTail)

                parserTail.start()

        time.sleep(1)
        logging.info(threading.enumerate())

        logging.info("Still alive")

    crawlerTail = Crawler(urlCache, True)
    logging.info(threading.enumerate())
    crawlerTail.die()

    parserTail = Parser(urlCache, True)
    logging.info(threading.enumerate())
    parserTail.die()

    glean(activeThreads)

######

main()