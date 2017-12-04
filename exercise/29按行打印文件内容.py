def print_line():
    f1=open(input('请输入文件名'))
    line=int(input('请输入需要显示该文件的前多少行'))
    print("文件前%d行的内容如下"%line)
    
    while line>0:
        print(f1.readline())
        line-=1
    f1.close()
    
print_line()

'''
a=21
b=21
c=23
d=23
e=21
