class Foo:
    def foo(self):
        self.foo='I love FishC.com'
        return self.foo
'''
class Foo:
    def __init__(self):
        self.foo='I love FishC.com'
    def foo(self):
        self.foo='I love FishC.com'
        return self.foo
'''
    
