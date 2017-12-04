import os

def stat():
    l=os.listdir()
    text=dict()
    for i in l:
        if (os.path.splitext(i))[1] in text.keys():
            text[(os.path.splitext(i))[1]]+=1
        else:
            text[(os.path.splitext(i))[1]]=1

    for i in text:
        print("该文件夹下共有类型为【%s】的文件%s个"%(i,text[i]))#

stat()
