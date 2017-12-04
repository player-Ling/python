i=1
def hlt(x,a,b,c):
    global i
    if x==1:
        print(".第%d步，将%c移动到%c"%(i,a,c))
    else:
        hlt(x-1,a,c,b)
        i+=1
        print("第%d步，将%c移动到%c"%(i,a,c))
        i+=1
        hlt(x-1,b,a,c)
 
