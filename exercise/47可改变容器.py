class Mylist(list):
    def __init__(self,*args):
        super().__init__(args)
        self.count=[]
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self,key):
        self.count[key]+=1
        return super().__getitem__(key)

    def __setitem__(self,key,value):
        self.count[key]+=1
        super().__setitem__(key,value)

    def __delitem__(self,key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self,key):
        return self.count[key]

    def append(self,value):
        self.count.append(0)
        super().append(value)

    def pop(self,key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self,value):
        key=super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self,key,value):
        self.count.insert(key,0)
        super().insert(key,value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()
    '''
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count={}.fromkeys([x for x in self.values],0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[self.values[key]]+=1
        return self.values[key]

    def __setitem__(self,key,values):
        self.count[values]=self.count[self.values[key]]
        del self.count[self.values[key]]
        self.values[key]=values

    def __delitem__(self,key):
        del self.count[self.values[key]]
        del self.values[key]
        

    def index(self,ind):
        return self.count[self.values[ind]]

    def append(self,values):
        self.count[values]=0
        return self.values.append(values)

    def pop(self):
        del self.count[self.values[-1]]
        self.pop=self.values[-1]
        self.values=self.values[0:-1]
        return self.pop

    def remove(self,values):
        if values in self.values:
            inde=self.values.index(values)
            del self.count[self.values[inde]]
            self.values=self.values[:inde]+self.values[inde+1:]
            return self.values
        else:
            print('未找到该元素')        

    def insert(self,key,values):
        self.values=self.values[:key]+[values]+self.values[key:]
        self.count[values]=0

    def extend(self,*values):
        self.values=self.values+[x for x in values]
        return self.values

    def clear(self):
        self.values.clear()
        self.count.clear()

    def reverse(self):
        self.values.reverse()
        return self.values
    '''

    
        
