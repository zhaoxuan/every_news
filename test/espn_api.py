import pytz
import datetime
import time
import urllib2
import json
import os
import elementtree.ElementTree as ET

url = 'http://api.espn.com/v1/sports/basketball/nba/events/top?apikey=g57n78ttcfpnfjgnry3j68e3'

data = urllib2.urlopen(url)

print json.load(data)['sports'][0]
