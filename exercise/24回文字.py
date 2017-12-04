'''
def hwz(a):
    b=0
    if len(a)>1:
        if a[0]==a[-1]:
            hwz(a[1:len(a)-1])
        else:
            b+=1
    else:
        return 0
        
    if b>0:
        print(a+'不是回文')
    elif b==0:
        print(a+'是回文')
'''
def is(n,start,end):
    if start>end:
        return 1
    else:
        return is(n,start+1,end-1)if n[start]==n[end]else 0

