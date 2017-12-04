
def compare_file(file1,file2):
    b=0
    if file1 and file2:
        fi1=open(file1,'r')
        fi2=open(file2,'r')
        f1=fi1.readlines()
        f2=fi2.readlines()
        
        for i in range(len(f1)):
            if f1[i]!=f2[i]:
                print('第%d行不一样'%(i+1))
                b+=1
        print('两个文件共有【%d】处不同'%b)
        fi1.close()
        fi2.close()
    else:
        print('文件错误')

compare_file(input('第一个文件'),input('第二个文件'))
'''
def compare_file(file1,file2):
    b=0
    if file1 and file2:
        f1=open(file1,'r')
        f2=open(file2,'r')
        count=0
        differ=[]
        
        for i1 in f1:
            i2=f2.readline()
            count+=1
            if i1!=i2:
                differ.append(count)
        f1.close()
        f2.close()
        
    else:
        print('文件错误')
        return 0
    return differ

differ=compare_file(input('第一个文件'),input('第二个文件'))
if len(differ)==0:
    print('两个文件一模一样')
else:
    print('两个文件共有【%d】处不同'%len(differ))
    for each in differ:
        print('第%d行不一样'%each)
'''
