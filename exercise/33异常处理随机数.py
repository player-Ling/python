import random

an=random.randint(1,10)


while 1:
    try:
        num=int(input('猜数字是多少'))
        if num==an:
            print('猜对啦')
            break
        elif num>an:
            print('猜大了')
        elif num<an:
            print('猜小了')
        else:
            print('猜错了')
    except ValueError:
        print('数据类型错误，请重新输入')

