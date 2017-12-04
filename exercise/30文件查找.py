import os

def search_f(start_dir,target):
    os.chdir(start_dir)
    for i in os.listdir(os.curdir):
        if i ==target:
            print(os.getcwd()+os.sep+i)
        if os.path.isdir(i):
            search_f(i,target)
            os.chdir(os.pardir)

start_dir=input("请输入待查找的初始目录")
target=input("请输入要查找的目标文件")
search_f(start_dir,target)
'''
def find_file():
    i=input("请输入待查找的初始目录")
    global list1
    list1=list()
    if os.path.isdir(i):
        b=input("请输入要查找的目标文件")
        find1(i,b)
        if list1=='':
            print('未找到')
        else:
            for g in list1:
                print(g)

def find1(lj,b):
    #global list1
    os.chdir(lj)
    pd=os.listdir()
    for i in pd:
        if(os.path.splitext(i))[1]=='':
            find1(os.path.join(lj,i),b)
    if b in pd:
        #print(os.path.join(i,b))
        print('找到')
        list1.append(os.path.join(lj,b))
    os.chdir(os.pardir)
find_file()
'''
