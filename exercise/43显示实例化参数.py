class C:
    def __init__(self,*c):
        if not c:
            print('并没有实例化参数')
        else:
            print('传入了%d个参数，他们分别是'%len(c),end='')
            for i in c:
                print(i,end='')
