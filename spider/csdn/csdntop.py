# -*- coding:utf-8 -*-
# time:2017/11/25
# py 3.6 csdn版主推荐-技术区前50入库
import re,requests,pymysql

db=pymysql.connect(host='localhost',port=3306,passwd='playerN19@',user='root',charset='utf8',db='tz')
cur=db.cursor()  #？？？有s和没S的区别
urll = 'http://bbs.csdn.net/recommend_tech_topics?page={}'
def getHtml(url,page=0):
    url = url.format(page)
    res=requests.get(url)
    res=res.content.decode()
    return res

def getUrls(str):
    po=re.compile(r'<a href="/topics/(.*?)" target="_blank">.*?</a>',re.S)
    list=re.findall(po,str)
    res=[]
    for i in list:
        res.append('http://bbs.csdn.net/topics/'+i)
    return res

def getCon(str):
    ht=getHtml(str)
    pa1=re.compile(r'<title>(.*?)</title>',re.S)
    pa2=re.compile(r'data-floor="">(.*?)<!-- Baidu Button BEGIN -->',re.S)
    title=re.findall(pa1,ht)
    tex=re.findall(pa2,ht)
    content=pross(tex)
    #print(title,content)
    return title,content

def pross(str1):
    string="".join(str1)           #把数组变成字符串

    pa=re.compile(r'(.*?)<.*?>(.*?)<.*?>(.*?)',re.S)
    tex=re.findall(pa,string)

    res=[]
    if tex:
        for con in tex:
            con=list(con)
            for i in con:
                i = i.replace(' ', '')
                i = i.replace('\n', '')
                i = i.replace('&nbsp;', ' ')
                content = ''

                if i != '':
                    res.append(i)
    return res
cur.execute("truncate table csdn;")
db.commit()
for page in range(1,3):
    html = getHtml(urll,page)
    urllist = getUrls(html)
    for i in urllist:
        title = "".join(getCon(i)[0])
        con = "".join(getCon(i)[1])
        con = con.replace("'", "''")
        print(i, title, con)
        cur.execute("insert into csdn(title,content,url) VALUES ('{}','{}','{}')".format(title, con, i))
        db.commit()
db.close()