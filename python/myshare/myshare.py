# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import time

def get_data_print():
    #data = ts.get_hist_data("601066", start="2020-10-01", end="2020-10-29")
    #data = data.sort_values(by=["date"], ascending=True)
    #data = ts.get_realtime_quotes('601066')
    pd.set_option('display.max_columns', None)
    formatSpace = '  '
    for num in range(0,300):
        rtData = ts.get_realtime_quotes(['sh', 'sz', '600893','600398', '000966']) 
        rtDataFormart = rtData[['code','time','open', 'pre_close','price','bid','ask','volume','amount','date']]

        myAccountleft   = 44009.74
        investCount     = 100000.00
        stockName       = ('hfdl', 'hlzj', 'cydl', '', '')
        shareCount      = (500.00, 2600.00, 1200.00, 0.00, 0.00)
        currentPrice    = [0.00, 0.00, 0.00, 0.00, 0.00]
        preClosePrice   = [0.00, 0.00, 0.00, 0.00, 0.00]
        vibratePrecent  = [0.00, 0.00, 0.00, 0.00, 0.00]
        TotalShare      = 0.00
        ToadyBenefit    = 0.00
        TotalBenifit    = 0.00

        #if num == 0 :
        #    print(rtDataFormart)
        arrays = pd.DataFrame(rtDataFormart.to_numpy())
        currentTime     =  arrays[1][1]
        currentDate     =  arrays[9][1]
        
        print(currentTime, end=' ')
        for i in range (0,3):
            print(stockName[i], end='')
            currentPrice[i]   = float(arrays[4][i+2])
            preClosePrice[i]  = float(arrays[3][i+2])
            vibratePrecent[i] = (currentPrice[i] - preClosePrice[i])/preClosePrice[i]
            TotalShare       += currentPrice[i]*shareCount[i]
            ToadyBenefit     += (currentPrice[i] - preClosePrice[i]) * shareCount[i]
            if(vibratePrecent[i] < 0.0):
                print ('%s %s %s' % ("\033[0;32;40m", '{:.2f}%'.format(vibratePrecent[i]*100), "\033[0m"), end=' ')  #green
            else:
                print ('%s %s %s' % ("\033[0;31;40m", '{:.2f}%'.format(vibratePrecent[i]*100), "\033[0m"), end=' ')  #red
            print(formatSpace, end='')
        TotalShare           += myAccountleft
        TotalBenifit          = TotalShare - investCount
        print("pro", end='')
        if(ToadyBenefit < 0.0):
            print ('%s %s %s' % ("\033[0;32;40m", '{:.2f}'.format(ToadyBenefit), "\033[0m"), end='')  #green
        else:
            print ('%s %s %s' % ("\033[0;31;40m", '{:.2f}'.format(ToadyBenefit), "\033[0m"), end='')  #red
        if(TotalBenifit < 0.0):
            print ('%s %s %s' % ("\033[0;32;40m", '{:.2f}'.format(TotalBenifit), "\033[0m"))  #green
        else:
            print ('%s %s %s' % ("\033[0;31;40m", '{:.2f}'.format(TotalBenifit), "\033[0m"))  #red
        
        #print(currentTime,  stockName[0], '{:.2f}%'.format(vibratePrecent[0]*100), formatSpace ,\
        #                    stockName[1], '{:.2f}%'.format(vibratePrecent[1]*100), formatSpace ,\
        #                    stockName[2], '{:.2f}%'.format(vibratePrecent[2]*100), formatSpace ,\
        #                    stockName[3], '{:.2f}%'.format(vibratePrecent[3]*100), formatSpace ,\
        #                    stockName[4], '{:.2f}%'.format(vibratePrecent[4]*100), formatSpace ,\
        #                    'pro {:.2f}'.format(ToadyBenefit), '{:.2f}'.format(TotalBenifit))
        time.sleep(5)

        # write result to file per ten times
        if num%10 == 9:
            fileName = currentDate + ".txt"
            with open(fileName,"a") as file:
                file.write(str(arrays[1][1])             + formatSpace + \
                    str(round(TotalShare     , 2))       + formatSpace + \
                    str(round(vibratePrecent[0]*100, 2)) + formatSpace + \
                    str(round(vibratePrecent[1]*100, 2)) + formatSpace + \
                    str(round(vibratePrecent[2]*100, 2)) + formatSpace + \
                    str(round(vibratePrecent[3]*100, 2)) + formatSpace + \
                    str(round(vibratePrecent[4]*100, 2)) + formatSpace + \
                    str(round(ToadyBenefit   , 2))       + formatSpace + \
                    str(round(TotalBenifit   , 2))       + "\n")

if __name__ == "__main__":
    get_data_print()
