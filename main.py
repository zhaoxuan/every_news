import sys;
path = "/mnt/usb/opt/every_news/lib"
if not path in sys.path:
  sys.path.append(path)
if not 'mailer' in sys.modules:
  import mailer

# import BeautifulSoup
# import urllib2
# import types

mailer.mail("Hi john\n This is raspberry pi \n I am fine.")
# url = "http://www.baidu.com"
# req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
# webpage = urllib2.urlopen(req)

# soup = BeautifulSoup.BeautifulSoup(webpage.read())

# a_tags = soup.findAll("a")

# print type(a_tags)