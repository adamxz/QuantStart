'''
Created on Jul 12, 2016

@author: adam
'''

import data

class SecurityUnitData(object):
    '''
    security
    open 时间段开始时价格
    close 时间段结束时价格
    low 最低价
    high 最高价
    volume 成交的股票数量
    amount 成交的金额
    factor_adj 前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: close/factor
    '''


    def __init__(self, security, data, date):
        '''
        Constructor
        '''
        self.security = security
        unit_data = data.get_latest_bars(security, date)[0]
        self.open = unit_data.open
        self.high = unit_data.high
        self.close = unit_data.close
        self.low = unit_data.low
        self.volumn = unit_data.volumn
        self.amount = unit_data.amount
        self.factor = unit_data.factor_adj