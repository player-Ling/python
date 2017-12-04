name=input("请输入你想查找的姓名")
score=[['Ling',100],['dao',90],['qw',70],['er',60],['b',50],['a',40]]
b=False
for i in score:
    if(name==i[0]):
        b=True
        print(name+'的分数是%d'%i[1])

#print(b)

if(b==False):
    print("查无此人")
