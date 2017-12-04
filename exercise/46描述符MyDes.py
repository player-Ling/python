class MyDes:
    def __init__(self,value=0,name=''):
        self.name=name
        self.value=value
    def __set__(self,instance,value):
        print('正在改变变量%s'%self.name)
        self.value=value
    def __get__(self,instance,owner):
        print('正在获取变量%s'%self.name)
        return self.value
    def __delete__(self,instance):
        print('正在删除变量%s'%self.name)
        print('这个变量无法删除')
class Test:
    x=MyDes(10,'x')
    
    
