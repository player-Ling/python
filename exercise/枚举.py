from enum import Enum,unique

@unique
class Gender(Enum):
    male=0
    female=1

class Student:
    
    def __init__(self,name,gender):
        if gender!=0 and gender!=1:
            raise TypeError('gender must be 0 or 1!')
        gen=Gender(gender)
        self.name=name
        self.gender=gen.name #gen.name=male/female gen.value=0/1
        
    def pr(self):
        print('%s is %s'%(self.name,self.gender))

