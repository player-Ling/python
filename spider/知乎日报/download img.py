# -*- coding:utf-8 -*-
# time:2017/11/28
import requests,urllib

req = urllib.request.urlopen('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1511889261661&di=a9bf1e5f72efe4d3bca45b38ceea17d5&imgtype=0&src=http%3A%2F%2Fwww.taopic.com%2Fuploads%2Fallimg%2F140421%2F318743-140421213T910.jpg').read()
with open(r'C:\Users\凌\Desktop\first.jpg','wb') as file:
    file.write(req)
