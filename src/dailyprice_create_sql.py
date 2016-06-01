# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:52:33 2016

@author: wangmeng70
@ description: catch the daily price form
http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/
stockid/000562.phtml?year=2014&jidu=4
"""

#网页和脚本编码不一致，需要编码转换
#使中文可以正常显示
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


import logging
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
import csv
import MySQLdb
import datetime

file_url = "E:/Dev/GitHub/QuantStart/tmp/securities_list.csv"
db_host = 'localhost'
db_user = 'root'
db_passwd = '123456'
db_name = 'securities_master'
table_column_num = 10

# Create the tables




