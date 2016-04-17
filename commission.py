# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:31:13 2016

@author: wangmeng70
"""

class Commission():
    """
    Calculate the commission fee from various brokers.
    stamp: 印花税
    transfer: 过户费
    brokerage: 券商佣金
    """
    
    def __init__(self, stamp = 0.001, transfer = 0.0006, brokerage = 0.00025):
        self.stamp = stamp
        self.transfer = transfer
        self.brokerage = brokerage
    
    # Calculate the fee when buying stocks.
    def commission_buy(self, shares, price):
        stamp_fee = 0
        transfer_fee = self.transfer * shares
        brokerage_fee = max(self.brokerage * shares * price, 5)
        fee_buy = stamp_fee + transfer_fee + brokerage_fee
        return fee_buy
    
    # Calculate the fee when selling stocks.
    def commission_sell(self, shares, price):
        stamp_fee = self.stamp * shares * price
        transfer_fee = self.transfer * shares
        brokerage_fee = max(self.brokerage * shares * price, 5)
        fee_sell = stamp_fee + transfer_fee + brokerage_fee
        return fee_sell

# 国金证券交易费        
class CommissionGuojin(Commission):
    def __init__(self, stamp = 0.001, transfer = 0.0006, brokerage = 0.00025):
        Commission.__init__(stamp, transfer, brokerage)

class CommissionHuatai(Commission):
    def __init__(self, stamp = 0.001, transfer = 0.0006, brokerage = 0.0002):
        self.stamp = stamp
        self.transfer = transfer
        self.brokerage = brokerage