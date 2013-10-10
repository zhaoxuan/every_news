#!/usr/bin/env python
# -*- coding: utf-8 –*-

import lib.mailer
import lib.weather_forecast
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')



wf = lib.weather_forecast.WeatherForecast()
today_weather =  wf.get_day_weather()
lib.mailer.mail("Every thing is OK " + today_weather)
