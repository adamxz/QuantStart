'''
Created on Jul 12, 2016

@author: adam
'''

class Position(object):
    '''
    total_amount 总持有股票数量, 包含可卖出和不可卖出部分
    sellable_amount 可卖出数量
    price 最新价格
    avg_cost 每只股票的持仓成本, 买入股票的加权平均价, 计算方法是: 
    (buy_volume1 * buy_price1 + buy_volume2 * buy_price2 + …) / (buy_volume1 + buy_volume2 + …) 
    每次买入后会调整avg_cost, 卖出时avg_cost不变. 这个值也会被用来计算浮动盈亏.
    security 股票代码
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.total_volumn = 0
        self.sellable_volumn = 0
        self.price = 0.0
        self.avg_cost = 0
        self.security = ''
        
    def calculate_avg_cost(self, buy_volumn, buy_price):
        self.avg_cost = (self.avg_cost * self.total_volumn + buy_volumn * buy_price) / (self.total_volumn + buy_volumn)