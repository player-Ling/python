def file_compare(file1,file2):
    count=''
    try:
        with open(file1) as fl1,open(file2) as fl2:
            f1=fl1.readlines()
            f2=fl2.readlines()
            count=0
            for i in range(len(f1)):
                list1=list()
                if f1[i]!=f2[i]:
                    for i1 in range(len(f1[i])):
                        print(i1)
                        if f1[i][i1]!=f2[i][i1]:
                            list1.append(i1+1)
                            count+=1
                    if list1!=[]:
                        dif[i+1]=list1
    except OSError:
        print('文件错误')
    return count
                    


file1=input('请输入文件1：')
file2=input('请输入文件2：')
dif=dict()
num=file_compare(file1,file2)
if num==0:
    print('两个文件相同')
elif num>0:
    print('两个文件共有%s处不同'%num)
    for i in dif:
        print('第%d行的第%s处不同'%(i,dif[i]))
