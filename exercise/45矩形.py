class Jx:
    def __init__(self,width=0,high=0):
        self.width=width
        self.high=high
        #self.square=0

    def __setattr__(self,name,value):
        if name=='square':
            self.width=value
            self.high=value
            #super().__setattr__(self.width,value)
            #super().__setattr__(self.high,value)
        else:
            super().__setattr__(name,value)#or
            #self.__dict__[name]=value
            
    def __getattribute__(self,name):
        #print('矩形长为%d,宽为%d'%(self.width,self.high))
        return super().__getattribute__(name) 

    def print(self):
        print('矩形长为%d,宽为%d'%(self.width,self.high))
    
    '''
    def setatt(self,name,value):
        if name==long:
            self.long=value
        elif name=width:
            self.width=value
        
    def setsqu(self,value):
        self.long=self.width  =value

    def delsqu(self):
        del (self.long,self.width)

    def getsqu(self):
        return self.long,self.width

    square=property(getsqu,setsqu,delsqu)
    '''
    
    
