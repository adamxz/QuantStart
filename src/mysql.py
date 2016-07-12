'''
Created on Jun 26, 2016

@author: adam
'''

import pymysql

class Mysql(object):
    '''
    classdocs
    '''


    def __init__(self, db_host = 'localhost', db_user = 'root', db_passwd = '1234',\
                 db_name = 'securities_master', charset_type = 'utf8'):
        '''
        Constructor
        '''
        self.db_host = db_host 
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name
        self.charset_type = charset_type 
        
    
    def open_conn(self):
        try:
            self.conn = pymysql.connect(host = self.db_host, user = self.db_user, passwd = self.db_passwd,\
                                   db = self.db_name,charset = self.charset_type)
        except Exception:
            print(Exception.args[0])
        else:
            self.cursor = self.conn.cursor()
            
    
    def insert(self, table_name, insert_columns, insert_values):
        # column_value_str = ('%s, ' * column_num)[:-2]
        insert_str = "insert into %s (%s) values (%s)" %(table_name, insert_columns, insert_values)
        self.cursor.execute(insert_str)
        
    def select(self, select_columns, table_name):
        select_str = 'select %s from %s' %(select_columns, table_name)
        return self.cursor.execute(select_str)
    
    def select_universe(self, select_str):
        return self.cursor.execute(select_str)
    
    def select_where(self, select_columns, table_name, where_column, where_value):
        select_str = 'select %s from %s where %s = %s' %(select_columns, table_name, where_column, where_value)
        self.cursor.execute(select_str)
        return self.cursor.fetchall()
        
        
    def close_conn(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        
if __name__ == '__main__':
    pass