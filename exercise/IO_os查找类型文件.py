import os
def pr_file(path,*typ):
    try:
        if os.path.isdir(r'{}'.format(path)):
            for i in os.listdir(path):
                os.chdir(path)
                ipath=os.path.join(os.getcwd(),i)
                pr_file(ipath,*typ)
        elif os.path.isfile(r'{}'.format(path)):
            if os.path.splitext(os.path.basename(path))[1] in typ:
                print(path)
    except PermissionError:
        pass

def find_file():
    # path = input('请输入路径')
    # typ =input('请输入文件类型')
    path=(r'f:\\python')
    typ=('.py','.txt')
    try:
        pr_file(path, *typ)
    except FileNotFoundError:
        print('路径不存在请重新输入')
        find_file()


if __name__ == '__main__':
    find_file()




'''
def traversal_dir(current_path, substr):
    #print('current path %s' % current_path)
    files = []
    dirs = []
    try:
        files = [x for x in os.listdir(current_path) if os.path.isfile(os.path.join(current_path, x))] #获取目录所有文件
        dirs = [x for x in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, x))] #获取目录所有目录
        #print(files)
        #print(dirs)
    except Exception as e:
        pass

    for x in files:
        if x.find(substr) >= 0:
            print(os.path.join(current_path,x))

    for x in dirs:
        nextpath = os.path.join(current_path, x)
        #print('next path %s' % nextpath)
        traversal_dir(nextpath, substr)

traversal_dir('D:', '.py')
'''