class Myrev:
    def __init__(self,value):
        self.value=value
        self.index=len(value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.value[self.index]
            
