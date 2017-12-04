class Nstr(str):
    def __lshift__(self,other):
        self=self[other:]+self[:other]
        return self
    def __rshift__(self,other):
        self=self[:-other]+self[-other:]
        return self
