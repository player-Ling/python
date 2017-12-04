'''
def add(x):
    return x%2

temp=range(10)
show=filter(add(),temp)
'''
print(list(filter(lambda x:x % 2,range(10))))
