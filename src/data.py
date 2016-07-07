'''
Created on Jul 6, 2016

@author: adam
'''

import datetime
import os, os.path
import pandas as pd

from abc import ABCMeta, abstractmethod

import mysql
import configure
import spider

class DataHandler(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_all_symbols(self):
        
        raise NotImplementedError("Should implement get_all_symbols()")
    
    @abstractmethod
    def get_latest_bars(self, symbol, N = 1):
        """
        Returns the last N bars from the latest symbol_list,
        or fewer if less bars are available.
        """
        
        raise NotImplementedError("Should implement get_latest_bars()")
        
    @abstractmethod
    def update_bars(self):
        """
        Pushes the latest bar to the latest symbol structure
        for all symbols in the symbol list.
        """
        raise NotImplementedError("Should implement update_bars()")
    
class DataHandlerSQL(DataHandler):
    
    def __init__(self, db_host = 'localhost', db_user = 'root', db_passwd = '1234', 
                 db_name = 'securities_master', charset_type = 'utf8'):
        self.db_host = db_host
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name
        self.charset_type = charset_type
        
        self.mysql = mysql.Mysql(db_host, db_user, db_passwd, db_name, charset_type)
        self.mysql.open_conn()
    
    def get_all_symbols(self):
        select_columns = 'id_A'
        table_name = 'data_security'
        num_symbols = self.mysql.select(select_columns, table_name)
        id_symbol_tmp = self.mysql.cursor.fetchmany(num_symbols)
        id_symbols = []
        for id_tmp in id_symbol_tmp:
            id_tmp = str(id_tmp)
            id_symbols.append(id_tmp[4:10])
        return id_symbols
            
    def get_latest_bars(self, symbol, N=1):
        pass
    

    def update_bars(self, symbols):
        spider_engine = spider.Spider()
        for symbol in symbols:
            max_date = self.mysql.select_where('max(date)', 'daily_price', 'id_security', symbol)
            if max_date == 'NULL':
                print(symbol+' was not included in SQL...\n')
                
                
            
        
if __name__ == '__main__':
    print(datetime.datetime.now())
    print(' is pouring into MySQL...\n')
        