#!/usr/bin/env python
# -*- coding: utf-8 –*-

import sys
import lib.mailer
import lib.weather_forecast
from lib.stock import Stock
from lib.file import File
# import os
import pdb
from datetime import *

reload(sys)
sys.setdefaultencoding('utf8')

ROOT = sys.path[0]


def main():
    param = sys.argv[1]
    if param == 'weather':
        weather()
        pass
    else:
        stock()
        pass

def stock():
    now = datetime.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    file_name = now.strftime('%Y%m%d%H%M')
    file_path = '/log/' + year + '/' + month + '/' + file_name + '.tsv'

    stocks = open(ROOT + '/log/StockCode', 'r')
    f = File(ROOT + file_path)

    while True:
        line = stocks.readline()
        if not line:
            break
        else:
            exchange = line[0:2]
            code = line[2:]
            st = Stock(exchange, code)
            stock_info = st.get_info()

            if stock_info == None:
                pass
            else:
                f.write('\t'.join(stock_info) + '\n')

    f.close
    stocks.close
    lib.mailer.mail("Stock process has completed")
    pass

def weather():
    wf = lib.weather_forecast.WeatherForecast()
    today_weather =  wf.get_day_weather()
    lib.mailer.mail(today_weather)
    pass



if __name__ == '__main__':
    main()