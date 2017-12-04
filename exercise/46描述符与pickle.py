import time
import os
import pickle
class MyDes:
    saved=[]
    def __init__(self,name=None):
        self.name=name
        self.filename=self.name+'.txt'

    def __get__(self,instance,owner):
        if self.name not in MyDes.saved:
            raise AttributeError('%s属性还没有赋值！'%self.name)#what the fuck

        with open(self.filename,'rb')as f:
            value=pickle.load(f)

        return value

    def __set__(self,instance,value):
        with open(self.filename,'wb')as f:
            pickle.dump(value,f)
            MyDes.saved.append(self.name)

    def __delete__(self,instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)
    
    '''
    def __init__(self,name='',value=''):#没有用pickle的方法
        self.value=value
        self.name=name
        self.word=''
    def __get__(self,instance,owner):
        return self.value

        
    def __set__(self,instance,value):
        self.value=value
        f=open(self.name+'.txt','at')
        self.word=str(self.value)
        f.write(self.word)
        f.close
    def __delete__(self,instance):
        del self.value
        del self.word
        os.remove(self.name+'.txt')
    '''
class Test:
    x=MyDes('x')
    y=MyDes('y')
