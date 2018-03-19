# -*- coding:utf-8 -*-
# time:2018/3/9
#maoyan tao100
import requests,re,json
from multiprocessing import Pool
from requests.exceptions import RequestException
def get_one_page(url,headers):
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield{      #把返回值变成生成器进行迭代
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],    #??
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
def write_to_file(content):
    with open(r'C:\Users\凌\Desktop\result2.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')   #json.dumps:把字典格式转化为字符串格式
        f.close()

def main(offset):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    url='http://maoyan.com/board/4?offset=' + str(offset)
    html=get_one_page(url,headers)
    #print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    #for i in range(10):
    #   main(i*10)
    pool=Pool()         #通过进程池抓去
    pool.map(main,[i*10 for i in range(10)])
