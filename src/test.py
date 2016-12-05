# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 13:03:03 2016

@author: wangmeng70
"""

import Toolbox.Configure.configure as conf
import Toolbox.mysql as mysql
import csv

# Analyse the soup
# body-div-div id="main"-div id="center"
if __name__ == '__main__':
    '''url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/300208.phtml?year=2016&jidu=3'
    spider_engine = Spider()
    soup = spider_engine.soup_read(url)'''
    
    # @Description: import the data of the securities from securities_list.csv into mysql database
    file_url = '/disk/GitHub/QuantStart/tmp/securities_list2.csv'    
    data_engine = mysql.Mysql()    
    db_column_num = conf.datasecurity_table_column_num
    data_engine.open_conn()
    file_csv = open(file_url, 'r')
    f_csv = csv.reader(file_csv)
    headers = next(f_csv)
    column_str = 'id_new, id_old'
    table_name = 'tmp'
    for row in f_csv:
    #insert_query = tuple(row)
        insert_values = "'"+row[0]+"'"+","+"'"+row[1]+"'"
        data_engine.insert(table_name, column_str, insert_values)
    data_engine.close_conn()