# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare.stock.indictor as idx
import tushare as ts
import pandas as pd
import numpy as np
import time

def get_data_print():
    #data = ts.get_hist_data("601066", start="2020-10-01", end="2020-10-29")
    #data = data.sort_values(by=["date"], ascending=True)
    #data = ts.get_realtime_quotes('601066')

    for num in range(0,100):
        rtData = ts.get_realtime_quotes(['sh', 'sz', '601066', '002074', '110075']) 

        rtDataFormart = rtData[['code','time','open', 'pre_close','price','bid','ask','volume','amount','date']]

        if num == 0 :
            print(rtDataFormart)
        arrays = pd.DataFrame(rtDataFormart.to_numpy())
        #print(arrays)
        zxjtCurrentPrice  = float(arrays[4][2])
        gxgkCurrentPrice  = float(arrays[4][3])
        nhzzCurrentPrice  = float(arrays[4][4])
        zxjtPreClosePrice = float(arrays[3][2])
        gxgkPreClosePrice = float(arrays[3][3])
        nhzzPreClosePrice = float(arrays[3][4])
        currentTime       =  arrays[1][1]
        currentDate       =  arrays[9][1]

        zxjtShareCount  = 1100.00
        gxgkShareCount  = 1600.00
        nhzzShareCount  = 10
        myAccountleft   = 13.45
        investCount     = 100000.00

        zxjtPrecent = (zxjtCurrentPrice - zxjtPreClosePrice)/zxjtPreClosePrice
        gxgkPrecent = (gxgkCurrentPrice - gxgkPreClosePrice)/gxgkPreClosePrice
        nhzzPrecent = (nhzzCurrentPrice - nhzzPreClosePrice)/nhzzPreClosePrice

        TotalShare   = zxjtCurrentPrice * zxjtShareCount + gxgkCurrentPrice * gxgkShareCount + \
            nhzzCurrentPrice *nhzzShareCount + myAccountleft
        ToadyBenefit = (zxjtCurrentPrice - zxjtPreClosePrice) * zxjtShareCount + \
            (gxgkCurrentPrice - gxgkPreClosePrice) * gxgkShareCount + (nhzzCurrentPrice - nhzzPreClosePrice) * nhzzShareCount
        TotalBenifit = TotalShare - investCount

        print(currentTime, '==> zxjt:{:.2f}%'.format(zxjtPrecent*100),'      ','gxgk:{:.2f}%'.format(gxgkPrecent*100),'      ',\
            'nhzz:{:.2f}%'.format(nhzzPrecent*100),'      ',\
            'Benefit:{:.0f}'.format(ToadyBenefit),'      ','{:.0f}'.format(TotalBenifit))
        time.sleep(4)

        # write result to file per ten times
        if num%10 == 9:
            fileName = currentDate + ".txt"
            with open(fileName,"a") as file:
                file.write(str(arrays[1][1]) + "       "+ str(round(TotalShare, 2)) + "       "+ \
                    str(round(zxjtPrecent*100, 2)) + "       "+ str(round(gxgkPrecent*100, 2)) + "       " + str(round(nhzzPrecent*100, 2)) + "       " +\
                        str(round(ToadyBenefit, 2)) + "       "+ str(round(TotalBenifit, 2)) + "\n")

if __name__ == "__main__":
    #print("start...", end="")
    get_data_print()
