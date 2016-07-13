'''
Created on Jul 10, 2016

@author: adam
'''



import configure
from data import DataHandlerSQL

if __name__ == '__main__':
    data_engine = DataHandlerSQL()
    symbols = data_engine.get_all_symbols()
    a = data_engine.get_latest_bars(symbols[0], '2016-01-01', 10)
    print(a)