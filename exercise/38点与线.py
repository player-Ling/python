import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
class Line():
    def count(x,y):
        #print(x.x)
        #print(x.y)
        #print(y.x)
        #print(y.y)
        return  math.sqrt(((x.x-y.x)*(x.x-y.x))+((x.y-y.y)*(x.y-y.y)))
