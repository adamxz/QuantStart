'''
Created on Jul 9, 2016

@author: adam
'''

# get the history data from sina
price_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/\
stockid/%s.phtml?year=%d&jidu=%d'
price_table_name = 'daily_price'
price_insert_columns = 'id_security, date, price_open, price_high, price_close, price_low, volumn, amount, factor_adj'
