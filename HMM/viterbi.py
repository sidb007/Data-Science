import csv
import sys
import numpy as np
import math
import copy
#a=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\hmm-emit.txt','r')
a=open(sys.argv[3],'r')
b=open(sys.argv[2],'r')
c=open(sys.argv[4],'r')
d=open(sys.argv[1],'r')
#c=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\hmm-prior.txt','r')
#b=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\hmm-trans.txt','r')
#d=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\\dev.txt','r')
emi_p={}
trans_p={}
prior={}
em_p=a.read().splitlines()

def log_sum(left,right):
	if right < left:
		return left + math.log1p(math.exp(right - left))
	elif left < right:
		return right + math.log1p(math.exp(left - right));
	else:
		return left + math.log1p(1)


# dict of dict for emmision 
for t in em_p:
    s=t.split()
    word_p={}    
    for ss in s[1:]:
        sss=ss.split(':')
        word_p[sss[0]]=(float(sss[1]))
    emi_p[s[0]]=word_p


tr_p=b.read().splitlines()
# dict of dict for transition 
for t in tr_p:
    s=t.split()
    word_p={}    
    for ss in s[1:]:
        sss=ss.split(':')
        word_p[sss[0]]=(float(sss[1]))
    trans_p[s[0]]=word_p


    
    
# dict of dict for prior state prob
tr_pri=c.read().splitlines()
for t in tr_pri:
    s=[]
    s=t.split()
    prior[s[0]]=(float(s[1]))


   
inp=d.read().splitlines()

aa=[]
def alfa(wordlist):
    alpha=[]
    alp={}
    #punct=['.',',','?','\'','\"',';',':']
    bag=wordlist.split()
    for p in prior.keys():
        alp[p]=prior[p]*emi_p[p][bag[0]]
    alpha.append(alp)
    alp={}
    for word in bag[1:]:
        #if word not in punct:
        for p in emi_p.keys():
            bi=emi_p[p][word]
            add=0.0            
            for tr in trans_p.keys():
                add=alpha[len(alpha)-1][tr]*trans_p[tr][p]+add
            alp[p]=bi*add
        alpha.append(alp)
        alp={}
    return alpha[len(alpha)-1]

def bitervi(wordlist):
    vp={}
    q={}
    alp={}    
    bag=wordlist.split()
    for p in prior.keys():
        alp[p]=math.log(prior[p])+math.log(emi_p[p][bag[0]])
    vp[bag[0]]=copy.deepcopy(alp)
    temp1={}    
    for i in alp.keys():
        temp1[i]=bag[0]+"_"+i
    q[bag[0]]=temp1
    alp={}
    for word in range(1,len(bag)):
        tv={}
        tq={}            
        for i in emi_p.keys():
            temp={}
            for j in trans_p.keys():
                temp[j]=vp[bag[word-1]][j]+math.log(trans_p[j][i])+math.log(emi_p[i][bag[word]])
            tv[i]=max(temp.values())
            for key,value in temp.iteritems():
                if tv[i]==value:
                    tq[i]=q[bag[word-1]][key]+" "+bag[word]+"_"+i
        vp[bag[word]]=tv
        q[bag[word]]=tq
    m=max(vp[bag[len(bag)-1]].values())
    for key,value in vp[bag[len(bag)-1]].iteritems():
        if m==value:
            print q[bag[len(bag)-1]][key]
        
for lis in inp:
    bitervi(lis)

#bitervi(inp[17])
    

         