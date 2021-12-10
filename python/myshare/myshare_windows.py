# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import time, os

def print_with_color(var, target, flag):
    if(var < target):
        #print ('%s%s%s%s' % ("\033[32m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #green
        print ('%s%s%s%s' % ("\033[34m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #blue
    else:
        print ('%s%s%s%s' % ("\033[31m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #red

def get_data_print(_):
    pd.set_option('display.max_columns', None)
    currentPrice    = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    preClosePrice   = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    vibratePrecent  = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    stockName       = [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' ]
    TotalShare      = 0.00
    ToadyBenefit    = 0.00
    TotalBenifit    = 0.00
    rtData          = []
    try:
        rtData = ts.get_realtime_quotes(stockCode) 
    except Exception as ex:
        print("Oops!  Exception<<%s>>detected, Will ry again couple of seconds later... "%ex)
        return

    rtDataFormart = rtData[['code','time','open', 'pre_close','price','bid','ask','volume','amount','date', 'name']]

    arrays = pd.DataFrame(rtDataFormart.to_numpy())
    currentTime     =  arrays[1][1]
    currentDate     =  arrays[9][1]

    print(currentTime, '', end='')
    i = 0
    while stockCode[i]   != '':
        currentPrice[i]   = float(arrays[4][i])
        preClosePrice[i]  = float(arrays[3][i])
        stockName[i]      = arrays[10][i]

        vibratePrecent[i] = (currentPrice[i] - preClosePrice[i])/preClosePrice[i]
        TotalShare       += currentPrice[i]*shareCount[i]
        ToadyBenefit     += (currentPrice[i] - preClosePrice[i]) * shareCount[i]

        if(i < 1):
            #print_with_color(currentPrice[i], preClosePrice[i], '') # output szzs as refer
            print('{:.0f}'.format(currentPrice[i]), end='')
            print_with_color(currentPrice[i] - preClosePrice[i], 0.0, '') # output szzs as refer
        else:
            #print_with_color(currentPrice[i], preClosePrice[i], '_') # output currentPrice with color
            if (countforPrint != 0):
                print('{:.2f}'.format(currentPrice[i]), end='') #output current Price
                print_with_color(vibratePrecent[i]*100, 0.0, '%')
            else:
                print(stockName[i], ' ', end='')
        print('  ',end='')
        i = i + 1
    #countforPrint = 0
    TotalShare             += myAccountleft
    TotalBenifit            = TotalShare - investCount
    print("pro ", end='')
    print_with_color(ToadyBenefit, 0.0, '')
    print(' ' , end='')
    print_with_color(TotalBenifit, 0.0, '')
    print() # new line
    time.sleep(4)


if __name__ == "__main__":
    # setting init account information
    print("starting...")
    print("current proxy was: ",os.getenv('http_proxy'))
    result = os.system('ping www.baidu.com -n 2')
    if result != 0:
        os.environ['http_proxy'] = 'http://cnhanab-proxy001.china.nsn-net.net:8080'
        print("change proxy to: ",os.getenv('http_proxy'))
    myAccountleft   = 149.78
    investCount     = 100000.00
    stockCode       = ('sh'  , '603893' ,  '603606'  ,   '300017'       ,   '300364'         ,   ''       ,   ''       )
    shareCount      = (0.00  ,  200.00  ,  400.00    ,   5900.00        ,    0.00         ,   0.00     ,   0.00     )
    countforPrint   = 0.0
    for i in range(2048):
        get_data_print( countforPrint )
        countforPrint = countforPrint + 1

