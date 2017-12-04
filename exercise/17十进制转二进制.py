def bb(x):
    bi=''
    while(x/2!=0):
        if(x%2==0):
            bi='0'+bi
        else:
            bi='1'+bi
        x//=2
    return bi

'''
def Dec2Bin(dec):
    temp = []
    result = ''
    
    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.append(quo)
 
    while temp:
        result += str(temp.pop())
    
    return result
'''
