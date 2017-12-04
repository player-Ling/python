import random            #随机函数
import math
t=0
a=random.randint(1,10)

while(t==0):
    #t=t+1
    i1=input("guess:")
    i=0
    #print(type(i))
    #print(isinstance(a,int))
    if(i1.isdigit()==1):
        i=int(i1)
        if(i==a):
            print("success")
            break
        else:
            if(i>a):
                print("big")
            if(i<a):
                print("small")
    else:
        print("输入类型不正确");

"""
s.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。

s.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。

s.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。

s.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。

s.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。

s.istitle()      所有单词都是首字母大写，为真返回 Ture，否则返回 False。

s.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False。

"""
