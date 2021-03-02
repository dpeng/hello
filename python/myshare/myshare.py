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
    for num in range(0,500):
        rtData = ts.get_realtime_quotes(['sh', 'sz', '002739', '002244', '600814']) 

        rtDataFormart = rtData[['code','time','open', 'pre_close','price','bid','ask','volume','amount','date']]

        if num == 0 :
            print(rtDataFormart)
        arrays = pd.DataFrame(rtDataFormart.to_numpy())
        #print(arrays)
        wddyCurrentPrice  = float(arrays[4][2])
        bjjtCurrentPrice  = float(arrays[4][3])
        hzjbCurrentPrice  = float(arrays[4][4])
        wddyPreClosePrice = float(arrays[3][2])
        bjjtPreClosePrice = float(arrays[3][3])
        hzjbPreClosePrice = float(arrays[3][4])
        currentTime       =  arrays[1][1]
        currentDate       =  arrays[9][1]

        wddyShareCount  = 1200.00
        bjjtShareCount  = 2800.00
        hzjbShareCount  = 2500.00
        myAccountleft   = 183.95
        investCount     = 50000.00

        wddyPrecent = (wddyCurrentPrice - wddyPreClosePrice)/wddyPreClosePrice
        bjjtPrecent = (bjjtCurrentPrice - bjjtPreClosePrice)/bjjtPreClosePrice
        hzjbPrecent = (hzjbCurrentPrice - hzjbPreClosePrice)/hzjbPreClosePrice

        TotalShare   = wddyCurrentPrice * wddyShareCount + \
                       bjjtCurrentPrice * bjjtShareCount + \
                       hzjbCurrentPrice * hzjbShareCount + \
                       myAccountleft
        ToadyBenefit = (wddyCurrentPrice - wddyPreClosePrice) * wddyShareCount + \
                       (bjjtCurrentPrice - bjjtPreClosePrice) * bjjtShareCount + \
                       (hzjbCurrentPrice - hzjbPreClosePrice) * hzjbShareCount
        TotalBenifit = TotalShare - investCount

        print(currentTime,  'wddy:{:.2f} {:.2f}%'.format(wddyCurrentPrice, wddyPrecent*100), formatSpace ,\
                            'bjjt:{:.2f} {:.2f}%'.format(bjjtCurrentPrice, bjjtPrecent*100), formatSpace ,\
                            'hzjb:{:.2f} {:.2f}%'.format(hzjbCurrentPrice, hzjbPrecent*100), formatSpace ,\
                            'pro:{:.2f}'.format(ToadyBenefit), '{:.2f}'.format(TotalBenifit)
            )
        time.sleep(3)

        # write result to file per ten times
        if num%10 == 9:
            fileName = currentDate + ".txt"
            with open(fileName,"a") as file:
                file.write(str(arrays[1][1]) + formatSpace + \
                    str(round(TotalShare     , 2)) + formatSpace + \
                    str(round(wddyPrecent*100, 2)) + formatSpace + \
                    str(round(bjjtPrecent*100, 2)) + formatSpace  + \
                    str(round(hzjbPrecent*100, 2)) + formatSpace  +\
                    str(round(ToadyBenefit   , 2)) + formatSpace + \
                    str(round(TotalBenifit   , 2)) + "\n")

if __name__ == "__main__":
    #print("start...", end="")
    get_data_print()
