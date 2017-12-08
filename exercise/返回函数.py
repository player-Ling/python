'''
def createCounter():
    res=0
    def counter():
        nonlocal res #nonlocal可以自由地操作外层作用域中的变量！
        res+=1
        return res
    return counter
'''
def createCounter():
    def counter():
        i = 1
        while True:
            yield i
            i += 1
    return counter().__next__

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
