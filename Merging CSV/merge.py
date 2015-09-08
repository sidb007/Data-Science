import pandas as pd
import os


path="C:\Users\sidb\Documents\Python data\\to_combine"
path2="C:\Users\sidb\Downloads\Police_Force\Police_Force"
merged=[]

def merge_files(path):
    x=os.listdir(path)
    f_paths=[]
    for i in x:
        f_paths.append(path+"\\"+i)
    f_paths=sorted(f_paths)
    merged=pd.read_csv(f_paths[0],skipinitialspace=True)
    for i in f_paths[1:]:
        temp=pd.read_csv(i,skipinitialspace=True)
        merged=pd.concat([merged,temp],verify_integrity=False)
    return merged

acc_file=merge_files(path2)
acc_file.to_csv(r'C:\Users\sidb\Desktop\python clean fiels\123.csv')    

