class Nstr:
    '''
    num=0
    def __init__(self,num):
        for i in num:
            self.num+=ord(i)

    def __add__(self,num1):
        return self.num+num1.num

    def __sub__(self,num1):
        return self.num-num1.num

    def __mul__(self,num1):
        return self.num*num1.num

    def __floordiv__(self,num1):
        return self.num//num1.num

    def __truediv__(self,num1):
        return self.num/num1.num
    '''
    def __new__(cls,arg=0):
        if isinstance(arg,str):
            num=0
            for i in arg:
                num+=ord(i)
            arg=num
            return int.__new__(cls,arg)
