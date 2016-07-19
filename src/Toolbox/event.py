# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:44:04 2016

@author: wangmeng70
"""

import commission as cs

class Event(object):
    """
    Event is base class providing an interface for all subsequent 
    (inherited) events, that will trigger further events in the 
    trading infrastructure.   
    """
    pass

class OrderEvent(Event):
    """
    买卖订单
    status 状态, 一个OrderStatus值
    add_time 订单添加时间, datetime.datetime对象
    is_buy bool值, 买还是卖
    amount 下单数量, 不管是买还是卖, 都是正数
    filled 已经成交的股票数量, 正数
    security 股票代码
    order_id 订单ID
    price 平均成交价格, 已经成交的股票的平均成交价格(一个订单可能分多次成交)
    avg_cost 卖出时表示下卖单前的此股票的持仓成本, 用来计算此次卖出的收益. 买入时表示此次买入的均价(等同于price).
    """
    
    def __init__(self):
        pass

class TradeEvent(Event):
    """
    订单的一次交易记录,一个订单可能分多次交易.
    time 交易时间, datetime.datetime对象
    amount 交易数量
    price 交易价格
    trade_id 交易记录id
    order_id 对应的订单id
    """
    
    def __init__(self):
        pass
    