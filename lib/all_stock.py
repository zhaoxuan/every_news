from HTMLParser import HTMLParser
import urllib2
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "name":
                        self.links.append(value)

if __name__ == "__main__":
    a = ['sha0','sha1','sha2','sha3','sha4','sha5','sha6','sha7','sha8','sha9','sha10','sha11','sha12','sha13','sha14','sha15','sha16','sza0','sza2','sza3','sza4','sza5','sza6','sza7','sza8','sza9']
    root = sys.path[0]
    f = open(root + '/../log/StockCode', 'a')
    for i in a:
        url = 'http://stock.sina.com.cn/stock/quote/' + i + '.html'
        html_code = urllib2.urlopen( url ).read()
        hp = MyHTMLParser()
        hp.feed(html_code)
        hp.close()
        for item in hp.links:
            f.write(item + '\n')
        pass
    f.close
