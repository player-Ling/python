'''
class Nint(int):
    
    def __new__(cls,num):
        num1=0
        if type(num) in [int,float]:
            num=int(num)
            return int.__new__(cls,num)
        else:
            for i in num:
                num1+=ord(i)
            num=num1
            return int.__new__(cls,num)
'''
class Nint(int):
    def __new__(cls,num=0):
        if isinstance(num,str):
            total=0
            for i in num:
                total+=ord(i)
            num=total
        return int.__new__(cls,num)
