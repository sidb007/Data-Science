import csv
import sys
import numpy as np
import math
import copy
#a=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\hmm-emit.txt','r')
#c=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\hmm-prior.txt','r')
#b=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\hmm-trans.txt','r')
#d=open('C:\Users\sidb\Documents\Python Important Scripts\Working Dir\hw10-data\\dev.txt','r')
a=open(sys.argv[3],'r')
b=open(sys.argv[2],'r')
c=open(sys.argv[4],'r')
d=open(sys.argv[1],'r')
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
        alp[p]=math.log(prior[p])+math.log(emi_p[p][bag[0]])
    alpha.append(alp)
    alp={}
    for word in bag[1:]:
        #if word not in punct:
        for p in emi_p.keys():
            bi=emi_p[p][word]
            add=-float("inf")
            for tr in trans_p.keys():
                add=log_sum(alpha[len(alpha)-1][tr]+math.log(trans_p[tr][p])+math.log(bi),add)
            alp[p]=add
        alpha.append(alp)
        alp={}
    return alpha[len(alpha)-1]

  
 

#prob=0.0
#for i in trans_p.keys():
#    prior[i]*emi_p[i][]
    
def prob(at):
    add=-float("inf")
    for key in at.keys():
    #add=log_sum(add,at[key])
        add=log_sum(at[key],add)
    return add
    

#
#for lis in inp:
#    at=alfa(lis)
#    try:    
#        print prob(at)       
#    except ValueError:
#        print 0.00
#
for lis in inp:
    at=alfa(lis)
    print prob(at)       
        

         