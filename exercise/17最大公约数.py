def gcd(x, y):
    '''
    if(x<y):
        z=x
        x=y
        y=z'''
    while(x%y!=0):
        z=x
        x=y
        y=z%y
    return y

