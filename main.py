import lib.mailer
import time

ts = time.strftime('%a, %d %b %Y %H:%M:%S %z')
lib.mailer.mail("This is raspberry pi.\n" + ts)
