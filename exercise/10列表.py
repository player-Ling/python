member=['小甲鱼','黑夜','迷途','已经','余弦']
'''
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.insert(9,88)
'''
member=['小甲鱼',88,'黑夜',90,'迷途',85,'已经',90,'余弦',88]
#member.extend(member)
#for i in member:
#    print(i)

for i in range(len(member)):
    if i%2==0:
        print(member[i],member[i+1])

'''
for i in range(len(member)):
    print(member[i])
'''    
'''
i=0
while i<len(member):
    print(member[i])
    i+=1
'''
print(member)
