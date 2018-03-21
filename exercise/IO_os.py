import os
num=0
def in_fine(path,num):
    num+=1
    try:
        if os.path.isfile(r'{}'.format(path)):#isfile判断路径是否是一个文件
            print('\t'*num + os.path.basename(path))
            # os.pardir()
        elif os.path.isdir(r'{}'.format(path)):   #isdir:判断路径是否是一个目录
            print(path)
            for i in os.listdir(path):          #遍历当前目录下的文件名
                os.chdir(path)                  #更改工作目录
                ipath = os.path.join(os.getcwd(), i)    #组合
                in_fine(ipath,num)              #递归


    except PermissionError:
        pass
    num -= 1
def find_file():
    path=(r'd:\\')
    try:
        in_fine(path,num)
        
    except FileNotFoundError:
        print('路径不存在请重新输入')
        find_file()

if __name__=='__main__':
    find_file()
