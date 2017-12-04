for i in range(100,1000):
    if(((i//100)**3+(i%10)**3+(i%100//10)**3)==i):
        print(i)
'''
1.	for i in range(100, 1000):
2.	    sum = 0
3.	    temp = i
4.	    while temp:
5.	        sum = sum + (temp%10) ** 3
6.	        temp //= 10         # 注意这里要使用地板除哦~
7.	    if sum == i:
8.	        print(i)

'''
