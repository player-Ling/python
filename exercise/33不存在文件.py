try:
    f=open('My_file.txt')
    print(f.read())
except OSError as reason:
    print('出错啦'+str(reason))

finally:
    if 'f' in locals():#如果文件对象变量存在当前局部变量符号的话，说明打开陈功
        f.close()

