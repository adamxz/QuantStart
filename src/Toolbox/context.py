'''
Created on Jul 18, 2016

@author: adam
'''

import datetime

from Toolbox.data import DataHandlerSQL
from Toolbox.portfolio import Portfolio
from Toolbox.position import Position
from Toolbox.Configure import ConfContext

class Context(object):
    '''
    context 
    portfolio
    '''
    
    def __init__(self, current_dt, 
                 starting_cash = ConfContext.default_starting_cash):
        self.current_dt = current_dt
        self.starting_cash = starting_cash
        self.portfolio = Portfolio(self.starting_cash)

        self.universe = []
        
    def set_universe(self, securities):
        self.universe = securities
    
        
