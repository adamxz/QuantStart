'''
Created on Jul 17, 2016

@author: adam
'''

from enum import Enum

class OrderStatus(Enum):
    #未成交
    open = 0
    #部分成交
    filled = 1
    #已撤销
    canceled = 2
    #交易所已拒绝
    rejected = 3
    #全部成交
    held = 4
    
class OrderStyle(object):
    pass
    
class Order(object):
    '''
    status 状态, 一个OrderStatus值
    add_time 订单添加时间, datetime.datetime对象
    is_buy bool值, 买还是卖
    amount 下单数量, 不管是买还是卖, 都是正数
    filled 已经成交的股票数量, 正数
    security 股票代码
    order_id 订单ID
    price 平均成交价格, 已经成交的股票的平均成交价格(一个订单可能分多次成交)
    avg_cost 卖出时表示下卖单前的此股票的持仓成本, 用来计算此次卖出的收益. 买入时表示此次买入的均价(等同于price).
    '''


    def __init__(self):
        '''
        买卖股票。调用成功后, 您将可以调用get_open_orders取得所有未完成的交易, 也可以调用cancel_order取消交易
        '''
        
        pass
        
        
    def order(self, security, volumn, style = None):
        '''
        买卖股票。调用成功后, 您将可以调用get_open_orders取得所有未完成的交易, 也可以调用cancel_order取消交易
        '''
        
        self.security = security
        self.volumn = volumn
        self.style = style
        
    def order_target(self, security, volumn, style = None):
        '''买卖股票, 使最终股票的数量达到指定的amount'''
        
        self.security = security
        self.volumn = volumn
        self.style = style
        
    def order_value(self, security, volumn, style = None):
        '''买卖价值为value的股票'''
        
        self.security = security
        self.volumn = volumn
        self.style = style
        
    def cancle_order(self, order):
        '''取消订单'''
        
        pass
        
    def get_open_orders(self):
        '''
        获得当天的所有未完成的订单
        参数: 无
        返回： 返回一个dict, key是order_id, value是Order对象
        '''
        
        pass
    
    def get_orders(self):
        '''
        获取当天的所有订单
        参数: 无
        返回: 返回一个dict, key是order_id, value是Order对象
        '''
        
        pass
    
    def get_trades(self):
        '''
        获取当天的所有成交记录, 一个订单可能分多次成交
        参数: 无
        返回: 返回一个dict, key是trade_id, value是Trade对象
        '''
        
        pass
    
    


        
          
        