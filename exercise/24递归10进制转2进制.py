'''
#wrong
def zz(x):
   y=''
    if x/2!=0:
        y=1
    else:
        if x%2==0:
            y=y+'0'
            zz(x//2)
        else:
            y=y+'1'
            zz(x//2)
    return y
'''
def zz(x):
    y=''
    if x:
        y=zz(x//2)
        return y+str(x%2)
    else:
        return y
        
