import sys
import os
import time

ROOT_PATH = os.getcwd()
path = ROOT_PATH + "/lib"
if not path in sys.path:
  sys.path.append(path)
if not 'mailer' in sys.modules:
  import mailer

ts = time.strftime('%a, %d %b %Y %H:%M:%S %z')
mailer.mail("Hi john\n This is raspberry pi \n I am fine.\n" + ts)

# import BeautifulSoup
# import urllib2
# import types

# url = "http://www.baidu.com"
# req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
# webpage = urllib2.urlopen(req)

# soup = BeautifulSoup.BeautifulSoup(webpage.read())

# a_tags = soup.findAll("a")

# print type(a_tags)