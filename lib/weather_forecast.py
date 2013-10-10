#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2  
import simplejson as json


class TimeoutException(Exception): 
    pass

class WeatherForecast(object):
    """docstring for WeatherForecast"""
    def __init__(self):
        url = 'http://m.weather.com.cn/data/101010100.html'
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

        self.req = urllib2.Request(url, headers = headers)

    def get_day_weather(self):
        # result = {
        #     'city':weather_info['city'],
        #     'datetime':weather_info['date_y'],
        #     'temperature':weather_info['temp1'],
        #     'weather':weather_info['weather1'],
        #     'cloud':weather_info['wind1'],
        #     'ziwai':weather_info['index_uv'],
        #     'yifu':weather_info['index_d']
        # }  
        try_times = 3
        for try_times in xrange(1,4):
            try:
                weather_html = urllib2.urlopen(self.req).read()
                weather_json = json.loads(weather_html)
                weather_info = weather_json['weatherinfo']
                result = weather_info['city'] + u' 温度 ' + weather_info['temp1']
                return result
            except Exception:
                if try_times < 3:
                    print try_times
                    pass
                else:
                    return "timeout except"
