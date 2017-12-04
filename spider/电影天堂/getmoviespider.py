# -*- coding:utf-8 -*-
import requests
import re
import pymysql

db=pymysql.connect(host='localhost',port=3306,user='root',password='playerN19@',charset='utf8',db='mv')
cursor=db.cursor()

def  getMovieList(page):
    res = requests.get('http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(page)) #format??(字符串格式化和%作用类似)
    res.encoding = 'gb2312'
    result=res.text
    reg=r'<a href="(.*?)" class="ulink"(.*?)</a>'
    reg=re.compile(reg)              #rs.compile??(转换成正则表达式对象)
    return re.findall(reg,result)   #reg.findall??（将该网页所拥有的该正则表达式全部匹配）
    #print(res.text)
def getMovieContent(url,title):
    res=requests.get('http://www.dytt8.net{}'.format(url))  #.format()
    res.encoding='gb2312'
    result = res.text
    reg=r'<div class="co_content8">(.*?)<strong>.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">'
    reg=re.compile(reg,re.S)
    try:
        content, link = re.findall(reg, result)[0]  # ???
    except:
        print(title,'出现错误以忽略')
        return
    sql="insert into by_movie(title,content,link) values('{}','{}','{}')".format(title,content.replace("\'","\\'"),link) #format
    cursor.execute(sql)#执行sql语句
    db.commit()
    #print(content)
    #print(link)
#print(getMovieList())
for page in range(5):
    for url,title in getMovieList(page):    #!!!（难吗？）
        getMovieContent(url,title)
db.close()