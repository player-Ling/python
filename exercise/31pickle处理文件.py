import pickle

def save_file(file,data):
    f1=open(file,'wb')
    pickle.dump(data,f1)
    f1.close()
    
def split_file(file_name):
    count=1
    single=[]
    double=[]
    f=open(file_name)
    count=0
    for i in f:
        count+=1
        if count%2:
            single.append(i)
        else:
            double.append(i)
    save_file('single.txt',single)
    save_file('double.txt',double)

    single=[]
    double=[]
    f.close()
    
split_file('2.txt')
