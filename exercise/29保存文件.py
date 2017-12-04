def safe():
    file_name=open(input("请输入文件名"),'at')
    print("请输入内容【单独输入‘：w’保存退出】:")
    while 1:
        str1=input('')
        if  str1==':w':
            break
        file_name.write(str1+'\n')
    file_name.close
safe()
