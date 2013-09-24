#!/usr/bin/env python2.7

import time
import lib.mailer
from lib.html import Html

def main():
    ts = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    # lib.mailer.mail("Hi john\n This is raspberry pi \n I am fine.\n" + ts)
    html = Html("http://finance.baidu.com/")

    content = html.find('a')
    for item in content:
        print item







if __name__ == '__main__':
    main()