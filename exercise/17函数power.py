def power(a,b):
    pow1=1
    while(b>0):
        pow1*=a
        b-=1
    return pow1

print(power(2,8))
