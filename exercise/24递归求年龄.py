'''
y=10
def age(x):
    global y
    if x==1:
        return y
    else:
        y+=2
        age(x-1)
    return y
'''
def age(x):
    if x==1:
        return 10
    else:
        return age(x-1)+2
