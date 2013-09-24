import lib.mailer
import time

ts = time.strftime('%a, %d %b %Y %H:%M:%S %z')
lib.mailer.mail("Hi john\n This is raspberry pi \n I am fine.\n" + ts)
