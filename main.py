#!/usr/bin/env python
# -*- coding: utf-8 –*-

import sys
import lib.mailer
import lib.weather_forecast
from lib.stock import Stock
from lib.file import File
import os

reload(sys)
sys.setdefaultencoding('utf8')

ROOT = sys.path[0]


def main():
    param = sys.argv[1]

    try:
        if param == 'weather':
            weather()
        else:
            stock()
            pass
    except Exception, e:
        # lib.mailer.mail("Every news has an error {0}".format(str(e)))
        raise e

def stock():
    # info_table = ['name', 'price', 'advance_decline', 'range', 'total', 'amount']
    # st = Stock('sh', '600036')
    # stock_info = st.get_info()

    f = File(ROOT + '/log/lig/stock.txt')
    f.write('1234\n')
    # f = open(ROOT + '/log/stock.txt', 'a')
    # f.write("asdf\n")
    # f.close

    pass

def weather():
    wf = lib.weather_forecast.WeatherForecast()
    today_weather =  wf.get_day_weather()
    lib.mailer.mail(today_weather)
    pass



if __name__ == '__main__':
    main()