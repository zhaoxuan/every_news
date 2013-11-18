#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re

class Stock(object):

    """docstring for Stock"""
    def __init__(self, exchange, code):
        super(Stock, self).__init__()
        self.code = code
        self.exchange = exchange
        # http://hq.sinajs.cn/list=s_sh000001
        self.data_api = "http://hq.sinajs.cn/list=s_"
        url = self.data_api + self.exchange + self.code
        headers = {'user-agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}

        self.req = urllib2.Request(url, headers = headers)

    def get_info(self):
        # stockName   = stockInfo[0]
        # stockEnd    = stockInfo[1]  #当前价，15点后为收盘价
        # stockZD     = stockInfo[2]  #涨跌
        # stockFD     = stockInfo[3]  #幅度
        # stockZS     = stockInfo[4]  #总手
        # stockJE     = stockInfo[5]  #金额
        # stockLastEnd= str(float(stockEnd) - float(stockZD)) #开盘价
        # stockZS_W   = str(int(stockZS) / 100)
        # info_table = ['name', 'price', 'advance_decline', 'range', 'total', 'amount']

        data = urllib2.urlopen(self.req).read().decode('gb2312')
        stock_info = re.search('''(")(.+)(")''', data).group(2).split(",")
        return stock_info
