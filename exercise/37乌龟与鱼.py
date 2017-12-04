import random as r
import os
import time

legal_x=[0,10]
legal_y=[0,10]
class Turtle:
    def __init__(self):
        self.power=100
        self.x=r.randint(legal_x[0],legal_x[1])#为什么非要用legal_x,y
        self.y=r.randint(legal_x[0],legal_y[1])
    def move(self):
        new_x=self.x+r.choice([1,2,-1,-2])#
        new_y=self.x+r.choice([1,12,-1,-2])

        if new_x<legal_x[0]:#判断是否越界
            self.x=legal_x[0]-(new_x-legal_x[0])
        elif new_x>legal_x[1]:
            self.x=legal_x[1]-(new_x-legal_x[1])
        else:
            self.x=new_x

        if new_y<legal_y[0]:
            self.y=legal_y[0]-(new_y-legal_y[0])
        elif new_y>legal_y[1]:
            self.y=legal_y[1]-(new_y-legal_y[1])
        else:
            self.y=new_y
        self.power-=1
        return (self.x,self.y)#记一记啊，记一记
    def eat(self):
        self.power==20
        if self.power>100:
            self.power=100

class Fish:
    def __init__(self):
        self.x=r.randint(legal_x[0],legal_x[1])
        self.y=r.randint(legal_y[0],legal_y[1])
    def move(self):
        new_x=self.x+r.choice([1,-1])
        new_y=self.y+r.choice([1,-1])

        if new_x<legal_x[0]:#
            self.x=legal_x[0]-(new_x-legal_x[0])
        elif new_x>legal_x[1]:
            self.x=legal_x[1]-(new_x-legal_x[1])
        else:
            self.x=new_x

        if new_y<legal_y[0]:
            self.y=legal_y[0]-(new_y-legal_y[0])
        elif new_y>legal_y[1]:
            self.y=legal_y[1]-(new_y-legal_y[1])
        else:
            self.y=new_y
        return (self.x,self.y)

turtle=Turtle()
fish=[]
for i in range(10):
    new_fish=Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('乌龟赢')
        break
    if not turtle.power:
        print('鱼赢')
        break

    pos=turtle.move()

    for each_fish in fish[:]:#???
        if each_fish.move()==pos:
            turtle.eat()
            fish.remove(each_fish)#怎么没报字典大小改变问题
            print('鱼给吃了一条')

            
'''
def move(wt,jl):#物体移动与距离设置
    blist[wt[0]][wt[1]]='  '
    global ti
    if wt==tor and wt not in fish.values():
        ti-=jl
    mo=random.randint(1,4)
    while jl:
        if mo==1:
            if wt[0]!=10:
                wt[0]+=1
            else:
                wt[0]-=jl
                jl=1
        elif mo==2:
            if wt[1]!=10:
                wt[1]+=1
            else:
                wt[1]-=jl
                jl=1
        elif mo==3:
            if wt[0]!=1:
                wt[0]-=1
            else:
                wt[0]+=jl
                jl=1
        elif mo==4:
           if wt[1]!=1:
                wt[1]-=1
           else:
                wt[1]+=jl
                jl=1
        jl-=1
    

def printG():#打印
    for i in range(12):
        for j in range(12):
            print(blist[i][j],end='')
        print()
    print('乌龟的剩余体力为%s'%ti)
    print('鱼的剩余个数为%s'%ys)

blist = [['  ' for i in range(12)] for i in range(12)]#好好消化！！！！！！

for i in range(12):
    for j in range(12):
        if j==0 or j==11 or i==0 or i==11:
            blist[i][j]='* '
        else:
            blist[i][j]='  '
fish={}
tor=[random.randint(1,10),random.randint(1,10)]
ti=100
ys=10
blist[tor[0]][tor[1]]='w '
for fi in range(10):
    fis=[random.randint(1,10),random.randint(1,10)]
    if fis==tor or fis not in fish.values():
        fish[fi]=fis
        blist[fish[fi][0]][fish[fi][1]]='y '
    else:
        fi-1
        continue
printG()

while ti>0 and ys>0:
    move(tor,2)
    for i in fish:
        if fish[i]!='':
            move(fish[i],1)
            if tor==fish[i]:
                fish[i]=''
                ti+=20
                ys-=1
            else:
                blist[fish[i][0]][fish[i][1]]='y '
    time.sleep(0.2)
    os.system('cls')
    blist[tor[0]][tor[1]]='w '
    printG()
if ti>0:
    print('乌龟赢')
elif ys>0:
    print('鱼赢')
'''
