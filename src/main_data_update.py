'''
Created on Jul 10, 2016

@author: adam
'''


from Toolbox.data import DataHandlerSQL


if __name__ == '__main__':
    data_engine = DataHandlerSQL()
    symbols = data_engine.get_all_symbols()
    data_engine.update_bars(symbols)
