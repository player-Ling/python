class Nstr(str):
    def __sub__(self,num):
        #self=self.replace(num,'')
        return self.replace(num,'')
'''
class Nster(str):

    def __sub__(self,b):
        return self if self.find(b)==-1 else self.replace(b,'')   
'''