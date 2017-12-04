def gy(x,y):
    if x%y!=0:
        y=gy(y,(x%y))
    return y
