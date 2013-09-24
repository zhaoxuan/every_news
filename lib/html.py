#!/usr/bin/env python2.7

import urllib2
import BeautifulSoup

class Html(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        self.req = urllib2.Request(self.url, headers = self.headers)
        self.get_content()
        pass

    def get_content(self):
        content = urllib2.urlopen(self.req).read()
        self.content = BeautifulSoup.BeautifulSoup(content, from_encoding = 'GB18030')
        return self.content

    def find(self, reg):
        result = self.content.findAll(reg)
        return result
