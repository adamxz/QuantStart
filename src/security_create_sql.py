# -*- coding:utf-8 -*-
# @Date: 2015/11/7
# @Author: Wang Meng
# @Description: import the data of the securities from securities_list.csv into mysql database

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import csv
import MySQLdb
import datetime

file_url = "/home/adam/Quant/Projects/securities_list.csv"
db_host = 'localhost'
db_user = 'root'
db_passwd = '123456'
db_name = 'securities_master'
db_column_num = 14

try:
  conn = MySQLdb.connect(host = db_host, user = db_user, passwd = db_passwd, db = db_name,charset = 'utf8')
  file_csv = open(file_url)
  f_csv = csv.reader(file_csv)
except Exception,e:
  print(e)
else:  
  headers = next(f_csv)
  cursor = conn.cursor()
  now = datetime.datetime.today()
  column_str = 'id,name,abbreviation,state_public,industry,area,capital_registered,date_IPO,price_IPO,shares_notcurrent,shares_limited,shares_current,date_created,date_updated'
  column_value_str = ('%s, '* db_column_num)[:-2]
  insert_str = 'insert into data_security (%s) values (%s)' %(column_str, column_value_str)
  for row in f_csv:
    insert_query = tuple(row)
    cursor.execute(insert_str, insert_query)
  conn.commit()
  cursor.close()
  conn.close()
