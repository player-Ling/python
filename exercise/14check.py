while(1):
    a=input("来输入一个密码\n")
    b=0

    q=0
    w=0
    e=0
    for i in a:
        if(i.isnumeric()):
            q+=1
        elif(i.isalpha()):
            w+=1
        elif(i.isalnum()==False):
            e+=1
    print(q,w,e)    
    if (len(a)<=8 and (a.isalpha() or a.isnumeric())):
        print("%s是一个低级密码"%a)
        break;
    elif (len(a)>8 and ((q!=0 and w!=0 and e==0)or( q!=0 and e!=0 and w==0)or( w!=0 and e!=0 and q==0))):#
        print("%s是一个中级密码"%a)
        #break;
    elif(len(a)>16 and a[0].isalpha()and q!=0 and w!=0 and e!=0):
        print("%s是一个高级密码"%a)
        #break
    else:
        print("密码错误请重新输入")
