# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import time, rumps

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
        #time.sleep(5)
        rumpsSelf.title = str(':-(')
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
            if (rumpsTimer.isDisplayName == 0):
                print('{:.2f}'.format(currentPrice[i]), end='') #output current Price
                print_with_color(vibratePrecent[i]*100, 0.0, '%')
            else:
                print(stockName[i], ' ', end='')
        print('  ',end='')
        i = i + 1
    rumpsTimer.isDisplayName = 0
    TotalShare             += myAccountleft
    TotalBenifit            = TotalShare - investCount
    print("pro ", end='')
    print_with_color(ToadyBenefit, 0.0, '')
    print(' ' , end='')
    print_with_color(TotalBenifit, 0.0, '')
    print() # new line

    #output brief information at menu bar of macOS
    rumpsSelf.title = str('{:.2f}|{:.2f}'.format(ToadyBenefit/1000, TotalBenifit/1000))

@rumps.clicked('Change timer')
def changeit(_):
    response = rumps.Window('Enter new interval').run()
    if response.clicked:
        rumpsTimer.interval = int(response.text)

@rumps.clicked('Start Monitor')
def start_timer(_):
    rumpsTimer.start()
    rumpsSelf.title = str('..')

@rumps.clicked('Display Name')
def display_name(_):
    rumpsTimer.isDisplayName = 1

@rumps.clicked('Stop Monitor')
def stop_timer(_):
    rumpsTimer.stop()
    rumpsSelf.title = str(':-)')

class macosMenuBar(rumps.App):
    def __init__(self):
        super(macosMenuBar, self).__init__(":-)", title=None, icon=None, template=None, \
            menu=('Change timer', 'Start Monitor', 'Display Name', 'Stop Monitor'), quit_button='Exit')
        rumpsTimer.start()

if __name__ == "__main__":
    # setting init account information
    myAccountleft   = 149.78
    investCount     = 100000.00
    stockCode       = ('sh'  , '603893' ,  '603606'  ,   '300017'       ,   '300364'         ,   ''       ,   ''       )
    shareCount      = (0.00  ,  200.00  ,  400.00    ,   5900.00        ,    0.00         ,   0.00     ,   0.00     )
    rumpsTimer      = rumps.Timer(get_data_print, 5)
    rumpsTimer.isDisplayName = 0
    rumpsSelf       = macosMenuBar()
    rumpsSelf.run()
