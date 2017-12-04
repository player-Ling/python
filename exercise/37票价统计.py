'''
#方法1
class Ticket:
    price=100
    chil_price=50
    def weekend(self):
        price*=1.2
        chil_price*=1.2
    def count(self,num,cnum):
        return num*self.price+cnum*self.chil_price

t=Ticket
print(Ticket.count(t,2,1))
'''
'''
#方法2
class Pj:
    old=0
    young=0
    time='YES'
    t1=1
    def enter(self):
        self.old=input('请输入成人数')
        self.young=input('请输如儿童人数')
        self.time=input('请输入是否是节假日(YES or NO)')
        if self.time not in ['YES','NO','Yes','No','yes','no']:
            print('请重新输入%s'%self.time)
            self.enter()
            
    def count(self):
        self.t1=[1.2 if self.time == 'YES' or 'Yes' or 'yes' else 1]
            
            
        print('票价为%d'%((int(self.old)*100+int(self.young)*50)*self.t1[0]))
'''
class Ticket():
    def __init__(self,weekend=False,child=False):
        self.exp=100
        if weekend:
            self.inc=1.2
        else:
            self.inc=1
        if child:
            self.discount=0.5
        else:
            self.discount=1

    def calcPrice(self,num):
        return self.exp*self.inc*self.discount*num

adult=Ticket()
child=Ticket(child=True)
print('2个成人+1个小孩的票价为：%d'%(adult.calcPrice(2)+child.calcPrice(1)))
