import math
import os
import sys

#path="C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw9"
#split_files=[]
#txt_files=os.listdir(path)
#for i in txt_files:
#    if (i.find('split')!=-1):
#        if i.find('split')==0:
#            split_files.append(i)

o=open(sys.argv[1])
v_files=o.read().splitlines()

wlist=[]
con_list={}
lib_list={}
vocab={}
nlib=0.0
ncon=0
prior=0.0

for i in v_files:
    o=open(i)
    wlist=o.read().splitlines()
    if i.find('con')==-1:  # not conservative
        nlib+=1
        for j in wlist:
            vocab[j.lower()]=1
            if lib_list.has_key(j.lower())==False:
                lib_list[j.lower()]=1
            else:
                lib_list[j.lower()]+=1
    else:
        ncon+=1
        for j in wlist:
            vocab[j.lower()]=1
            if con_list.has_key(j.lower())==False:
                con_list[j.lower()]=1
            else:
                con_list[j.lower()]+=1

len_c=len(con_list.keys())*1.0
len_l=len(lib_list.keys())*1.0

for j in vocab.keys():
    if con_list.has_key(j)==False:
        con_list[j]=0
    if lib_list.has_key(j)==False:
        lib_list[j]=0
        

prior=nlib/(nlib+ncon)
cc=0


#len_vocab=len(vocab.keys())*1.0
len_vocab=sum(vocab.values())


for i in vocab.keys():
    p_wkc=0.0
    nkc=con_list[i]
    p_wkc=(nkc+1)/(len_c+len_vocab)    
    con_list[i]=math.log(p_wkc)
    
for i in vocab.keys():
    p_wkl=0.0
    nkl=lib_list[i]
    p_wkl=(nkl+1)/(len_l+len_vocab)    
    lib_list[i]=math.log(p_wkl)
    
o1=open(sys.argv[2])
v_files1=o1.read().splitlines()

def test(filename):
    o2=open(filename)
    wlist=o2.read().splitlines()
    #con
    con_sum=0.0
    lib_sum=0.0
    for i in wlist:
        i=i.lower()        
        if con_list.has_key(i):
           con_sum+=con_list[i]            
        if lib_list.has_key(i):
            lib_sum+=lib_list[i]
    con_sum*=(1-prior)
    lib_sum*=prior
    if lib_sum>con_sum:
        return 'L'
    else:
        return 'C'

acc=0.0    
for i in v_files1:
    res=test(i)
    act=i[0].upper()
    if res==act:
        acc+=1
    print res
acc/=len(v_files1)    
print (round(acc,4))
