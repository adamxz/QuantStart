'''
Created on Jul 12, 2016

@author: adam
'''

from Toolbox.position import Position

class Portfolio(object):
    '''
    cash 当前持有的现金
    positions 当前持有的股票(包含不可卖出的股票), 一个dict, key是股票代码, value是Position对象
    starting_cash 初始资金
    portfolio_value 当前持有的股票和现金的总价值
    positions_value 当前持有的股票的总价值
    cash_used 已使用的现金
    returns 当前的收益比例, 相对于初始资金
    '''


    def __init__(self, starting_cash = 10000.0):
        '''
        Constructor
        '''
        self.cash = starting_cash
        self.starting_cash = starting_cash
        self.portfolio_value = starting_cash
        self.positions_value = 0.0
        self.cash_used = 0.0
        self.return_ratio = 0.0
        self.positions = {}
        
    def update_portfolio(self, security, trade_volumn, trade_price, order_style):
        if security not in self.positions:
            self.positions[security] = Position(security)
            
        self.positions[security].update_trade(trade_volumn, trade_price, order_style)
        self.positions_value += self.positions[security].total_volumn * self.positions[security].price
        self.cash = self.cash - trade_volumn * trade_price * order_style
        self.portfolio_value += self.positions_value + self.cash
        self.returns = (self.portfolio_value - self.starting_cash) / self.starting_cash
        