class Stack:
    z=[]
    for x in z:
        self.push(x)
    def isEmpty(self):
        if self.z==[]:
            return True
        else:
            return False
            
    def push(self,x):
        self.z.append(x)
        
    def pop(self):
        return self.z.pop()

    def top(self):
        return self.z[-1]

    def bottom(self):
        return self.z[0]
    
