class C:
    def __init__(self,value=24.0):
        self.value=float(value)#不强转会怎样

    def __get__(self,instance,owner):
        return self.value
    
    def __set__(self,instance,value):
        self.value=value

    def __delete__(self,instance):
        del self.value

class H:
    def __get__(self,instance,owner):
        return instance.c*1.8+32

    def __set__(self,instance,value):
        instance.c=(float(value)-32)/1.8
class Temp:
    c=C()
    h=H()

'''
class Myproperty:
    def __init__(self,fget=0,fset=0,fdel=0):
        self.fget=fget
        self.fset=fsets
        self.fdelete=fdel

    def __get__(self,instance,owner):
        return self.fget(instance)

    def __set__(self,instance,value):
        return self.fset(instance,value)
    
    def __delete__(self,instance):
        return self.fdelete(instance)
    
class Wd:
    def __init__(self):
        self.s=0 
        self.h=0

    def getX(self,name):
        return self.name
    
    def setX(self,value):
        self.name=value
        
    def delX(self,name):
        del self.name

    s1=Myproperty(getX('s '),setX,delX)
    h1=Myproperty(getX,setX,delX)
'''    
