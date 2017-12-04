import os
import pickle

def countline(URL='.'):
    count=0
    os.chdir(URL)
    li=os.walk(URL)
    for i in li:
        for i1 in i[2]:
            if os.path.splitext(i1)[1] in ['.py','.c']:
                f=open(os.path.join(i[0]+os.sep+i1),'rb')
            #print(i)
                fl=f.readlines();
                count+=len(fl)
                f.close()
    print('你总共些了%s行代码'%count)
            

URL=input('请输入目录')
countline(URL)
#17/05/06   2701
