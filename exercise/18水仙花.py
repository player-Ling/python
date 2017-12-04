def sxh():
    for x in range(100,1000):
        a=(x//100)**3
        b=(x%100//10)**3
        c=(x%10)**3
        #print(a,b,c)
        if (a+b+c==x):
            print(x)
            

