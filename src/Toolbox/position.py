'''
Created on Jul 12, 2016

@author: adam
'''


class Position(object):
    '''
    total_volumn 总持有股票数量, 包含可卖出和不可卖出部分
    sellable_volumn 可卖出数量
    price 最新价格
    avg_cost 每只股票的持仓成本, 买入股票的加权平均价, 计算方法是: 
    (buy_volume1 * buy_price1 + buy_volume2 * buy_price2 + …) / (buy_volume1 + buy_volume2 + …) 
    每次买入后会调整avg_cost, 卖出时avg_cost不变. 这个值也会被用来计算浮动盈亏.
    security 股票代码
    '''


    def __init__(self, security):
        '''
        Constructor
        '''
        self.total_volumn = 0
        self.sellable_volumn = 0
        self.price = 0.0
        self.avg_cost = 0.0
        self.security = security
        
    def calculate_avg_cost(self, trade_volumn, trade_price, order_style):
        self.avg_cost = (self.avg_cost * self.total_volumn + trade_price * trade_volumn * order_style) \
        / (self.total_volumn + trade_volumn * order_style)
        
    def update_trade(self, trade_volumn, trade_price, order_style):
        if order_style == 1:
            self.sellable_volumn = self.total_volumn
            self.total_volumn += trade_volumn
        elif order_style == -1:
            self.total_volumn -= trade_volumn
            self.sellable_volumn = self.total_volumn
        self.avg_cost = self.calculate_avg_cost(trade_volumn, trade_price, order_style)
        
    def update_price(self, data, date):
        tmp = data.get_latest_bars(self.security, date)
        self.price = tmp[0][4] # 前一天的收盘价
        