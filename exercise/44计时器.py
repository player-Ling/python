import time as t
class Mytime:
    def __init__(self):
        self.cou=''
        self.last=[]
        self.begin=0
        self.end=0
        self.biao=['年','月','日','时','分','秒']

    def __str__(self):
        return self.cou

    __repr__=__str__

    def __add__(self,other):
        cou='一共运行了'
        for i in range(6):
            result=self.last[i]+other.last[i]
            if result:
                cou+=str(result)+self.biao[i]
        return cou
        
    
    def start(self):
        self.begin=t.localtime()
        self.cou='请使用stop()方法'
        print('开始计时')

    def stop(self):
        if self.cou=='':
            print('请使用start()方法')
        else:
            self.end=t.localtime()
            print('计时结束')
            self._count()
            print('时间为'+self.cou)
        
        
    def _count(self):
        for i in range(6):
            self.last.append(self.end[i]-self.begin[i])
            if self.last[i]:
                self.cou=str(self.last[i])+self.biao[i]
        self.begin=0
        self.end=0


