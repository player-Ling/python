def X3(*a,base=3):
    if a:
        a=list(a)
        b=0
        for i in range(len(a)):
            if(a[len(a)-1]!=5):
                a[i]=a[i]*base
            else:
                base=5
                a[i]=a[i]*base
                b=1
        if(b==1):
            a.pop()
    return a
print(X3(1,2,3,4,5,3))
