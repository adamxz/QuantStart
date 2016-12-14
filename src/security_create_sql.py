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

file_url = "../tmp/securities_list.csv"
db_host = 'localhost'
db_user = 'root'
db_passwd = '1234'
db_name = 'securities_master'
db_column_num = 14

try:
    conn = pymysql.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name,charset = 'utf8')
    file_csv = open(file_url, 'r', encoding= 'utf-8')
    f_csv = csv.reader(file_csv)
except Exception:
    print(Exception.args[0])
else:  
    headers = next(f_csv)
    cursor = conn.cursor()
    now = datetime.datetime.today()
    column_str = 'id_security,name,abbreviation,state_public,industry,area,capital_registered,date_IPO,price_IPO,shares_notcurrent,shares_limited,shares_current,date_created,date_updated'
    column_value_str = ('%s, '* db_column_num)[:-2]
    insert_str = 'insert into data_security (%s) values (%s)' %(column_str, column_value_str)
    for row in f_csv:
        #insert_query = tuple(row)
        insert_query = row
        cursor.execute(insert_str, insert_query)
    conn.commit()
    cursor.close()
    conn.close()