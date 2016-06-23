# -*- coding:utf-8 -*-
# @Date:2015/11/8
# @Author: Wang Meng
# @Description: Creating the csv file of security data from http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code=sh600000
# @Description2: The share information comes from http://f10.eastmoney.com/f10_v2/CapitalStockStructure.aspx?code=sh600000
# @The json url is: http://stockdata.stock.hexun.com/gszl/data/jsondata/jbgk.ashx?groupqzaby=1&count=1000&stateType=up&titType=1&page=1&callback=hxbase_json15

# @Attention: This script should be run every month.

#剩余工作：空格消除（如万  科A）、异常处理、logging
#网页和脚本编码不一致，需要编码转换
#使中文可以正常显示
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )

import logging
import socket
#from urllib2 import Request, urlopen
from urllib import request
from bs4 import BeautifulSoup
import pypinyin
import csv
import datetime
import time

'''return the soup and state. 
if the state is true, there is data for the security; 
else, there is no data for the id.'''
def soup_read(url, file_csv):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    header = {'User-Agent': user_agent}
    req = Request(url, headers = header)
    try:
        response = urlopen(req)
        page = response.read()
    except socket.error:
        logging.warning('%s is paused...' % url_postfix)
        time.sleep(1)
        response = urlopen(req)
        page = response.read()
    response.close()
    soup = BeautifulSoup(page)
    if soup.body.div.div.get('class') == ['noData']:
        return (soup, False)
    else:
        return (soup, True)

'''write the basic information into the csv file.
the url is http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code=''' 
def basic_info_csv(soup, file_csv):
    flag = soup.find(text = '该公司暂无基本资料')
    if flag:
        state_public = 0
        id_A = '0'
        name = '0'
        abbr = '0'
        industry = '0'
        area = '0'
        capital_registered = '0'
        date_IPO = '0'
        price_IPO = '0'
    else:
        state_public = 1
    if state_public:
        content_all = soup.find_all(class_='tips-fieldnameL')
        for content in content_all:
            if content.string == 'A股代码':
                id_A = content.find_next_sibling().string
            if content.string == 'A股简称':
                name = content.find_next_sibling().string
                name.replace(' ','')
                name_first_letter = pypinyin.pinyin(name,pypinyin.FIRST_LETTER)
                abbr = ''.join(i[0] for i in name_first_letter)
            if content.string == '所属行业':
                industry = content.find_next_sibling().string
            if content.string == '区域':
                area = content.find_next_sibling().string
            if content.string == '注册资本(元)':
                capital_registered = content.find_next_sibling().string[:-1]
            if content.string == '上市日期':
                date_IPO = content.find_next_sibling().string
                if date_IPO == '--':
                    date_IPO = '0'
            if content.string == '首日开盘价(元)':
                price_IPO = content.find_next_sibling().string
                if price_IPO == '--':
                    price_IPO = '0'
    file_csv.write(name+','+abbr+','+str(state_public)+','+industry+','+area+','+capital_registered+','+date_IPO+','+price_IPO+',')

'''write the share information into the csv file.
the url is http://f10.eastmoney.com/f10_v2/CapitalStockStructure.aspx?code='''
def share_info_csv(soup, file_csv):
    content_all = soup.find_all(class_='tips-fieldnameL')
    for content in content_all:
        if content.string == '未流通股份':
            shares_nocurrent = content.find_next_sibling().string
            if shares_nocurrent == '--':
                shares_nocurrent = '0'
            else:
                shares_nocurrent = filter(lambda ch: ch in '0123456789.', shares_nocurrent)
        if content.string == '流通受限股份':
            shares_limited = content.find_next_sibling().string
            if shares_limited == '--':
                shares_limited = '0'
            else:
                shares_limited = filter(lambda ch: ch in '0123456789.', shares_limited)
        if content.string == '已流通股份':
            shares_current = content.find_next_sibling().string
            if shares_current == '--':
                shares_current = '0'
            else:
                shares_current = filter(lambda ch: ch in '0123456789.', shares_current)
        
    now = datetime.date.today()
    file_csv.write(shares_nocurrent+','+shares_limited+','+shares_current+','+str(now)+','+str(now)+'\n')

#this is the main function
if __name__ == "__main__":
    # file preparation
    file_url = '/home/adam/workspace/QuantStart/tmp/securities_list.csv'
    file_csv = open(file_url, 'w')
    file_csv.write('id,name,abbr,state_public,industry,area,capital_registered(billion),date_IPO,price_IPO,shares_notcurrent,shares_limited,shares_current,date_created,date_updated\n')

    #url preparation
    url_ini_basic = 'http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code='
    url_ini_share = 'http://f10.eastmoney.com/f10_v2/CapitalStockStructure.aspx?code='

    prefix = range(7)
    prefix_str = ['sh', 'sh', 'sz', 'sz', 'sz', 'sz', 'sz']
    prefix_ini = [600000, 603000, 0, 1696, 1896, 2000, 300000]
    prefix_max = [1999, 999, 999, 0, 0, 776, 489]
    '''prefix_str = ['sz', 'sz', 'sz', 'sz', 'sz']
      prefix_ini = [0, 1696, 1896, 2000, 300000]
      prefix_max = [999, 0, 0, 776, 489]'''

    #Collect the basic information of the company();
  
    for i in prefix:
        logging.warning('%d is i...' % i)
        for j in range(prefix_max[i]+1):
            id_tmp = prefix_ini[i] + j
            #logging.warning('id_tmp is %d...\n' % id_tmp)
            id_tmp = '%06d' % id_tmp
            #logging.warning('id_tmp2 is %s...\n' % id_tmp)
            url_postfix = prefix_str[i]+id_tmp
            logging.warning('%s is processing...' % url_postfix)
            url = url_ini_basic + url_postfix
            url_share = url_ini_share + url_postfix
            (soup, state) = soup_read(url,file_csv)
            #if state is true, import the information into the csv file
            if state:
                file_csv.write(url_postfix+',')
                basic_info_csv(soup, file_csv)
                (soup_share, state_share) = soup_read(url_share,file_csv)
                share_info_csv(soup_share, file_csv)
    file_csv.close()