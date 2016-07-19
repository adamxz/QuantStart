'''
Created on Jul 18, 2016

@author: adam
'''

import datetime

from Toolbox.data import DataHandlerSQL
from Toolbox import portfolio
from Toolbox import position
from Toolbox.Configure import ConfContext

class context(object):
    '''
    context 
    portfolio
    '''
    
    def __init__(self, starting_date = ConfContext.default_starting_date):
        self.starting_date = starting_date
        positions = position.Position()
        self.portfolio = portfolio.Portfolio(positions, starting_cash = 10000.0)
        self.current_dt = self.starting_date
        self.universe = []
        
    def set_universe(self, securities):
        self.universe = securities
        
    def update_date(self):
        if self.current_dt.weekday() < 4:
            self.current_dt = self.current_dt + datetime.timedelta(days=1)
        elif self.current_dt.weekday() == 4:
            while self.current_dt.weekday() != 0:
                self.current_dt = self.current_dt + datetime.timedelta(days=1)
        
