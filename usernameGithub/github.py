import requests
import sys
import os
import time

# work dir
# os.chdir(sys.path[0])
os.chdir(r'/home/dpeng/code/usernameGithub')

def trans_time(sec):
    hour = int(sec / 3600)
    sec = sec % 3600
    minute = int(sec / 60)
    sec = sec % 60
    return "%s hour %s min %.2f sec" % (hour, minute, sec)

def get_html(url):
    try:
#        time.sleep(1)
        print('Accessing the github website...', url)
        html = requests.get(url, headers=headers, timeout=10).text
    except Exception as e:
        print('exception happened, and sleep ten seconds before retry')
        print(e)
        time.sleep(10)
        return get_html(url)
    print('Get the html from github successfully!')
    return html


start = time.time()
url = r'https://github.com/search?q={0}&type=Users&ref=searchresults'

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Host':'github.com',
'Referer':'https://github.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
}
count = 0
found = 0

# open the words.txt
with open('words.txt', 'r') as input:
    while True:
        print('=' * 120)
        print('reading the key work from word.txt')
        line = input.readline()
        if not line:
            break
        word = line.split(' ', 1)[0]
        print('read word from file successflly', word)
        used_time = trans_time(time.time() - start)
        count += 1

        print('Checking %s: checked %s words, find %s result. script already running %s' % (word, count, found, used_time))

        html = get_html(url.format(word))
        # if the user name doesnt used'We couldn't find any users matching xxxxx'
        print('writed to the file')
        if 'find any users matching' in html:
            found += 1
            with open('youcanuse.txt', 'a') as output:
                output.write(line)
        print('Write successflly')

used_time = trans_time(time.time() - start)
print('Done! \n time eclips %s\n totally checked %s word and %s can used' % (used_time, count, found))
