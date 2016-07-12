# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2016

@author: adam
'''

from urllib import request
import socket
from bs4 import BeautifulSoup

import logging
import time

import configure.ConfSpider as cs

socket.setdefaulttimeout(cs.timeout)

class Spider(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        self.header = {'User-Agent': self.user_agent}

    def soup_read(self, url):
        req = request.Request(url, headers = self.header)
        for i in range(0, cs.max_try):
            try:
                response = request.urlopen(req)
                # https://www.zhihu.com/question/30970752
                page = response.read().decode('gb2312', 'ignore')
            except socket.error:
                logging.warning('Website analysis is paused for %d times', i+1)
                time.sleep(5)
            else:
                response.close()
                break
        # sina网页有部分不符合标准的xml，如果使用‘lxml'无法正确解析，如002752 300208 300234 300361 300388
        soup = BeautifulSoup(page, "lxml")
        return soup