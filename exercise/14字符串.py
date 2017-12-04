str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
a=0

for i in str1:
    if str1[a].isnumeric():
        a+=1
        #print(a)
    else:
        str1=str1[:a]+str1[a+1:]
print(str1)

"""
str1="asdfqwer"
str2=str1[1:]
#print(str2)
str1='123412341234'
print(str1)
 
str1="asdf
        asdf"
"""

