class Word(str):
    def __new__(self,s):
        #for i in s:
        if ' ' in s:
            s=s[:s.index(' ')]
        return str.__new__(self,s)

    def __it__(self,other):
        if len(self)<len(other):
            return True
        else:
            return False

    def __ie__(self,other):
        if len(self)<=len(other):
            return True
        else:
            return False

    def __gt__(self,other):
        if len(self)>len(other):
            return True
        else:
            return False

    def __ge__(self,other):
        '''
        if len(self)>=len(other):
            return True
        else:
            return False
        '''
        return len(self)>=len(other)
