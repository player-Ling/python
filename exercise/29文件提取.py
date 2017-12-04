def print_file(file_name,first1,end1):
    f=open(file_name)

    if first1=='':
        first=0
        fir1='开始'
    else:
        first=int(first1)-1
        fir1='第'+str(first1)+'行'
        
    if end1=='':
        end=len(f.readlines())
        f.seek(0,0)
        en1='结束'
    else:
        end=int(end1)
        en1='第'+str(end1)+'行'
        
    if first1==''and end1=='':
        print("文件%s全文的内容如下"%file_name)
    else:
        print("文件%s从%s到%s的内容如下"%(file_name,fir1,en1))
    for i in range(first):
        f.readline()
    
    for i in range(end-first):
        print(f.readline())

    f.close()

file_name=input("请输入要打开的文件：")
inx=input("请输入要显示的行数【格式如13：21】或【：21或21:】")
first,end=inx.split(':')
print_file(file_name,first,end)
