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
#import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )


import logging
from urllib import request
from bs4 import BeautifulSoup
import pymysql
import datetime

db_host = 'localhost'
db_user = 'root'
db_passwd = '1234'
db_name = 'securities_master'
table_column_num = 10
table_name_security = 'data_security'


# Create the tables
try:
    conn = pymysql.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name,charset = 'utf8')
except Exception:
    print(Exception.args[0])
else:
    cursor = conn.cursor()
    select_str = 'select %s from %s' %('id_A','data_security')
    num_security = cursor.execute(select_str)
    table_name = cursor.fetchmany(num_security)
    conn.commit()
    for i in table_name:
        j = str(i)
        drop_str = 'drop table `daily_price_%s`;' %j[4:10]
        '''create_str = 'create table `daily_price_%s` (\
        `id` int not null auto_increment, \
        `date_price` date not null, \
        `price_open` decimal(19,4) null, \
        `price_high` decimal(19,4) null, \
        `price_low` decimal(19,4) null, \
        `price_close` decimal(19,4) null, \
        `factor_adj` decimal(19,4) null, \
        `volumn` bigint null, \
        `amount` bigint null, \
        primary key (`id`) \
        )  engine=InnoDB auto_increment=1 default charset=utf8;' %j[4:10]
        #cursor.execute(drop_str) 
        cursor.execute(create_str)'''
        #add_str = 'ALTER TABLE daily_price_%s ADD `amount` bigint null;' %j[4:10]
        cursor.execute(drop_str)
        conn.commit()
    cursor.close()
    conn.close()

