'''
Created on Jul 12, 2016

@author: adam
'''

class Portfolio(object):
    '''
    cash 当前持有的现金
    positions 当前持有的股票(包含不可卖出的股票), 一个dict, key是股票代码, value是Position对象
    positions 当前持有的不可卖出的股票(比如在A股T+1市场, 今天购票的股票), 并没有考虑股票今天是否停牌, 一个dict, key是股票代码, value是Position对象.
    starting_cash 初始资金
    portfolio_value 当前持有的股票和现金的总价值
    positions_value 当前持有的股票的总价值
    capital_used 已使用的现金
    returns 当前的收益比例, 相对于初始资金
    '''


    def __init__(self, positions, events, start_date, starting_cash = 10000.0):
        '''
        Constructor
        '''
        self.cash = starting_cash
        self.positions = positions
        self.starting_cash = starting_cash
        self.portfolio_value = starting_cash
        self.positions_value = 0.0
        self.capital_used = 0.0
        self.returns = 0.0