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
from concurrent.futures import ThreadPoolExecutor
import threading
import lib.gl as gl

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    param = sys.argv[1]
    if param == 'weather':
        weather()
        pass
    else:
        # stock()
        stocks = open(gl.ROOT + '/log/StockCode', 'r')
        Stock.get_stocks(stocks, 60*10)
        stocks.close()
        pass

def stock():
    if datetime.now().strftime('%H%M') < '1500':
        threading.Timer(60*10, stock).start()

    now = datetime.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')
    file_name = now.strftime('%Y%m%d%H%M')
    file_path = '/log/' + year + '/' + month + '/' + day + '/' + file_name + '.tsv'

    stocks = open(gl.ROOT + '/log/StockCode', 'r')
    f = File(gl.ROOT + file_path)

    stock_codes = []
    while True:
        line = stocks.readline()
        if not line:
            break
        else:
            exchange = line[0:2]
            code = line[2:]
            stock_codes.append([exchange, code])

    with ThreadPoolExecutor(max_workers = 10) as executer:
        for stk in stock_codes:
            executer.submit(get_stock_info, stk[0], stk[1], f)
            pass

    f.close
    stocks.close
    pass

def get_stock_info(exchange, code, f):
    st = Stock(exchange, code)
    stock_info = st.get_info()
    if stock_info == None:
        print 'failed ' + exchange + code
        return 'failed'
    else:
        f.write('\t'.join(stock_info) + '\n')
        return 'successed'

def weather():
    wf = lib.weather_forecast.WeatherForecast()
    today_weather =  wf.get_day_weather()
    lib.mailer.mail(today_weather)
    pass



if __name__ == '__main__':
    main()