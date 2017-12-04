'''
#ÊÓÆµ´ğ°¸
class count():
    num=0
    def __init__(self):
        self.num+=10
        count.num+=1

    def __del__(self):
        self.num-=10
        count.num-=1
'''
class a:
    c=0
    def __init__(self):
        a.c+=1
        self.c=100
    def __del__(self):
        a.c-=1
        del self
    
