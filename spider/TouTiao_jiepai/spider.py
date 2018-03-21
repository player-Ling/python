#!/user/bin/env python
# -*- coding:utf-8 -*-
# time:2018/3/20
import json,re,os
from hashlib import md5
import pymongo
import requests
from urllib.parse import urlencode
from json.decoder import JSONDecodeError
from config import *
from bs4 import BeautifulSoup
from multiprocessing import Pool

client=pymongo.MongoClient(MONGO_URL,connect=False)#???;connect=False解除多线程警告
db=client[MONGO_DB]

def get_page_index(offect,KEY_WORD):
    data={
        'offset':offect,
        'format':'json',
        'keyword':KEY_WORD,
        'autoload':'true',
        'count':'20',
        'cur_tab':3,
        'from':'gallery'
    }
    params = urlencode(data)
    url="https://www.toutiao.com/search_content/?"+urlencode(data)#urlencode():把字典等转为urlencode的方法
    #print(url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except ConnectionError:
        print('请求索引页出错')
        return None

def parse_page_index(text):
    try:
        data = json.loads(text)     #解码python json格式，将python json格式解码成Python数据风格，与json.dumps对应（将一个Python数据类型列表进行json格式的编码解析）
                                    #json.dump和json.dumps很不同，json.dump主要用来json文件读写，和json.load函数配合使用。
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('请求详情页出错')
        return None



def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'lxml')     #使用lxml解析库生成BS4对象
    title=soup.select('title')[0].get_text()    #使用select获取属性并提取第一个值的文字
    patt=re.compile('gallery: JSON.parse\("(.*?)"\),', re.S)
    result=re.search(patt,html)
    if result:
        data=json.loads(result.group(1).replace("\\",""))       #正则表达式中，group()用来提出分组截获的字符串,()用来分组
                                                                #group()同group（0）就是匹配正则表达式整体结果
                                                                #group(1)列出第一个括号匹配部分，group(2)列出第二个括号匹配部分，group(3)列出第三个括号匹配部分。
        if data and 'sub_images' in data.keys():
            sub_image=data.get('sub_images')
            images=[item.get('url') for item in sub_image]
            for image in images:down_image(image)
            return{
                'title':title,
                'images':images,
                'url':url
            }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):#？？？
        print("存储成功",result)
        return True
    return False

def down_image(url):
    print("当前正在下载",url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)#content返回二进制内容，text返回网页文本
            return response.text
        return None
    except ConnectionError:
        print('请求图片出错')
        return None

def save_image(content):
    file_path='{0}/{1}.{2}'.format(r'C:\Users\Ling\Desktop\头条街拍',md5(content).hexdigest(),'jpg')#???
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()

def main(offect):
    html=get_page_index(offect,KEY_WORD)
    urls=parse_page_index(html)
    for url in urls:
        html=get_page_detail(url)
        if html:
            result=parse_page_detail(html,url)
            save_to_mongo(result)

if __name__=='__main__':
    groups=[i for i in range(GROUP_START,GROUP_END+1)]
    pool=Pool()
    pool.map(main,groups)