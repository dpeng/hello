# -*- coding:utf-8         -*- 
# -*- Created on 20201029  -*- 
# -*- @author: Kacper      -*- 

import tushare as ts
import pandas as pd
import configparser, time, os
import rumps
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

def get_data_print(_):
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

@rumps.clicked('Reload Config')
def reload_config(_):
    print("reloading...")
    rumpsSelf.title = str('reloading...')
    global myAccountleft, investCount, stockCode, shareCount
    (myAccountleft, investCount, stockCode, shareCount) = load_config_info( )
    print(shareCount)
class macosMenuBar(rumps.App):
    def __init__(self):
        super(macosMenuBar, self).__init__(":-)", title=None, icon=None, template=None, \
            menu=('Change timer', 'Start Monitor', 'Display Name', 'Stop Monitor', 'Reload Config'), quit_button='Exit')
        rumpsTimer.start()

if __name__ == "__main__":
    # setting init account information
    print("starting...")
    print("tushare version: ", ts.__version__)
    print("pandas version: ", pd.__version__)
    print("rumps version: ", rumps.__version__)

    (myAccountleft, investCount, stockCode, shareCount) = load_config_info( )

    rumpsTimer      = rumps.Timer(get_data_print, 5)
    rumpsTimer.isDisplayName = 0
    rumpsSelf       = macosMenuBar()
    rumpsSelf.run()
