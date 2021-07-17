import re
import urllib.request
import os

def get_url(page):
    #爬取得网站信息
    html="https://www.musicbooks.cn/category/%e7%bd%91%e6%98%93%e4%ba%91%e9%9f%b3%e4%b9%90%e7%83%ad%e8%af%84/page/" + page
    data=urllib.request.urlopen(html).read()
    data=data.decode('utf-8')
    pattern = re.compile('https://www.musicbooks.cn/[1-9]\d*.html').findall(data)
    return (pattern)
def write(str_):
    f = open('D:\\Users\\JOJO\\Desktop\\wyy.txt','')
    s = f.read()
    f.write(s + '\n\n'+ str_)
    f.close()

put = []
for i in range(144):
    a = get_url(str(i+1))
    for j in a:
        data=urllib.request.urlopen(j).read()
        data=data.decode('utf-8')
        pattern = re.compile('description" content=".*"').findall(data)
        put.append(pattern[0][22:-1])
        #write(pattern[0][22:-1])
print(put)
f = open('D:\\Users\\JOJO\\Desktop\\wyy.txt','a',encoding = 'utf-8')
for i in put:
    f.write(i+'\n')

f.close()
