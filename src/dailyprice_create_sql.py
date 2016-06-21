# -*- confing: utf8 -*-
'''
Created on 2016年6月19日
@description: catch the daily price from
http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/
stockid/000562.phtml?year=2014&jidu=4
@author: adam
'''

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


import logging
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
import csv
import MySQLdb
import datetime

db_host = 'localhost'
db_user = 'root'
db_passwd = '123456'
db_name = 'securities_master'
table_column_num = 10

# Get the  daily price from 
# Create the tables
try:
    conn = MySQLdb.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name,charset = 'utf8')
except Exception:
    print(Exception.args[0])
else:
    

if __name__ == '__main__':
    pass