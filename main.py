#!/usr/bin/env python
# -*- coding: utf-8 –*-

import lib.mailer
import lib.weather_forecast
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

import time
import lib.mailer
from lib.html import Html

def main():
    wf = lib.weather_forecast.WeatherForecast()
    today_weather =  wf.get_day_weather()
    lib.mailer.mail("Every thing is OK " + today_weather)

    ts = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    lib.mailer.mail("Hi john\n This is raspberry pi \n I am fine.\n" + ts)
    html = Html("http://finance.baidu.com/")

    content = html.find('a')
    for item in content:
        print item.text







if __name__ == '__main__':
    main()





