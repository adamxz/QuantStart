# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:03:03 2016

@author: wangmeng70
"""

import configure
from spider import Spider

# Analyse the soup
# body-div-div id="main"-div id="center"
if __name__ == '__main__':
    url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/300208.phtml?year=2016&jidu=3'
    spider_engine = Spider()
    soup = spider_engine.soup_read(url)