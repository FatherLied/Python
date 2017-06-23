# # / Requests
# # Parser - BeautifulSoup
# import requests
# from PIL import Image
# from StringIO import StringIO
# from bs4 import BeautifulSoup

# # Get image from home
# r = requests.get('https://xkcd.com/')
# soup = BeautifulSoup(r.text, 'html.parser')
# selector = '#comic img'
# img = soup.select(selector)[0]


# # Get image from image url
# image_url = 'https:' + img.attrs['src']
# r = requests.get(image_url)
# filename = img.attrs['src'].split('/')[-1]
# i = Image.open(StringIO(r.content))
# i.save(filename)



# # Build gallery for 50 images

import requests
r = requests.get('https://c.xkcd.com/random/comic/')
print r.status_code
print r.url