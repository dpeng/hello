# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import configparser, time, os

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
    print("pro ", end='')
    print_with_color(ToadyBenefit, 0.0, '')
    print(' ' , end='')
    print_with_color(TotalShare, 0.0, '')
    print() # new line
    time.sleep(4)


if __name__ == "__main__":
    # setting init account information
    print("starting...")
    config = configparser.ConfigParser()
    config.read("./config.ini")
    http_proxy      = config.get("DEFAULT", "http_proxy")
    code1           = config.get("CODESHARE", "code1")
    code2           = config.get("CODESHARE", "code2")
    code3           = config.get("CODESHARE", "code3")
    code4           = config.get("CODESHARE", "code4")
    code5           = config.get("CODESHARE", "code5")
    code6           = config.get("CODESHARE", "code6")
    code7           = config.get("CODESHARE", "code7")
    code8           = config.get("CODESHARE", "code8")
    share1          = float(config.get("CODESHARE", "share1"))
    share2          = float(config.get("CODESHARE", "share2"))
    share3          = float(config.get("CODESHARE", "share3"))
    share4          = float(config.get("CODESHARE", "share4"))
    share5          = float(config.get("CODESHARE", "share5"))
    share6          = float(config.get("CODESHARE", "share6"))
    share7          = float(config.get("CODESHARE", "share7"))
    share8          = float(config.get("CODESHARE", "share8"))
    os.environ['http_proxy'] = http_proxy
    
    stockCode       = ['sh' , code1 , code2 , code3 , code4 , code5 , code6 , code7 , code8 ]
    shareCount      = [0.00 , share1, share2, share3, share4, share5, share6, share7, share8]
    countforPrint   = 0.0
    for i in range(2048):
        get_data_print( countforPrint )
        countforPrint = countforPrint + 1

