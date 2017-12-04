class Counter:
    def __init__(self):
        self.count=-1
        #super().__setattr__('c',0)

    def __setattr__(self,name,value):
        super().__setattr__(name,value)
        super().__setattr__('c',self.count+1)

    def __delattr__(self,name):
        self.c-=1
        super().__delattr__(name)

    '''
    def __getattr__(self,name):
        return ('没有该属性')
    
    def __setattr__(self,name,value):        
        super().__setattr__(name,value)
        #self.count+=1

    def __getattribute__(self,name):
        if name=='counter':
            return self.count
        else:
            return self.name
    '''
