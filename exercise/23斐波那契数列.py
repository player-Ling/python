'''
#迭代
def fb(x):
    if x>2:
        x=fb(x-1)+fb(x-2)
    elif x==2:
        x=1
    return x
'''
#递归
def fb(x):
    n1=1
    n2=1
    n3=1
    if x==2:
        n2=1
    elif x>2:
        for i in range(2,x):
            n3=n2+n1
            n1=n2
            n2=n3
    return n3
