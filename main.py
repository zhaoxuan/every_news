#!/usr/bin/env python
# -*- coding: utf-8 –*-

import sys
import lib.mailer
import lib.weather_forecast
from lib.stock import Stock
import datetime
import lib.gl as gl

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    param = sys.argv[1]
    if param == 'weather':
        weather()
        pass
    else:
        stocks_path = gl.ROOT + '/log/StockCode'
        Stock.get_stocks(stocks_path, 60*10)
        now = datetime.datetime.now().strftime("%Y-%M-%d")
        lib.mailer.mail(now + " stock has updated completely.")
        pass

def weather():
    wf = lib.weather_forecast.WeatherForecast()
    today_weather = wf.get_day_weather()
    lib.mailer.mail(today_weather)
    pass



if __name__ == '__main__':
    main()