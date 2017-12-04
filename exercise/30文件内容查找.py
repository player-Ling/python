import os

def print_pos(key_dict):
    key=key_dict.keys()
    keys=sorted(key)
    for each_key in keys:
        print('关键字在第%s行，第%s的位置'%(each_key,str(key_dict[each_key])))

def pos_in_line(line,key):
    pos=[]
    begin=line.find(word)                   #find是什么鬼
    while begin !=-1:
        pos.append(begin+1)
        begin=line.find(word,begin+1)

    return pos

def search_in_file(file_name,word):
    f=open(file_name)
    count=0
    key_dict=dict()

    for each_line in f:
        count+=1
        if word in each_line:
            pos=pos_in_line(each_line,word)
            key_dict[count]=pos
    f.close()
    return key_dict

def search_files(URL,word,pri):
    if os.path.isdir(URL):
        all_files=os.walk(URL)
        txt_files=[]

        for i in all_files:                     #便利所有子目录下的文件
            for each_file in i[2]:
                if os.path.splitext(each_file)[1]=='.txt':
                    each_file=os.path.join(i[0],each_file)#用当前目录试试
                    #each_file=os.getcwd()+os.sep+each_file#不行
                    txt_files.append(each_file)
        for each_txt_file in txt_files:
            key_dict=search_in_file(each_txt_file,word)
            if key_dict:
                print('==========================')
                print('在文件【%s】中找到关键字【%s】'%(each_txt_file,word))
                print_pos(key_dict)
                
    else:
        print('地址有误')

URL=input('请输入要查找的路径')
word=input('请输入要查询的关键字')
pri=('请输入是否要打印关键字'+word+'的具体位置(YES/NO)')
search_files(URL,word,pri)

'''
def find_word(URL,word,pri):
    os.chdir(URL)
    global list1
    for i in os.listdir():
        if os.path.isdir(i)==False:
            if os.path.splitext(i)[1] in ['.txt']:
                of=open(i)
                hs=0
                b=0
                if word in of.read():
                    print('在文件【'+os.getcwd()+os.sep+i+'】中找到关键字【'+word+'】')
                    of.seek(0,0)
                for i1 in of:
                    if i1!='\n':
                        hs+=1
                    if word in i1:
                        for i2 in i1:
                            b+=1
                            if word == i2:
                                list1.append(b)
                        print('关键字出现在第'+str(hs)+'行，第【'+str(list1)+'】个位置')
                        b=0
                    list1=[]
                        
                hs=0
                list1=[]
                of.close()
        else:
            find_word(os.getcwd()+os.sep+i,word,pri)
            os.chdir(os.pardir)
                
    

URL=input('请输入要查找的路径')
word=input('请输入要查询的关键字')
list1=[]
dict1={}
pri=('请输入是否要打印关键字'+word+'的具体位置(YES/NO)')
find_word(URL,word,pri)
'''

