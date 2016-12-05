'''
Created on Jul 19, 2016

@author: adam
'''

import datetime

from Toolbox.context import Context
from Toolbox.data import DataHandlerSQL
from Toolbox.handler import Handler


starting_date = datetime.date.today() - datetime.timedelta(days = 365)
ending_date = datetime.date.today()


def initialize(context):
    '''
    初始化函数
    '''
    securities = ['sh600000']
    context.set_universe(securities)
    
def pre_handle():
    pass
    
    
def handle_data(context, data_engine):
    res = data_engine.get_latest_bars(context.universe[0],context.current_dt)
    context.portfolio.update_portfolio(context.universe[0],100,float(res[0][4]),1)
    

def post_handle(context):
    pass
    
    
    

if __name__ == '__main__':
    handler = Handler(starting_date, ending_date)
    context = Context(handler.current_date)
    initialize(context)
    
    data_engine = DataHandlerSQL()
    while handler.update_date():
        handle_data(context, data_engine)
    
    
    