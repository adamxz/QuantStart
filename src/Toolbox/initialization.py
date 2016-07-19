'''
Created on Jul 18, 2016

@author: adam
'''

import datetime

from Toolbox.data import DataHandlerSQL
from Toolbox import portfolio
from Toolbox import position

class context(object):
    '''
    context 
    portfolio
    '''
    
    def __init__(self):
        self.starting_date = datetime.date.today() - datetime.timedelta(days = 365)
        positions = position.Position()
        self.portfolio = portfolio.Portfolio(positions, starting_cash = 10000.0)
        self.current_dt = self.starting_date
        self.universe = []
        
    def set_universe(self, securities):
        self.universe = securities
        
        
def initialize():
    '''
    初始化函数
    '''
    securities = ['sh600000']
    set_universe(securities)
    
    
def handle_data():
    pass