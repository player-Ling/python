# -*- coding:utf-8 -*-
# time:2017/11/22
#py 3.6
#！！！
import re,requests,pymysql
db=pymysql.connect(host='localhost',port=3306,passwd='playerN19@',user='root',charset='utf8',db='tz')
#db= pymysql.connect(host='localhost',port=3306,user='root',passwd='playerN19@',charset='utf8',db='doutu')
cursor=db.cursor()
url='http://baidu.com/'
url1='http://daily.zhihu.com/'
def getHtml(url):
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    request = requests.get(url,headers=header)
    html=request.text
    return html

def getUrls(html):
    pa=re.compile(r'<a href="/story/(.*?)".*?<span class="title">(.*?)</span>',re.S)
    urls={}

    res=re.findall(pa,html)
    iurls=["http://daily.zhihu.com/story/"+row[0] for row in res]
    title=[row[1] for row in res]
    urls=dict(zip(iurls,title))             #zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
                                            #如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
    return urls

def getContent(title,url):
    html=getHtml(url)
    content=prossing(html)
    r=''.join(content)          #！！！Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    #print(url,title,re)            #???

    #r=url+title+res
    return r

def prossing(str):                                          #处理文字的方法（有待改进）
    pa=re.compile(r'<p>(.*?)</p>',re.S)
    items=re.findall(pa,str)

    result = []
    if items !='':
        for content in items:
            tag=re.search(r'<.*?>',content,re.S)            #把含有<>归类处理
            http=re.search(r'.*?html.*?',content,re.S)      #把含有html归类处理
            html_tag=re.search(r'&',content,re.S)           #？？？不知道干啥子的
            #print(content)
            if http:
                continue
            #if html_tag:
            #    content = htmlParser.unescape(content)
            elif tag:
                pa=re.compile(r'(.*?)<.*?>(.*?)<.*?>(.*?)')
                items=re.findall(pa,content)
                #print(items)
                content_tag=''
                if len(items) >0:
                    for item in items:
                        if len(item)>0:
                            for items_s in item:
                                content_tag=content_tag+items_s
                        else:
                            content_tag=content_tag+items_s     #???
                    content_tag=re.sub('<.*?>','',content_tag)
                    result.append(content_tag)
                else:
                    continue
            else:
                result.append(content)
    return result

html=getHtml(url1)
urls=getUrls(html)
#print(urls)
for item in urls:
    res=getContent(urls[item],item)
    res=res.replace("'","''")
    print(urls[item],item,res)
    cursor.execute("insert into zhihu(title,content,url) VALUES ('{}','{}','{}')".format(urls[item],res,item))
    db.commit()
db.close()