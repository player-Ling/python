a=input("guess:\n")
#print("\n")
while(a):
    if(a.isdigit()==1):
        b=int(a)
        if((b%4==0 and b%100!=0) or b%400==0):
            print("%d是闰年"%b)
            break
        else:
            print("%d不是闰年"%b)
            break
    else:
        print("请重新输入")
        a=input("guess\n")
"""
1.	temp = input('请输入一个年份：')
2.	while not temp.isdigit():
3.	    temp = input("抱歉，您的输入有误，请输入一个整数：")
4.	
5.	year = int(temp)
6.	if year/400 == int(year/400):
7.	    print(temp + ' 是闰年！')
8.	else:
9.	    if (year/4 == int(year/4)) and (year/100 != int(year/100)):
10.	        print(temp + ' 是闰年！')
11.	    else:
12.	        print(temp + ' 不是闰年！')

"""

