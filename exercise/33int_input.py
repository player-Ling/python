def in_input():
    while 1:
        try:
            a=int(input('请输入一个整数'))
            break
        except ValueError:
            print('您输入的不是一个整数')

in_input()
