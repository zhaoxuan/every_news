from HTMLParser import HTMLParser
import urllib2
import sys
import re
import string

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        pattern = re.compile(r'http://bbs.10jqka.com.cn/')

        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    match = pattern.split(value)
                    if len(match) == 2:
                        tmp = match[1].split(',')
                        if tmp[0] != 'fu':
                            self.links.append(string.join(tmp[0:2], ''))

if __name__ == "__main__":
    root = sys.path[0]
    f = open(root + '/../log/StockCode', 'a')
    url = 'http://bbs.10jqka.com.cn/codelist.html'
    html_code = urllib2.urlopen( url ).read()
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    for item in hp.links:
        f.write(item + '\n')
    f.close









