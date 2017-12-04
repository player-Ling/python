def pow(x,y):
    if y>1:
        x=x*pow(x,y-1)
    return x
