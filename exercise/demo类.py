class Demo:
    '''
    def __getattr__(self,name):
        return ('该属性不存在')

    def __getattribute__(self,name):
        return super().__getattribute__(self,name)

    def __setattr__(self,name,value):
        return super().__setattr__(self,name,value)
    '''
    def __getattr__(self,name):
        self.name='Ling'
        return self.name
