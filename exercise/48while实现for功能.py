it=iter(range(5))
while True:
    try:
        each=next(it)
    except StopIteration:
        break
    print(each)
