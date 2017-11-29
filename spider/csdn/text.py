# -*- coding:utf-8 -*-
# time:2017/11/25
q='http://bbs.csdn.net/recommend_tech_topics'
w='http://bbs.csdn.net/recommend_tech_topics?page=2'
import re,requests
a=r'\n'
b=a.replace(r"'\'",r'\\')
def getHtml(url):
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    request = requests.get(url,headers=header)
    html=request.text
    return html

def getCon(str):
    html=getHtml(str)
    pa1=re.compile(r'<title>(.*?)</title>',re.S)
    pa2=re.compile(r'data-floor="">(.*?)<!-- Baidu Button BEGIN -->',re.S)
    title=re.findall(pa1,html)
    tex=re.findall(pa2,html)
    content=pross(tex)
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
getCon('http://bbs.csdn.net/topics/392290259')