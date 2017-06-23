# / Requests
# Parser - BeautifulSoup
import requests
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
folderPath = "Gallery"

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
# r = requests.get('https://xkcd.com/')
r = requests.get('https://c.xkcd.com/random/comic/')
soup = BeautifulSoup(r.text, 'html.parser')
selector = '#comic img'
img = soup.select(selector)[0]


# Get image from image url
image_url = 'https:' + img.attrs['src']
r = requests.get(image_url)
filename = img.attrs['src'].split('/')[-1]
i = Image.open(StringIO(r.content))
i.save("{}/{}".format(folderPath, filename))



# Build gallery for 50 images

# import requests
# r = requests.get('https://c.xkcd.com/random/comic/')
# print r.status_code
# print r.url


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GlobalResource(threading.Thread):
	# Global Killswitch
	running = True

	@classmethod
	def die(cls):
		cls.running = False

	def __init__(self):
		Thread.__init__(self)


class Crawler(threading.Thread):
	# # Global Killswitch
	# running = True

	# @classmethod
	# def die(cls):
	# 	cls.running = False

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	def __init__(self, urlCache):
		super().__init__(self)
		
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
				pass


			pass

class Parser(threading.Thread):
	# # Global Killswitch
	# running = True
	lastFound = False

	# @classmethod
	# def die(cls):
	# 	cls.running = False

	@classmethod
	def sawLast(cls):
		cls.lastFound = False

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	def __init__(self):
		super().__init__(self)
		
		self.workLoad = []

		pass

	def run(self):
		while self.running:
			pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():

	size = 50
	urlQueue = Queue(size)

	pass

######

main()