var='HI'

def fun1():
    global var
    var='Baby'
    return fun2(var)

def fun2(var):
    var+='I love you'
    fun3(var)
    return var

def fun3(var):
    var='Ling'

print(fun1())
