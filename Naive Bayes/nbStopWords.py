import math
import copy
import operator
import os
import sys

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
    for j in wlist:
        j=j.lower()
        if vocab.has_key(j):        
            vocab[j]+=1
        else:
            vocab[j]=1
    if i.find('con')==-1:  # not conservative
        nlib+=1
        for j in wlist:
            j=j.lower()
            if lib_list.has_key(j):
                lib_list[j]+=1
            else:
                lib_list[j]=1
    else:
        ncon+=1
        for j in wlist:
            j=j.lower()
            if con_list.has_key(j):
                con_list[j]+=1
            else:
                con_list[j]=1

prior=nlib/(nlib+ncon)

sorted_vocab=sorted(vocab.items(), key=operator.itemgetter(1),reverse=True)

for i in range(int(sys.argv[3])):
    key=sorted_vocab[i][0]
    if vocab.has_key(key):
        del vocab[key]
    if con_list.has_key(key):
        del con_list[key]
    if lib_list.has_key(key):
        del lib_list[key]

new_dict=copy.deepcopy(vocab)
for i in new_dict:
    if new_dict[i]<=2:
        del vocab[i]
        if con_list.has_key(i):
            del con_list[i]
        if lib_list.has_key(i):
            del lib_list[i]

len_c=len(con_list.keys())*1.0
len_l=len(lib_list.keys())*1.0

for j in vocab.keys():
    if con_list.has_key(j)==False:
        con_list[j]=0
    if lib_list.has_key(j)==False:
        lib_list[j]=0

len_vocab=len(vocab.keys())*1.0
#len_vocab=sum(vocab.values())*1.0

q=1

for i in vocab.keys():
    p_wkc=0.0
    nkc=con_list[i]
    p_wkc=(nkc+q)/(len_c+len_vocab*q)    
    con_list[i]=math.log(p_wkc)
    
for i in vocab.keys():
    p_wkl=0.0
    nkl=lib_list[i]
    p_wkl=(nkl+q)/(len_l+len_vocab*q)    
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
#        print "con"+str(con_sum)
#        print "lib"+str(lib_sum)
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
        