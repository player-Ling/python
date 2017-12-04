Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=1,2,3
>>> type(a)
<class 'tuple'>
>>> b=1,
>>> type(b)
<class 'tuple'>
>>> temp='L','i','n','g'
>>> temp
('L', 'i', 'n', 'g')
>>> type(temp)
<class 'tuple'>
>>> temp=temp[:1]+'asdf'+[1:]
SyntaxError: invalid syntax
>>> temp=temp[:1]+''+temp[1:]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    temp=temp[:1]+''+temp[1:]
TypeError: can only concatenate tuple (not "str") to tuple
>>> temp=temp[:1]+temp=temp[:1]+'asdf',+temp[1:]
SyntaxError: can't assign to operator
>>> temp=temp[:1]+('asdf',)+temp[1:]
>>> temp
('L', 'asdf', 'i', 'n', 'g')
>>> 

>>> temp1=(x for x in range(10))
>>> temp1
<generator object <genexpr> at 0x000000000326A150>
>>> temp1=[x form x in range(10)]
SyntaxError: invalid syntax
>>> temp1=[x for x in range(10)]
>>> temp1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(temp1)
<class 'list'>
>>> temp2=(x for x in range(10))
>>> type(temp2)
<class 'generator'>
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 1, in <module>
    dir(string)
NameError: name 'string' is not defined
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 1, in <module>
    dir(__string__)
NameError: name '__string__' is not defined
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 1, in <module>
    dir(__str__)
NameError: name '__str__' is not defined
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
sdfqwer
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
123412341234
>>> str1=""
>>> str1="\"
SyntaxError: EOL while scanning string literal
>>> str1="asdf\asdf"
>>> str1=("asdfasdf"
	）
      
SyntaxError: invalid character in identifier
>>> str1()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    str1()
TypeError: 'str' object is not callable
>>> str1="asdf
        \asdf"
        
SyntaxError: EOL while scanning string literal
>>> str1=(asdf
        asdf)
SyntaxError: invalid syntax
>>> str1=("asdf"
		"asdf")
>>> str1
'asdfasdf'
>>> str1="asdf"
        \"asdf"
        
SyntaxError: multiple statements found while compiling a single statement
>>> str1="asdf\
        asdf"
>>> str1
'asdf        asdf'
>>> file=open('C:\Users\Ling\Desktop')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> (C:\Users\Ling\Desktop)
SyntaxError: invalid syntax
>>> ("C:\Users\Ling\Desktop")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> open("C:\Users\Ling\Desktop")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> file1 = open('C:\Users\Ling\Desktop', 'r')

SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
>>> str1.split(/)
SyntaxError: invalid syntax
>>> str1.split("/")
['<a href="http:', '', 'www.fishc.com', 'dvd" target="_blank">鱼C资源打包<', 'a>']
>>> str2=str1.split('/')[1]
>>> str2
''
>>> str1
'<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
>>> str2=str1.split('/')[0]
>>> str
<class 'str'>
>>> str2
'<a href="http:'
>>> str2=str1.split('/')[2]
>>> str2
'www.fishc.com'
>>> str1
'<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
>>> str1.rfind("/")
58
>>> str1[58,-13]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    str1[58,-13]
TypeError: string indices must be integers
>>> str1[58,13]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    str1[58,13]
TypeError: string indices must be integers
>>> str1[58]
'/'
>>> str1[58:-13]
''
>>> str1[58:13]
''
>>> str1.find("/")
14
>>> str1[14:]
'//www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
>>> str1[16,13]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    str1[16,13]
TypeError: string indices must be integers
>>> str1[16:13]
''
>>> str1[16:29]
'www.fishc.com'
>>> str1[16:-1]
'www.fishc.com/dvd" target="_blank">鱼C资源打包</a'
>>> str1[16,-30]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    str1[16,-30]
TypeError: string indices must be integers
>>> str1[16,-13]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    str1[16,-13]
TypeError: string indices must be integers
>>> str1[16:-30]
'www.fishc.com/d'
>>> str1[17:-28]
'ww.fishc.com/dvd'
>>> str1[16:-32]
'www.fishc.com'
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> for i in range(str1)
SyntaxError: invalid syntax
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 12, in <module>
    for i in range(str1):
TypeError: 'str' object cannot be interpreted as an integer
>>>  for i in range(str1):
	 
SyntaxError: unexpected indent
>>> for i in range(str1):
	print(str1[i])

	
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    for i in range(str1):
TypeError: 'str' object cannot be interpreted as an integer
>>> str1[1]
'2'
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 2, in <module>
    for i in range(str1):
TypeError: 'str' object cannot be interpreted as an integer
>>> str1[0]==char
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    str1[0]==char
NameError: name 'char' is not defined
>>> str1[0]
'i'
>>> type(str1[0])
<class 'str'>
>>> str1[0]==char
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    str1[0]==char
NameError: name 'char' is not defined
>>> str1[0]==str
False
>>> str1[0]==int
False
>>> str1[1]==int
False
>>> str1[0].isalpha
<built-in method isalpha of str object at 0x00000000023A0FB8>
>>> str1[i].isalpha()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    str1[i].isalpha()
NameError: name 'i' is not defined
>>> str1[1].isalpha()
False
>>> str1[0].isalpha()
True
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 2, in <module>
    for i in range(str1):
TypeError: 'str' object cannot be interpreted as an integer
>>> for i in range(str1):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    for i in range(str1):
TypeError: 'str' object cannot be interpreted as an integer
>>> while(str1)
SyntaxError: invalid syntax
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 2, in <module>
    for i in range(str1):
TypeError: 'str' object cannot be interpreted as an integer
>>> for i in range(str1):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    for i in range(str1):
TypeError: 'str' object cannot be interpreted as an integer
>>> for i in str1:
	print(i)

	
i
2
s
l
5
4
o
v
v
v
b
4
e
3
b
f
e
r
i
3
2
s
5
6
h
;
$
c
4
3
.
s
f
c
6
7
o
0
c
m
9
9
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 3, in <module>
    if i==char():
NameError: name 'char' is not defined
>>> a=a
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a=a
NameError: name 'a' is not defined
>>> a='a'
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[1].isalpha()
False
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
2
3
2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14字符串.py", line 8, in <module>
    str1=str1.strip(i)
NameError: name 'i' is not defined
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
2
3
2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm
>>> str1.isalpha()
False
>>> str1[0].isalpha()
False
>>> str1[1].isalpha()
True
>>> str1
'2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm'
>>> True
True
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[0].isalpha()
True
>>> str1[1].isalpha()
False
>>> str1=str1.strip(str1[1])
>>> str1
'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1
'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1
'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[1]
'2'
>>> str1=str1.strip('2')
>>> str1
'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> asdf='aaaaaaabbbbbbbaaaaa'
>>> asdf.strip('a')
'bbbbbbb'
>>> str1.strip('2')
'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1.strip('i')
'2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1.strip('2')
'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[1:].strip('2')
'sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1
'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1=str1[1:].strip('2')
>>> str1
'sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[2:].strip('1')
'54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[1]
'2'
>>> str1[1].isprintable
<built-in method isprintable of str object at 0x000000000291DDC0>
>>> str1[1].isalpha()
False
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[0].isalpha()
True
>>> str1=str1[0].isalpha()+str1[2:].isalpha()
>>> str1
1
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1=str1[0]=+str1[2:]
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    str1=str1[0]=+str1[2:]
TypeError: bad operand type for unary +: 'str'
>>> str1=str1[:0]=+str1[2:]
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    str1=str1[:0]=+str1[2:]
TypeError: bad operand type for unary +: 'str'
>>> str1[0]
'i'
>>> str1=str1[:0]+str1[2:]
>>> str1
'sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'

>>> str1=str1[:0]+str1[2:]
>>> str1
'sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1=str1[0]+str1[2:]
>>> str1
'isl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> for i in str1:
	if i.isalphy():
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#152>", line 2, in <module>
    if i.isalphy():
AttributeError: 'str' object has no attribute 'isalphy'
>>> for i in str1:
	print(i)

	
i
s
l
5
4
o
v
v
v
b
4
e
3
b
f
e
r
i
3
2
s
5
6
h
;
$
c
4
3
.
s
f
c
6
7
o
0
c
m
9
9
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
islovvvbebferishcsfcocm
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
i2sl54ovvvb4e3bferi32s56hc43sfc67o0cm99
>>> 
=================== RESTART: D:/编程/python/init/鱼/14字符串.py ===================
2544332564367099
>>> 
str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
>>> str1[::3]
'ilovefishc.com'
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
>>> 1234
1234
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
>>> qwer
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    qwer
NameError: name 'qwer' is not defined
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
>>> 1234qwer
SyntaxError: invalid syntax
>>> 'asdf2341'
'asdf2341'
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
>>> 1234qer
SyntaxError: invalid syntax
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
>>> 1234
1234
>>> 1234
1234
>>> 1234
1234
>>> 1234
1234
>>> 1234
1234
>>> 123
1234
>>> 123
123
4
>>> 123
123
4
>>> 1
1
32
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码1234
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 11, in <module>
    print("%d是一个低级密码"%a)
TypeError: %d format: a number is required, not str
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码asdf1234
密码错误请重新输入
来输入一个密码1234
1234是一个低级密码
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
12344567456errwer!
12344567456errwer!是一个中级密码
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
a1234123412341234123412341234
a1234123412341234123412341234是一个中级密码
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
aqw4123412341234123rdf13r12f13f123f123f
aqw4123412341234123rdf13r12f13f123f123f是一个中级密码
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
1234123412341@@@@@1234
1234123412341@@@@@1234是一个中级密码
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
wqwerqwer@@@@@!!!$!$!$$!$$!$
wqwerqwer@@@@@!!!$!$!$$!$$!$是一个中级密码
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
qwer@@@@@@
qwer@@@@@@是一个中级密码0
来输入一个密码
来输入一个密码
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 2, in <module>
    a=input("来输入一个密码\n")
KeyboardInterrupt
>>> a=1234123werqwer!!!
SyntaxError: invalid syntax
>>> a='asdf1234@@@@'
>>> a.isalnum
<built-in method isalnum of str object at 0x0000000003278F70>
>>> a.isalnum()
False
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
qwer@@@
密码错误请重新输入
来输入一个密码
qwer1234
密码错误请重新输入
来输入一个密码
1234
1234是一个低级密码
>>> 
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
a123412341234123412341
a123412341234123412341是一个中级密码0
来输入一个密码
a@@@@@@@@@@@@@@@@@@@@@@@@@@@@12341234
a@@@@@@@@@@@@@@@@@@@@@@@@@@@@12341234是一个中级密码0
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
a@@@@@@@@@@@@@@@@@@@@@@
a@@@@@@@@@@@@@@@@@@@@@@是一个中级密码---0
来输入一个密码
1234@@@@@@@@@@@@@@@@@@@
1234@@@@@@@@@@@@@@@@@@@是一个中级密码---0
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
qwe@@@@@@@@@@@@@@@@@@
qwe@@@@@@@@@@@@@@@@@@是一个中级密码---0
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
11234@@@@@@@@2
0
11234@@@@@@@@2是一个中级密码---0
来输入一个密码
0Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 8, in <module>
    print(c)
KeyboardInterrupt
>>> a=input()
qwer@@@@@@@@@@@@@
>>> a.isalnum
<built-in method isalnum of str object at 0x0000000002FA9D68>
>>> a.isalnum()
False
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
qwer@@@@@@@@@@@@@@@@@@
1
qwer@@@@@@@@@@@@@@@@@@是一个中级密码---1
来输入一个密码
1@@@@@@@@@@@@@@@@@@@@@@@@
1
1@@@@@@@@@@@@@@@@@@@@@@@@是一个中级密码---1
来输入一个密码
1234############@@@@@@@！！！！！！！！！！！qwer
1
1234############@@@@@@@！！！！！！！！！！！qwer是一个中级密码---1
来输入一个密码
1q
0
密码错误请重新输入
来输入一个密码
qwer12344
0
qwer12344是一个中级密码---0
来输入一个密码
1234@@@@@@@@@@@
1
1234@@@@@@@@@@@是一个中级密码---1
来输入一个密码
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 2, in <module>
    a=input("来输入一个密码\n")
KeyboardInterrupt
>>> a='1234@@@@@@@@@@@'
>>> alen(a)>8 and (a.isalpha and a.isnumeric ))
SyntaxError: invalid syntax
>>> alen(a)>8 and (a.isalpha and a.isnumeric )
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    alen(a)>8 and (a.isalpha and a.isnumeric )
NameError: name 'alen' is not defined
>>> len(a)>8 and (a.isalpha and a.isnumeric )
<built-in method isnumeric of str object at 0x0000000002F18AF0>
>>> len(a)>8
True
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
111@@@@@@@@@@@
1
密码错误请重新输入
来输入一个密码
qwer@@@@@@@@@@@@@
1
qwer@@@@@@@@@@@@@是一个高级密码
来输入一个密码
11qwer@@@@@@
1
密码错误请重新输入
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
123412@@@@@@@@@@
1
密码错误请重新输入
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
1@@@@@@@@@@@@@@@@@@@@@@@
1
1@@@@@@@@@@@@@@@@@@@@@@@是一个高级密码
来输入一个密码
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 2, in <module>
    a=input("来输入一个密码\n")
KeyboardInterrupt
>>> a='qwer1234'
>>> for i in a
SyntaxError: invalid syntax
>>> for i in a:
	if(type(i)==int):
		print(i)

		
>>> 
>>> type(a[1])
<class 'str'>
>>> for i in a:
	if(a[i].isnumeric):
		print(i)

		
Traceback (most recent call last):
  File "<pyshell#194>", line 2, in <module>
    if(a[i].isnumeric):
TypeError: string indices must be integers
>>> for i in a:
	if(i.isnumeric):
		print(i)

		
q
w
e
r
1
2
3
4
>>> for i in a:
	if(i.isnumeric()):
		print(i)

		
1
2
3
4
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
1234qwer!!!
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 16, in <module>
    print(c)
NameError: name 'c' is not defined
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
1234qwer
密码错误请重新输入
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
qwer1234
0 0 8
密码错误请重新输入
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
1234qwer
4 4 0
密码错误请重新输入
来输入一个密码
qwer12341234
8 4 0
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 20, in <module>
    print("%s是一个中级密码---%d"%(a,c))
NameError: name 'c' is not defined
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
1234qwerq
4 5 0
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 20, in <module>
    print("%s是一个中级密码---%d"%a)
TypeError: not enough arguments for format string
>>> 
================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
qwer12341234
8 4 0
qwer12341234是一个中级密码
来输入一个密码
1234qwer!@
4 4 2
1234qwer!@是一个中级密码
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
qwer1234@@
4 4 2
密码错误请重新输入
来输入一个密码
1234qwerqwerr@@@@@@@@@@@@@@
4 9 14
1234qwerqwerr@@@@@@@@@@@@@@是一个高级密码
来输入一个密码

================== RESTART: D:/编程/python/init/鱼/14check.py ==================
来输入一个密码
1234qwerqwer@@@@@@@@
4 8 8
密码错误请重新输入
来输入一个密码
qwer123@@@@@@@@@@@@@@
3 4 14
qwer123@@@@@@@@@@@@@@是一个高级密码
来输入一个密码
12342qwerqwer
5 8 0
12342qwerqwer是一个中级密码
来输入一个密码
1234@@@@@@@@@@
4 0 10
1234@@@@@@@@@@是一个中级密码
来输入一个密码
@@@@@@@@@@@qwer
0 4 11
@@@@@@@@@@@qwer是一个中级密码
来输入一个密码
12341234qwerqwer
8 8 0
12341234qwerqwer是一个中级密码
来输入一个密码
Traceback (most recent call last):
  File "D:/编程/python/init/鱼/14check.py", line 2, in <module>
    a=input("来输入一个密码\n")
KeyboardInterrupt
>>> str1 = '''待我长发及腰，将军归来可好？
此身君子意逍遥，怎料山河萧萧。
天光乍破遇，暮雪白头老。
寒剑默听奔雷，长枪独守空壕。
醉卧沙场君莫笑，一夜吹彻画角。
江南晚来客，红绳结发梢。'''

>>> str
<class 'str'>
>>> str1
'待我长发及腰，将军归来可好？\n此身君子意逍遥，怎料山河萧萧。\n天光乍破遇，暮雪白头老。\n寒剑默听奔雷，长枪独守空壕。\n醉卧沙场君莫笑，一夜吹彻画角。\n江南晚来客，红绳结发梢。'
>>> str1 = ''待我长发及腰，将军归来可好？
此身君子意逍遥，怎料山河萧萧。
天光乍破遇，暮雪白头老。
寒剑默听奔雷，长枪独守空壕。
醉卧沙场君莫笑，一夜吹彻画角。
江南晚来客，红绳结发梢。''
SyntaxError: invalid character in identifier
>>> str2 = '待卿长发及腰，我必凯旋回朝。\
昔日纵马任逍遥，俱是少年英豪。\
东都霞色好，西湖烟波渺。\
执枪血战八方，誓守山河多娇。\
应有得胜归来日，与卿共度良宵。\
盼携手终老，愿与子同袍。'

>>> str2
'待卿长发及腰，我必凯旋回朝。昔日纵马任逍遥，俱是少年英豪。东都霞色好，西湖烟波渺。执枪血战八方，誓守山河多娇。应有得胜归来日，与卿共度良宵。盼携手终老，愿与子同袍。'
>>> file1 = open('C:\windows\temp\readme.txt')
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    file1 = open('C:\windows\temp\readme.txt')
OSError: [Errno 22] Invalid argument: 'C:\\windows\temp\readme.txt'
>>> file1 = open(r'C:\windows\temp\readme.txt', 'r')
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    file1 = open(r'C:\windows\temp\readme.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\windows\\temp\\readme.txt'
>>> file1 = open(r'C:\Users\Ling\Desktop\study.txt', 'r')
>>> 
KeyboardInterrupt
>>> 
>>> file1 = open('C:\Users\Ling\Desktop\study.txt', 'r')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> file1
<_io.TextIOWrapper name='C:\\Users\\Ling\\Desktop\\study.txt' mode='r' encoding='cp936'>
>>> str1 = '<a href="http://www.fishc.com/dvd" target="_blank">
SyntaxError: EOL while scanning string literal
>>> str1 = '<a href="http://www.fishc.com/dvd" target="_blank">'
>>> str2=str1.split('/')[2]
>>> str2
'www.fishc.com'
>>> str3=str1[16:29]
>>> str3
'www.fishc.com'
>>> str5=str1[-45:-32]
>>> str5
'f="http://www'
>>> str5=str1[-30:-32]
