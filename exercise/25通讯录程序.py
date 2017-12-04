print('---欢迎进入通讯录程序---')
print('---1：查询联系人资料---')
print('---2：插入新的联系人---')
print('---3：删除已有联系人---')
print('---4：退出通讯录程序---')
print('')

con=dict()

while 1:
    i=int(input('\n请输入相关指令代码'))
    if i==1:
        name=input('请输入联系人姓名')
        if name in con:
            print(name+':'+con[name])
        else:
            print('查无此人')
    if i==2:
        name=input('请输入联系人姓名')
        if name in con:
            print("该用户已存在",end='')
            print(name+':'+con[name])
            if input("是否修改电话号码（YES/NO）")=='YES':
                con[name]=input("请输入电话：")
        else:
            con[name]=input("请输入电话：")
    if i==3:
        name=input('请输入联系人姓名')
        if name in con:
            del(con[name])
            print('已删除该用户%s：%s'%(name,con[name]))
            #con.pop[name]
        else:
            print("查无此人")
    if i==4:
        break
print("感谢使用")


'''
def sr():
    global a
    print('')
    a=input('请输入相关指令代码')
    while(not a.isnumeric()):
        a=input('请重新输入相关指令代码')
    a=int(a)
    #print(type(a),a)
    
a=input('请输入相关指令代码')
while(not a.isnumeric()):
    a=input('请重新输入相关指令代码')
a=int(a)

adict={}

while(a!=4):
    if a==1:
        b=input('请输入联系人姓名')
        if b in adict.keys():
            print('%s:%s'%(b,adict[b]))
            sr()
        else:
            print('查无此人')
            sr()
    elif a==2:
        b=input('请输入联系人姓名')
        if b in adict.keys():
            print('该用户已存在%s：%s'%(b,adict[b]))
            d=input('是否修改用户资料(YES/NO)')
            while not (d=='YES' or d=='NO'):
                print('输入错误')
                d=input('是否修改用户资料(YES/NO)')
            if d=='YES':
                c=input('请输入联系人手机')
                adict[b]=c
                sr()
            elif d=='NO':
                sr()
        else:
            c=input('请输入联系人手机')
            adict[b]=c
            sr()
    elif a==3:
        b=input('请输入联系人姓名')
        if b in adict.keys():
            print('已删除该用户%s：%s'%(b,adict[b]))
            adict.pop(b)
            sr()
        else:
            print('查无此人')
            sr()
    else:
        print("输入错误请重新输入")
        sr()
'''
