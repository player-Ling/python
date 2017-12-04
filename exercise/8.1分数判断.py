print("分数查询")
a=input("请输入分数\n")
while(a.isdigit()==0):
    a=input("错误，请重新输入分数\n")
a=int(a)
if 80>a>=60:
    print("D")
elif 0<=a<60:
    print("C")
elif 90>a>=80:
    print("B")
elif 100>=a>=90:
    print("A")
else:
    print("输入错误")
