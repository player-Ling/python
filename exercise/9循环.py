'''
a='Ling'
for i in range(3):
    b=input("请输入姓名：\n")
    while '*' in b:
        b=input("不能有*请重新输入姓名：\n")
    if b==a:
        print("Greate")
        break
    else:
        print("wrong还有%d次机会"%(2-i))
        #b=input("请重新输入姓名：\n")
        continue'''
count=3
password='Ling'
while count:
    passwd=input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count-1, '次机会！', end=' ')
    count-=1
      
"""
for i in range(10):
    if i%2!=0:
        print(i)
        continue
    i+=1
    print(i)
"""
"""
for i in 10:
    i=i+2
    print(i)
"""
"""wrong
i=0
string1='Ling.com'
while i< range(len(string1)):
    print(i)
"""
'''
a=0
string1='Ling.com'
for i in string1:
    print(a)
    a+=1
'''

