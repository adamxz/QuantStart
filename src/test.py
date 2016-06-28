# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:03:03 2016

@author: wangmeng70
"""

import logging
import socket
from urllib import request
from bs4 import BeautifulSoup
import datetime
import time

price_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/\
stockid/%s.phtml?year=%d&jidu=%d'

def soup_read(id, year, quarter):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    header = {'User-Agent': user_agent}
    url = price_url %(id, year, quarter)
    req = request.Request(url, headers = header)
    try:
        response = request.urlopen(req)
        page = response.read()
    except socket.error:
        logging.warning('%s is paused...' % id)
        time.sleep(1)
        response = request.urlopen(req)
        page = response.read()
    response.close()
    # body-div-div id="main"
    soup = BeautifulSoup(page)
    return soup
    
# Analyse the soup
# body-div-div id="main"-div id="center"
if __name__ == '__main__':
    soup = soup_read(600000, 2015,1)
    
    print(soup)