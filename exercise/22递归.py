def JC(x):
    if(x==1):
        return 1
    else:
        return x*JC(x-1)
	
'''
def factorial(x):
    re=x
    for i in range(1,x):
        re*=i

    return re
x=int(input())
print("%d的阶乘是%d"%(x,factorial(x)))
'''
