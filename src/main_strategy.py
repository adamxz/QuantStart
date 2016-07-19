'''
Created on Jul 19, 2016

@author: adam
'''

from Toolbox.initialization import context

def initialize():
    '''
    初始化函数
    '''
    securities = ['sh600000']
    context = context.context()
    context.set_universe(securities)
    
    
def handle_data():
    pass

if __name__ == '__main__':