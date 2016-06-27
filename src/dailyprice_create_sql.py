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

import mysql


table_column_num = 10

price_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/\
stockid/%s.phtml?year=%d&jidu=%d'
year_today = datetime.date.today().year
quarter_today = datetime.date.today().month % 4


# return the soup. 
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
    soup = BeautifulSoup(page, "lxml")
    return soup


# Get the id_security
def get_id_security(db_host, db_user, db_passwd, db_name):
    try:
        conn = pymysql.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name,charset = 'utf8')
    except Exception:
        print(Exception.args[0])
    else:
        cursor = conn.cursor()
        select_str = 'select %s from %s' %('id_A','data_security')
        num_security = cursor.execute(select_str)
        id_security_tmp = cursor.fetchmany(num_security)
        conn.commit()
        id_security = []
        for id in id_security_tmp:
            id = str(id)
            id_security.append(id[4:10])
    return id_security
        
# Analyse the soup
# body-div-div id="main"-div id="center"
def soup_analyze(soup):
    soup.div.get

if __name__ == '__main__':
    sql = mysql.Mysql()
    sql.open_conn()
    id_security = 300001
    soup = soup_read(id_security, year_today,quarter_today)
    soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。
    year_start = soup_table[0].find_all('option')[-5].string  # 获得年份
    year_range = range(year_today,int(year_start),-1)
    insert_columns = 'id_security, date, price_open, price_high, price_close, price_low, volumn, amount, factor_adj'
    for year in year_range:
        soup = soup_read(id_security, year_today,quarter_today)
        soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。
        for i in range(9,len(soup_table),8):
            insert_item = []
            insert_item.append(soup_table[i].a.string[7:17])
            for j in range(1,8):
                insert_item.append(soup_table[i+j].string)
            sql.insert(insert_item, )
    
    print(soup)