# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import configparser, time, os
import colorama

def load_config_info( ):
    config = configparser.ConfigParser()
    config.read("./config.ini")
    http_proxy      = config.get("DEFAULT", "http_proxy")
    myAccountleft   = float(config.get("DEFAULT", "myAccountleft"))
    investCount     = float(config.get("DEFAULT", "investCount"))
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
    return (myAccountleft, investCount, stockCode, shareCount)

def print_with_color(var, target, flag):
    if(var < target):
        #print ('%s%s%s%s' % ("\033[32m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #green
        print ('%s%s%s%s' % ("\033[34m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #blue
    else:
        print ('%s%s%s%s' % ("\033[31m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #red

def get_data_print(countforPrint, previousTodayBenifit):
    pd.set_option('display.max_columns', None)
    currentPrice    = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    preClosePrice   = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    vibratePrecent  = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    stockName       = [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' ]
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

    i = 0
    while stockCode[i]   != '':
        currentPrice[i]   = float(arrays[4][i])
        preClosePrice[i]  = float(arrays[3][i])
        stockName[i]      = arrays[10][i]

        vibratePrecent[i] = (currentPrice[i] - preClosePrice[i])/preClosePrice[i]
        TotalShare       += currentPrice[i]*shareCount[i]
        ToadyBenefit     += (currentPrice[i] - preClosePrice[i]) * shareCount[i]
        i = i + 1
    if (previousTodayBenifit != ToadyBenefit):
        i = 0
        print(currentTime, '', end='')
        while stockCode[i]   != '':
            if(i < 1):
                #print_with_color(currentPrice[i], preClosePrice[i], '') # output szzs as refer
                print('{:.0f}'.format(currentPrice[i]), end='')
                print_with_color(currentPrice[i] - preClosePrice[i], 0.0, ' ') # output szzs as refer
            else:
                #print_with_color(currentPrice[i], preClosePrice[i], '_') # output currentPrice with color
                if (countforPrint != 0):
                    print('{:.2f}'.format(currentPrice[i]), end='') #output current Price
                    print_with_color(vibratePrecent[i]*100, 0.0, '%')
                else:
                    print(stockName[i], ' ', end='')
                print('  ',end='')
            i = i + 1 
        TotalShare             += myAccountleft
        TotalBenifit            = TotalShare - investCount
        print("pro ", end='')
        print_with_color(ToadyBenefit, 0.0, '')
        print(' ' , end='')
        print_with_color(TotalBenifit, 0.0, '')
        print() # new line
    time.sleep(4)
    return ToadyBenefit


if __name__ == "__main__":
    # setting init account information
    colorama.init(autoreset=True)
    print("tushare version: ", ts.__version__)
    print("pandas version: ", pd.__version__)

    (myAccountleft, investCount, stockCode, shareCount) = load_config_info( )

    countforPrint   = 0.0
    previousTodayBenifit    = 0.0
    for i in range(2048):
        previousTodayBenifit = get_data_print(countforPrint, previousTodayBenifit)
        countforPrint = countforPrint + 1

