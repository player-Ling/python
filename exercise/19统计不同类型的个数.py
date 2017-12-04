def count(*x):
    for y in x:
        y.split('\'')
        a=b=c=d=0
        for i in y:
            if i.isalpha():
                a+=1
            elif i.isnumeric():
                b+=1
            elif i.isspace():
                c+=1
            else:
                d+=1
        print("字符串%s共有：英文字母%d个，数字%d个，空格%d个,其他字符%d个\n"%(i,a,b,c,d))

z=input()
count(z)
