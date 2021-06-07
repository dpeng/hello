# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import time

def print_with_color(var, target, flag):
    if(var < target):
        #print ('%s%s%s%s' % ("\033[32m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #green
        print ('%s%s%s%s' % ("\033[34m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #blue
    else:
        print ('%s%s%s%s' % ("\033[31m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #red

def get_data_print():
    #data = ts.get_hist_data("601066", start="2020-10-01", end="2020-10-29")
    #data = data.sort_values(by=["date"], ascending=True)
    pd.set_option('display.max_columns', None)
    # setting init account information
    myAccountleft   = 2488.75
    investCount     = 100000.00
    stockName       = (''    , 'hydl'     , 'thkj '  , 'xzyy '   ,   'jly  '     , ''       , ''       )
    stockCode       = ('sh'  , '600744'   , '603025' , '600211'  ,   '300999'    , ''       , ''       )
    shareCount      = (0.00  ,  3200.00   ,  500.00  ,  300.00   ,    200.00     , 0.00     , 0.00     )

    for num in range(0,300):
        currentPrice    = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        preClosePrice   = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        vibratePrecent  = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        TotalShare      = 0.00
        ToadyBenefit    = 0.00
        TotalBenifit    = 0.00
        rtData = ts.get_realtime_quotes(stockCode) 
        rtDataFormart = rtData[['code','time','open', 'pre_close','price','bid','ask','volume','amount','date']]

        arrays = pd.DataFrame(rtDataFormart.to_numpy())
        currentTime     =  arrays[1][1]
        currentDate     =  arrays[9][1]

        print(currentTime, '', end='')
        #for i in range (0,5):
        i = 0
        while stockCode[i] != '':
            currentPrice[i]   = float(arrays[4][i])
            preClosePrice[i]  = float(arrays[3][i])
            vibratePrecent[i] = (currentPrice[i] - preClosePrice[i])/preClosePrice[i]
            TotalShare       += currentPrice[i]*shareCount[i]
            ToadyBenefit     += (currentPrice[i] - preClosePrice[i]) * shareCount[i]

            if(i < 1):
                print_with_color(currentPrice[i], preClosePrice[i], '') # output szzs as refer
            else:
                #print_with_color(currentPrice[i], preClosePrice[i], '_') # output currentPrice with color
                if (num % 10):
                    print('{:.2f}'.format(currentPrice[i]), end='') #output current Price
                else:
                    print(stockName[i], end='')
                print_with_color(vibratePrecent[i]*100, 0.0, '%')
            print('  ',end='')
            i = i + 1
        TotalShare           += myAccountleft
        TotalBenifit          = TotalShare - investCount
        print("pro ", end='')
        print_with_color(ToadyBenefit, 0.0, '')
        print(' ' ,end='')
        print_with_color(TotalBenifit, 0.0, '')
        print() # new line
 
        time.sleep(5)

        # write result to file per ten times
        if num%10 == 9:
            fileName = currentDate + ".txt"
            with open(fileName,"a") as file:
                file.write(str(arrays[1][1])             + '  ' + \
                    str(round(TotalShare     , 2))       + '  ' + \
                    str(round(vibratePrecent[0]*100, 2)) + '  ' + \
                    str(round(vibratePrecent[1]*100, 2)) + '  ' + \
                    str(round(vibratePrecent[2]*100, 2)) + '  ' + \
                    str(round(vibratePrecent[3]*100, 2)) + '  ' + \
                    str(round(vibratePrecent[4]*100, 2)) + '  ' + \
                    str(round(vibratePrecent[5]*100, 2)) + '  ' + \
                    str(round(ToadyBenefit   , 2))       + '  ' + \
                    str(round(TotalBenifit   , 2))       + "\n")

if __name__ == "__main__":
    get_data_print()
