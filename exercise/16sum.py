#将ASCII字符转换为对应的数值即‘a’-->65，使用ord函数,ord('a')
#使用chr函数，将数值转换为对应的ASCII字符，chr(65)
a=input("请输入")
sum=0
while(a):
    a=a.split(',')
    for i in a:
        if(i.isalnum()==False):
            a=input("请输入数字或字符")
        else:
            if(i.isalpha()):
                i=ord(i)
            elif(i.isnumeric()):
                i=int(i)
            sum+=i
    print(sum)
    break
