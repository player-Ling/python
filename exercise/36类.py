class Rectangle:
    long=10
    width=5

    def setRectLong(self,value):
        self.long=value

    def setRectWidth(self,value):
        self.width=value
    '''
    def getRect(self,value):
        if value=='long':
            return self.long
        elif value=='width':
            return self.width
        else:
            print('wrong')
    '''
    def getRect(self):
        print('矩形长为：%d宽为：%d'%(self.long,self.width))

    def getArea(self):
        return self.long*self.width
'''
class person:
    name='凌'
    def printp(self):
        print(self.name)
'''
