# -*- coding:utf-8 -*-
# @Date: 2015/11/7
# @Author: Wang Meng
# @Description: import the data of the securities from securities_list.csv into mysql database

# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

import csv
import pymysql
import datetime

import Toolbox.Configure.configure as conf

file_url = csv_url
db_host = conf.db_host
db_user = conf.db_user
db_passwd = conf.db_passwd
db_name = conf.db_name
db_column_num = conf.datasecurity_table_column_num

try:
    conn = pymysql.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name,charset = 'utf8')
    file_csv = open(file_url)
    f_csv = csv.reader(file_csv)
except Exception:
    print(Exception.args[0])
else:  
    headers = next(f_csv)
    cursor = conn.cursor()
    now = datetime.datetime.today()
    column_str = conf.column_str
    column_value_str = ('%s, '* db_column_num)[:-2]
    insert_str = 'insert into data_security (%s) values (%s)' %(column_str, column_value_str)
    for row in f_csv:
        #insert_query = tuple(row)
        insert_query = row
        cursor.execute(insert_str, insert_query)
    conn.commit()
    cursor.close()
    conn.close()