def findstr():
    a=input("请输入目标字符串:")
    b=input("请输入子字符串(2个字符):")
    if(a and b.isalpha() and len(b)==2):
        c=a.count(b)
        print("子字符串在目标字符串中一共出现%d次"%c)
    else:
        print("输入错误")
