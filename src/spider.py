'''
Created on Jul 8, 2016

@author: adam
'''

from urllib import request
import socket
from bs4 import BeautifulSoup

import logging
import time


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
        try:
            response = request.urlopen(req)
            page = response.read()
        except socket.error:
            logging.warning('Website analysis is paused...' )
            time.sleep(5)
            response = request.urlopen(req)
            page = response.read()
            response.close()
        soup = BeautifulSoup(page, "lxml")
        return soup