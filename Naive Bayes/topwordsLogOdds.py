import math
import sys
import operator

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

prior=nlib/len(v_files)

len_vocab=len(vocab.keys())*1.0

for i in vocab.keys():
    p_wkc=0.0
    p_wkl=0.0
    
    nkl=lib_list[i]
    p_wkl=(nkl+1)/(len_l+len_vocab)    
    nkc=con_list[i]
    p_wkc=(nkc+1)/(len_c+len_vocab)    
    
    lib_list[i]=math.log(p_wkl/p_wkc)
    con_list[i]=math.log(p_wkc/p_wkl)
       
sorted_con = sorted(con_list.items(), key=operator.itemgetter(1),reverse=True)
sorted_lib = sorted(lib_list.items(), key=operator.itemgetter(1),reverse=True)

for i in range(20):
    print str(sorted_lib[i][0])+" "+str(round(math.exp(sorted_lib[i][1]),4))
print 
for i in range(20):
    print str(sorted_con[i][0])+" "+str(round(math.exp(sorted_con[i][1]),4))
