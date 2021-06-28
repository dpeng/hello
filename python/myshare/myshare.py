# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import time, rumps

outputNameOrCodeCount = 0
def print_with_color(var, target, flag):
    if(var < target):
        #print ('%s%s%s%s' % ("\033[32m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #green
        print ('%s%s%s%s' % ("\033[34m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #blue
    else:
        print ('%s%s%s%s' % ("\033[31m", '{:.2f}'.format(abs(var)), flag, "\033[0m"), end='')  #red

def get_data_print(_):
    #data = ts.get_hist_data("601066", start="2020-10-01", end="2020-10-29")
    #data = data.sort_values(by=["date"], ascending=True)
    pd.set_option('display.max_columns', None)
    # setting init account information
    myAccountleft   = 1013.45
    investCount     = 100000.00
    stockName       = (''    , 'wczd'    , 'yjdq '  ,  'slw  '    ,   'rhrj '     ,   ''       ,   ''       )
    stockCode       = ('sh'  , '600704'   , '300820' ,  '600460'   ,   '300339'    ,   ''       ,   ''       )
    shareCount      = (0.00  ,  3000.00   ,  500.00  ,  400.00     ,    300.00     ,   0.00     ,   0.00     )

    currentPrice    = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    preClosePrice   = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    vibratePrecent  = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    TotalShare      = 0.00
    ToadyBenefit    = 0.00
    TotalBenifit    = 0.00
    rtData          = []
    try:
        rtData = ts.get_realtime_quotes(stockCode) 
    except:
        print("Oops!  Network connetion error.  Will ry again 5 seconds later...")
        time.sleep(5)
        return

    rtDataFormart = rtData[['code','time','open', 'pre_close','price','bid','ask','volume','amount','date']]

    arrays = pd.DataFrame(rtDataFormart.to_numpy())
    currentTime     =  arrays[1][1]
    currentDate     =  arrays[9][1]

    print(currentTime, '', end='')
    i = 0
    global outputNameOrCodeCount
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
            if (outputNameOrCodeCount % 10):
                print('{:.2f}'.format(currentPrice[i]), end='') #output current Price
            else:
                print(stockName[i], end='')
            print_with_color(vibratePrecent[i]*100, 0.0, '%')
        print('  ',end='')
        i = i + 1
    outputNameOrCodeCount = outputNameOrCodeCount + 1
    TotalShare           += myAccountleft
    TotalBenifit          = TotalShare - investCount
    print("pro ", end='')
    print_with_color(ToadyBenefit, 0.0, '')
    print(' ' ,end='')
    print_with_color(TotalBenifit, 0.0, '')
    print() # new line

    #output brief information at menu bar of macOS
    rumpsSelf.title = str('{:.2f}|{:.2f}'.format(ToadyBenefit/1000, TotalBenifit/1000))

@rumps.clicked('Change timer')
def changeit(_):
    response = rumps.Window('Enter new interval').run()
    if response.clicked:
        rumpsTimer.interval = int(response.text)

@rumps.clicked('Start timer')
def start_timer(_):
    rumpsTimer.start()

@rumps.clicked('Stop timer')
def stop_timer(_):
    rumpsTimer.stop()
    rumpsSelf.title = str('status')
    
class macosMenuBar(rumps.App):
    def __init__(self):
        super(macosMenuBar, self).__init__("status", title=None, icon=None, template=None, \
            menu=('Change timer', 'Start timer', 'Stop timer'), quit_button='Exit')
        rumpsTimer.start()

if __name__ == "__main__":
    rumpsTimer = rumps.Timer(get_data_print, 5)
    rumpsSelf = macosMenuBar()
    rumpsSelf.run()
