from concurrent.futures import ThreadPoolExecutor
import urllib2
import threading
from datetime import *

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://www.foxnews.com/']

# Retrieve a single page and report the url and contents
# def load_url(url, timeout):
#     headers = {'user-agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
#     req = urllib2.Request(url, headers = headers)
#     conn = urllib2.urlopen(req).read()
#     return conn
# now = datetime.now()
# with ThreadPoolExecutor(max_workers=5) as executor:
#     for url in URLS:
#         result = executor.submit(load_url, url, 60)
#         print result.result()
# print datetime.now() - now
def puts(a, b):
    print a
    print b
    pass

threading.Timer(2, puts, [1]).start()