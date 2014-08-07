#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from datetime import *
from lib.file import File
from concurrent.futures import ThreadPoolExecutor
import threading
import socket
import time
import re
import gl

class Stock(object):

    """docstring for Stock"""
    def __init__(self, exchange, code):
        super(Stock, self).__init__()
        self.code = code
        self.exchange = exchange
        # http://hq.sinajs.cn/list=s_sh000001
        # self.data_api = "http://hq.sinajs.cn/list="
        # use tencent api for getting stock data
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

        for try_times in xrange(1,4):
            try:
                start = time.time()
                data = urllib2.urlopen(self.req, timeout = 1).read().decode('gb2312')
                data = re.search('''(")(.+)(")''', data)
                end = time.time()
                print("It takes " + str(end - start) + " second")
                if data == None:
                    pass
                else:
                    stock_info = data.group(2).split("~")
                    return stock_info
            except Exception:
                if try_times < 3:
                    print try_times
                    pass
                else:
                    return None


    @classmethod
    def get_stocks(cls, stocks_path, frequency):
        if datetime.now().strftime('%H%M') < '1500':
            threading.Timer(frequency, cls.get_stocks, [stocks_path, frequency]).start()

        now = datetime.now()
        year = now.strftime('%Y')
        month = now.strftime('%m')
        day = now.strftime('%d')
        file_name = now.strftime('%Y%m%d%H%M')
        file_path = '/log/' + year + '/' + month + '/' + day + '/' + file_name + '.tsv'

        f = File(gl.ROOT + file_path)
        stocks = open(stocks_path, 'r')
        stock_codes = cls.parse_stock_info(stocks)
        stocks.close()

        with ThreadPoolExecutor(max_workers = 5) as executer:
            for stk in stock_codes:
                executer.submit(cls.get_stock_info, stk[0], stk[1], f)
                pass

        f.close()
        pass

    @classmethod
    def get_stock_info(cls, exchange, code, f):
        st = Stock(exchange, code)
        stock_info = st.get_info()
        if stock_info == None:
            print 'failed ' + exchange + code
            return 'failed'
        else:
            f.write('\t'.join(stock_info) + '\n')
            return 'successed'

    @classmethod
    def parse_stock_info(cls, stock_file):
        stock_codes = []
        while True:
            line = stock_file.readline()
            if not line:
                break
            else:
                exchange = line[0:2]
                code = line[2:]
                stock_codes.append([exchange, code])
        return stock_codes
