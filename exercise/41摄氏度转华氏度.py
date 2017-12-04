class C2f(int):
    def __new__(cls,nt):
        nt=nt*1.8+32
        return int. __new__(cls,nt)
