# -*- coding:utf-8 -*-
# time:2017/11/21
#import requests
#py 2.7
#！！！
import urllib2,re,HTMLParser,requests
import sys                      #导入/引入一个python标准模块
reload(sys)                     #对已经加载的模块进行重新加载
sys.setdefaultencoding('utf-8') #输出的内容是什么编码


def getHtml(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'} #增加头部信息，防止反扒
    request=urllib2.Request(url,headers=header)
    response=urllib2.urlopen(request)   #打开网页
    text=response.read()                #获取源代码
    #print text
    return text

def getUrls(html):
    pattern=re.compile('<a href="/story/(.*?)"')
    res=re.findall(pattern,html)
    urlist=[]
    for i in res:
        urlist.append("http://daily.zhihu.com/story/"+i)
    #print(urlist)
    return urlist

def getContent(iurl):
    html=getHtml(iurl)
    pattern=re.compile('<h1 class="headline-title">(.*?)</h1>')
    items=re.findall(pattern,html)
    print(items[0])
    pattern1 = re.compile(r'<div class="content">\n<p>(.*?)</div>',re.S)    #re.s的作用扩展到整个字符串，包括“\n”防止因为换行导致检索不到结果
    items = re.findall(pattern1, html)
    for item in items:
        for countent in characterProcessing(item):
            print(countent)

#过滤
def characterProcessing(html):
    htmlParser = HTMLParser.HTMLParser()                                    #对HTMLParser.HTMLParser() 的利用需要实现其子类
    pattern = re.compile('<p>(.*?)</p>|<li>(.*?)</li>.*?', re.S)            #re.s的作用扩展到整个字符串，包括“\n”防止因为换行导致检索不到结果
    items = re.findall(pattern, html)
    result = []
    for index in items:

        if index != '':
            for content in index:
                tag = re.search('<.*?>', content)
                http = re.search('<.*?http.*?', content)
                html_tag = re.search('&', content)
                if html_tag:
                    content = htmlParser.unescape(content)

                if http:
                    continue
                elif tag:

                    pattern = re.compile('(.*?)<.*?>(.*?)</.*?>(.*)')
                    items = re.findall(pattern, content)
                    content_tags = ''
                    if len(items) > 0:
                        for item in items:
                            if len(item) > 0:
                                for item_s in item:
                                    content_tags = content_tags + item_s
                            else:
                                content_tags = content_tags + item_s
                        content_tags = re.sub('<.*?>', '', content_tags)
                        result.append(content_tags)
                    else:
                        continue
                else:
                    result.append(content)
    return result

def getInfo(iurl):
    html = getHtml(iurl)

    # print(items[0])
    # return items
def main():
    url = 'http://daily.zhihu.com/'
    html=getHtml(url)
    urls=getUrls(html)
    #print(urls)
    num=0
    for url in urls:
        try:
            print(getContent(url))
            print(url)
        except Exception,e:
            print(e)
if __name__=='__main__':
    main()