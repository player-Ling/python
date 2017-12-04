import time
import os
class Record:
    def __init__(self,value=0,name=''):
        self.name=name
        self.value=value

    def __get__(self,instance,owner):
        f=open('record.txt','at')
        f.write('变量%s于北京时间%s被读取%s=%s\n'%(self.name,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),self.name,self.value))
        f.close()
        return self.value
    def __set__(self,instance,value):
        self.value=value
        f=open('record.txt','at')
        f.write('变量%s于北京时间%s被修改%s=%s\n'%(self.name,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),self.name,self.value))
        f.close()
    def __delete__(self,instance):
        del self.value

class T:
    x=Record(10,'x')
    y=Record(8.8,'y')
