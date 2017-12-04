import os

def find1(URL,typ):
    os.chdir(URL)
    for i in os.listdir():
        if (os.path.splitext(i))[1]==typ:
            list1.append(os.getcwd()+os.sep+i+os.linesep)
        if os.path.isdir(i):
            find1(i,typ)
            os.chdir(os.pardir)
    
        
URL=input('请输入要查找的目录')
typ=input('请输入文件的类型')

if os.path.isdir(URL):
    list1=[]
    find1(URL,typ)
    if list1!=[]:
        f=open(URL+os.sep+'vedioList.txt','at')
        for i in list1:
            print(i)
            #print(k)
            f.write(i)
            
        f.close()
        print("已把文件归纳于"+URL+'的vedioList.txt中')
    else:
        print('未找到'+typ+'类型的文件')
else:
    print('该路径未找到')
'''
def search_file(start_dir,target):
    os.chdir(start_dir)
    for i in os.listdir():
        ext=os.path.splitext(i)[1]
        if ext in target:
            vedio_list.append(os.getcwd()+os.sep+i+os.linesep)
        if os.path.isdir(i):
            search_file(i,target)
            os.chdir(os.pardir)

start_dir=input('请输入要查找的目录')
program_dir=os.getcwd()
target=input('请输入文件的类型')
vedio_list=[]
search_file(start_dir,target)
f=open(program_dir+os.sep+'vediolist.txt','w')
f.writelines(vedio_list)
print(vedio_list)
f.close()
'''
