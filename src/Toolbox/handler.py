# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:21:33 2016

@author: adam
"""

import datetime

from Toolbox.Configure import ConfHandler


class Handler(object):
    
    
    def __init__(self, starting_date = ConfHandler.default_starting_date,
                 ending_date = ConfHandler.default_ending_date):
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.current_date = starting_date
        
    def update_date(self):
        if self.current_date.weekday() < 4:
            self.current_date = self.current_date + datetime.timedelta(days=1)
        elif self.current_date.weekday() == 4:
            while self.current_date.weekday() != 0:
                self.current_date = self.current_date + datetime.timedelta(days=1)
        
        if self.current_date <= self.ending_date:
            return True
        else:
            return False
    