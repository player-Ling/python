import os
def calc():
    a=os.listdir()
    for i in a:
        print(i+'占用'+str(os.path.getsize(i))+"Byte空间")
calc()
