def triangles():
    list1=['','','','','',1,'','','','','']
    #print(list1)
    while 1:
        yield list1
        list2 = []
        for i in range(11):
            try:
                if type(list1[i - 1]) == int or type(list1[i + 1]) == int:
                    if type(list1[i - 1]) == int and type(list1[i + 1]) == int:
                        index = list1[i - 1] + list1[i + 1]
                        list2.append(index)
                    elif type(list1[i - 1]) == int:
                        list2.append(list1[i - 1])
                    elif type(list1[i + 1]) == int:
                        list2.append(list1[i + 1])
                else:
                    list2.append('')
            except IndexError:
                list2.append(list1[i - 1])
        list1=list2

n=0
for i in triangles():
    n+=1
    if n<7:
        print(i)
