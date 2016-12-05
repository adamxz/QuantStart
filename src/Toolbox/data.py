'''
Created on Jul 6, 2016

@author: adam
'''

import datetime
from abc import ABCMeta, abstractmethod

from Toolbox.Configure import ConfData as cd
from Toolbox import mysql, spider

class DataHandler(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_all_securities(self):
        
        raise NotImplementedError("Should implement get_all_securities()")
    
    @abstractmethod
    def get_latest_bars(self, symbol, date, N = 1):
        """
        Returns the last N bars from the latest security_list,
        or fewer if less bars are available.
        """
        
        raise NotImplementedError("Should implement get_latest_bars()")
        
    @abstractmethod
    def update_bars(self):
        """
        Pushes the latest bar to the latest security structure
        for all securities in the symbol list.
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
        
        self.today = datetime.date.today()
        self.year_today = self.today.year
        self.quarter_today = self.today.month % 4
    
    def get_all_symbols(self):
        select_columns = 'id_security'
        table_name = 'data_security'
        num_securities = self.mysql.select(select_columns, table_name)
        id_symbol_tmp = self.mysql.cursor.fetchmany(num_securities)
        id_symbols = []
        for id_tmp in id_symbol_tmp:
            id_tmp = str(id_tmp)
            id_symbols.append(id_tmp[2:10])
        return id_symbols
            
    def get_latest_bars(self, symbol, date, N=1):
        '''
        获取当前日期最后N条数据
        当前日期需要确定
        '''
        date_str = str(date)
        # 注意是date<'%s'，是为了避免未知函数，今天只能知道昨天的数据
        select_str = "select id_security, date, price_open, price_high, price_close, \
        price_low, volumn, amount, factor_adj from daily_price where id_security='%s' \
        and date<'%s' order by date desc limit %d" %(symbol, date_str, N)
        num_res = self.mysql.select_universe(select_str)
        res = self.mysql.cursor.fetchmany(num_res)
        return res
       

    def update_bars(self, symbols):
        spider_engine = spider.Spider()
        url_prefix = cd.price_url
        for symbol in symbols:
            print(symbol + ' is updating...')
            max_date_tmp = self.mysql.select_where('max(date)', 'daily_price', 'id_security', "'"+symbol+"'")
            if max_date_tmp[0][0]:               
                max_date = max_date_tmp[0][0].strftime('%Y-%m-%d')
                print(symbol + ' adds from ' + max_date + '...')
                year_start = int(max_date[:4])
            else:
                print(symbol+' was not included in SQL...')
                url = url_prefix %(symbol, self.year_today, self.quarter_today)
                soup = spider_engine.soup_read(url)
                soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。
                year_start = soup_table[0].find_all('option')[-5].string # 获得年份
                if year_start < '1990':
                    year_start = self.year_today  
                max_date = str(year_start) + '-01-01'
            year_range = range(self.year_today, int(year_start)-1, -1)
            quarter_range = range(4, 0, -1)
            for year in year_range:
                for quarter in quarter_range:
                    url = url_prefix % (symbol, year, quarter)
                    soup = spider_engine.soup_read(url)
                    soup_table = soup.find_all(align = 'center') #从下标1开始，每8个一组数据。                   
                    for i in range(9,len(soup_table),8):
                        insert_item = "'" + symbol + "', "
                        insert_date = ''
                        if year > 2006:
                            insert_date = soup_table[i].a.string[7:17]
                        elif year == 2006:
                            if quarter > 2:
                                insert_date = soup_table[i].a.string[7:17]
                            elif quarter == 2:
                                if soup_table[i].a:
                                    insert_date = soup_table[i].a.string[7:17]
                                else:
                                    insert_date = soup_table[i].string[8:18]
                            else:
                                insert_date = soup_table[i].string[8:18]
                        else:
                            insert_date = soup_table[i].string[8:18]
                        if insert_date <= max_date:
                            break                        
                        insert_item = insert_item + "'" + insert_date + "'"
                        for j in range(1,8):
                            insert_item = insert_item + ", '"+ soup_table[i+j].string + "'"
                        self.mysql.insert(cd.price_table_name, cd.price_insert_columns, insert_item)
    
    def _destruction_(self):
        self.mysql.close_conn()        