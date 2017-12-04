class Demo:
    def __getattr__(self,name):	#在__getattr__中设置
        self.name='Ling'
        return self.name
'''
    def __init__(self):		#在__init__中设置
        self.x='FishC'

    def __getattr__(self,name):
        print('该属性不存在')

'''


