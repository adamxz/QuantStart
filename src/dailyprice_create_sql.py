# -*- confing: utf8 -*-
'''
Created on 2016年6月19日
@description: catch the daily price from
http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/
stockid/000562.phtml?year=2014&jidu=4
@author: adam
'''

#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )


import logging
import socket
from urllib import request
from bs4 import BeautifulSoup
import datetime
import time
import pymysql

db_host = 'localhost'
db_user = 'root'
db_passwd = '1234'
db_name = 'securities_master'
table_column_num = 10

price_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/\
stockid/%s.phtml?year=%d&jidu=%d'


# return the soup. 
def soup_read(url, id_security, year, quarter):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    header = {'User-Agent': user_agent}
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
    


# Get the  daily price from 
# Create the tables
try:
    conn = pymysql.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name,charset = 'utf8')
except Exception:
    print(Exception.args[0])
else:
    cursor = conn.cursor()
    select_str = 'select %s from %s' %('id_A','data_security')
    num_security = cursor.execute(select_str)
    id_security = cursor.fetchmany(num_security)
    conn.commit()
    for id in id_security:
        id = str(id)
        id = id[4:10]
        
    

if __name__ == '__main__':
    pass