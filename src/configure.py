'''
Created on Jul 6, 2016

@author: adam
'''

# MySQL connection
db_host = 'localhost'
db_user = 'root'
db_passwd = '1234'
db_name = 'securities_master'
charset_type = 'utf8'

# security_initial_csv
# Get basic information for securities and pouring into csv file

csv_url = '/home/adam/workspace/QuantStart/tmp/securities_list.csv'
csv_header = 'id,name,abbr,state_public,industry,area,capital_registered(billion),date_IPO,price_IPO,shares_notcurrent,shares_limited,shares_current,date_created,date_updated\n'
basic_url = 'http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code='
share_url = 'http://f10.eastmoney.com/f10_v2/CapitalStockStructure.aspx?code='
prefix = range(7)
prefix_str = ['sh', 'sh', 'sz', 'sz', 'sz', 'sz', 'sz']
prefix_ini = [600000, 603000, 0, 1696, 1896, 2000, 300000]
prefix_max = [1999, 999, 999, 0, 0, 999, 999]


# security_initial_sql
# Basic information pouring into MySQL from csv file

datasecurity_table_column_num = 14
column_str = 'id_A,name,abbreviation,state_public,industry,area,capital_registered,date_IPO,price_IPO,shares_notcurrent,shares_limited,shares_current,date_created,date_updated'


# dailyprice_initial_sql

dailiprice_table_name = 'daily_price'
dialyprice_table_column_num = 10
dailyprice_test_table_name = 'daily_price_test'
price_url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/\
stockid/%s.phtml?year=%d&jidu=%d'


# dailyprice_update


