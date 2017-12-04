import pickle
'''
mb_list=['1\n','2\n','3\n','4\n','5\n','6\n','7\n','8\n','9\n','10\n']
mb_file=open('mb_file.txt','wb')
pickle.dump(mb_list,mb_file)
mb_file.close()
'''
mb_file=open('1.txt','rb')
mb_list2=pickle.load(mb_file)
print(mb_list2)
mb_file.close()

