class parent1(object):
    def __init__(self):
        super(parent1,self).__init__()
        print( 'is parent1')  
        print('goes parent1')  
  
class parent2(object):
    def __init__(self):
        super(parent2,self).__init__()
        print ('is parent2') 
        print ('goes parent2')
  
class child1(parent1):
    def __init__(self):
        print('is child1')  
        super(child1,self).__init__()
        print ('goes child1')  
  
class child2 (parent1):
    def __init__(self):
        
        print( 'is child2')  
        super(child2,self).__init__()  
        print ('goes child2')  
  
class child3(parent2):
    def __init__(self):
        
        print ('is child3')  
        super(child3,self).__init__()
        print ('goes child3')  
  
class grandson(child3,child2,child1):
    def __init__(self):
        
        print ('is grandson')  
        #child1.__init__(self)  
        #child2.__init__(self)  
        #child3.__init__(self)
        super(grandson,self).__init__()
        print('goes grandson')  
  
  
if __name__=='__main__':  
    grandson()


#tencent/micromsg/WeiXin
