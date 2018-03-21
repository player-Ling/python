#-*- coding:utf-8 -*-

import urllib.request,urllib

#print(urllib.urlopen(url).read())
def callback(a,b,c):
    res=100*a*b/c
    if res>100:
        res=100
    print('\r'+'%.2f%%'%res,end='')
url='https://docs.python.org/3/library/index.html'
local=r'D:\1\1.html'
urllib.request.urlretrieve(url,local,callback)

