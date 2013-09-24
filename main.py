import lib.mailer
import lib.weather_forecast
import time

ts = time.strftime('%a, %d %b %Y %H:%M:%S %z')
# lib.mailer.mail("This is raspberry pi.\n" + ts)

wf = lib.weather_forecast.WeatherForecast()
print wf.get_day_weather()