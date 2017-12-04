import random
import math
t=0
a=random.randint(1,10)

while(t==0):
    #t=t+1
    i=int(input("guess:"))
    if(i==a):
        print("success")
        break
    else:
        if(i>a):
            print("big")
        if(i<a):
            print("small")

            
"""
random.seed(10)
print random.random()   #0.57140259469
random.seed(10)
print random.random()   #0.57140259469  同一个种子值，产生的随机数相同
pr int random.random()   #0.428889054675
 
random.seed()           #省略参数，意味着取当前系统时间
print random.random()
random.seed()
print random.random()
"""
