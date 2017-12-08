
def _odd_iter(): #求1000以内素数
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0 # 返回True 或 False

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break 
'''
def is_hw(n):       #回文联1
    return str(n)==str(n)[::-1]
    
def is_palindrome(n):   #回文联2
    res=str(n)
    for j in range(int(n/2)+1):
        first = res[0]
        end = res[-1]
        if first==end:
            res=res[1:-1]
        else:
            return False
        return True

output = filter(is_hw, range(1, 200))
print('1~200:', list(output))
'''

'''
def is_palindrome(n):
    n=str(n)
    for j in range(int(len(n)/2+1)):
        first = n[0]
        end = n[-1]
        if first==end:
            n=n[1:-1]
        else:
            return True
    return False

output = filter(is_palindrome, range(1, 200))
print('1~1000:', list(output))
'''
