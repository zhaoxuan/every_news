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
        # self.data_api = "http://hq.sinajs.cn/list="
        self.data_api = "http://qt.gtimg.cn/q="
        url = self.data_api + self.exchange + self.code
        headers = {'user-agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}

        self.req = urllib2.Request(url, headers = headers)

    def get_info(self):
        # 0   => '未知',
        # 1   => '名字',
        # 2   => '代码',
        # 3   => '当前价格',
        # 4   => '昨收',
        # 5   => '今开',
        # 6   => '成交量',
        # 7   => '外盘',
        # 8   => '内盘',
        # 9   => '买一',
        # 10  => '买一量',
        # 19  => '卖一',
        # 20  => '卖一量',
        # 29  => '最近逐笔成交',
        # 30  => '时间',
        # 31  => '涨跌',
        # 32  => '涨跌%',
        # 33  => '最高',
        # 34  => '最低',
        # 35  => '价格/成交量（手）/成交额',
        # 36  => '成交量',
        # 37  => '成交:万',
        # 38  => '换手率%',
        # 39  => '市盈率',
        # 40  => '',
        # 41  => '最高',
        # 42  => '最低',
        # 43  => '振幅%',
        # 44  => '流通市值',
        # 45  => '总市值',
        # 46  => '市净率',
        # 47  => '涨停价',
        # 48  => '跌停价',
        # 49  => '未知',

        data = urllib2.urlopen(self.req).read().decode('gb2312')
        data = re.search('''(")(.+)(")''', data)
        if data == None:
            pass
        else:
            stock_info = data.group(2).split("~")
            return stock_info
