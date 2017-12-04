def bulid(na,pw):
    global dict1,a
    if na in dict1.keys():
        print('该用户已存在，请重输')
        a='N'
    else:
        dict1[na]=pw
        print('创建成功')
        return 1
def init(na,pw):
    global dict1,a
    if na in dict1.keys():
        if pw ==dict1[na]:
            print('登录成功')
            return 1
        else:
            print('密码错误')
    else:
        print('该用户不存在，请重输')
        a='E'
        return 
dict1=dict()
while 1:
    
    print('\n|---新建用户：N/n---|')
    print('|---登录账户：E/e---|')
    print('|---退出程序：Q/q---|')
    a=input('|---请输入指令代码')
    if a=='N' or a=='n':
        while 1:
            a=bulid(input('请输入用户名'),input('请输入密码'))
            if a==1:
                break
    elif a=='E' or a=='e':
        while 1:
            q=init(input('请输入用户名'),input('请输入密码'))
            if q==1:
                break
    elif a=='Q' or a=='q':
        break
    else:
        print('输入错误请重输')
