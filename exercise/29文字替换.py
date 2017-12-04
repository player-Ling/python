def change():
    f=open(input('请输入文件名'),'a+')
    word=input('请输入需要替换的单词或字符')
    c_word=input('请输入新的单词或字符')

    content=[]#
    count=0#

    for i in f:
        if word in i:
            count=i.count(word)#没看懂
            i=i.replace(word,c_word)
        content.append(i)

    print('文件%s中共有%d个【%s】'%(f,count,word))
    print('您确定要把所有的【%s】换为【%s】吗？'%(word,c_word))
    p=input('【YES/NO】')

    if p in ['YES','Yes','yes']:
        f.writelines(content)#又没看懂
        
    f.close()
    
change()
