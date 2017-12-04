y=[]
def sz(x):
    if x>0:
        y.insert(0,x%10)
        sz(x//10)
    return y
    
        

