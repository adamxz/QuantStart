# -*- confing: utf8 -*-
'''
Created on 2016年6月19日
@description: catch the daily price from
http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/600000.phtml?year=2014&jidu=4
@author: adam
'''
'''
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )
'''

import logging
import socket
from urllib import request
from bs4 import BeautifulSoup
import datetime
import time
import pymysql

import mysql

db_host = 'localhost'
db_user = 'root'
db_passwd = '1234'
db_name = 'securities_master'
charset_type = 'utf8'
table_name = 'daily_price'
test_table_name = 'daily_price_test'
table_column_num = 10

price_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/\
stockid/%s.phtml?year=%d&jidu=%d'
today = datetime.date.today()
year_today = today.year
quarter_today = today.month % 4


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
        cursor.close()
        conn.close()
    return id_security
        
# Analyse the soup
# body-div-div id="main"-div id="center"
def soup_analyze(soup):
    pass

def unit_test(id_security, year_today, quarter_today, sql):
    sql.open_conn()
    soup = soup_read(id_security, year_today,quarter_today)
    soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。
    year_start = soup_table[0].find_all('option')[-5].string  # 获得年份
    #year_range = range(year_today,int(year_start),-1)
    year_range = range(year_today, int(year_start)-1,-1)
    insert_columns = 'id_security, date, price_open, price_high, price_close, price_low, volumn, amount, factor_adj'
    #date_partition = '2006-06-30'
    for year in year_range:
        for quarter in range(4, 0, -1):
            soup = soup_read(id_security, year, quarter)
            soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。      
            '''for i in range(9,len(soup_table),8):
                insert_item = "'" + str(id_security) + "', "
                if year > 2006 or (year == 2006 and quarter >2):
                    insert_item = insert_item + "'" + soup_table[i].a.string[7:17] + "'"
                else:
                    insert_item = insert_item + "'" + soup_table[i].string[8:18] + "'"
                for j in range(1,8):
                    insert_item = insert_item + ", '"+ soup_table[i+j].string + "'"
                sql.insert(table_name, insert_columns, insert_item)
                sql.conn.commit()'''
            for i in range(9,len(soup_table),8):
                insert_item = "'" + str(id_security) + "', "
                if year > 2006:
                    insert_item = insert_item + "'" + soup_table[i].a.string[7:17] + "'"
                elif year == 2006:
                    if quarter > 2:
                        insert_item = insert_item + "'" + soup_table[i].a.string[7:17] + "'"
                    elif quarter == 2:
                        if soup_table[i].a:
                            insert_item = insert_item + "'" + soup_table[i].a.string[7:17] + "'"
                        else:
                            insert_item = insert_item + "'" + soup_table[i].string[8:18] + "'"
                    else:
                        insert_item = insert_item + "'" + soup_table[i].string[8:18] + "'"
                else:
                    insert_item = insert_item + "'" + soup_table[i].string[8:18] + "'"
                for j in range(1,8):
                    insert_item = insert_item + ", '"+ soup_table[i+j].string + "'"
                sql.insert(test_table_name, insert_columns, insert_item)
                sql.conn.commit()
    sql.close_conn()

def unit_action(id_securities, year_today, quarter_today, sql):
    sql.open_conn()
    for id_security in id_securities:
        print(id_security + ' is pouring into MySQL...\n')
        soup = soup_read(id_security, year_today,quarter_today)
        soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。
        year_start = soup_table[0].find_all('option')[-5].string  # 获得年份
        year_range = range(year_today,int(year_start)-1,-1)
        insert_columns = 'id_security, date, price_open, price_high, price_close, price_low, volumn, amount, factor_adj'
        for year in year_range:
            for quarter in range(4, 0, -1):
                soup = soup_read(id_security, year, quarter)
                soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。      
                for i in range(9,len(soup_table),8):
                    insert_item = "'" + str(id_security) + "', "
                    if year > 2006:
                        insert_item = insert_item + "'" + soup_table[i].a.string[7:17] + "'"
                    elif year == 2006:
                        if quarter > 2:
                            insert_item = insert_item + "'" + soup_table[i].a.string[7:17] + "'"
                        elif quarter == 2:
                            if soup_table[i].a:
                                insert_item = insert_item + "'" + soup_table[i].a.string[7:17] + "'"
                            else:
                                insert_item = insert_item + "'" + soup_table[i].string[8:18] + "'"
                        else:
                            insert_item = insert_item + "'" + soup_table[i].string[8:18] + "'"
                    else:
                        insert_item = insert_item + "'" + soup_table[i].string[8:18] + "'"
                    for j in range(1,8):
                        insert_item = insert_item + ", '"+ soup_table[i+j].string + "'"
                    sql.insert(table_name, insert_columns, insert_item)
                    sql.conn.commit()
    sql.close_conn()
                    
if __name__ == '__main__':
    id_securities = get_id_security(db_host, db_user, db_passwd, db_name)
    sql = mysql.Mysql(db_host, db_user, db_passwd, db_name, charset_type)
    unit_action(id_securities[38:], year_today, quarter_today, sql)
    #unit_test(600053, year_today, quarter_today, sql)