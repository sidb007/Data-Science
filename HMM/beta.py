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

def beeta(wordlist):
    beta={}
    bet={}
    bag=wordlist.split()
    for p in prior.keys():
        bet[p]=math.log(1.0)
    beta[bag[len(bag)-1]]=copy.deepcopy(bet)
    for word in list(reversed(range(len(bag)-1))):
        for p in emi_p.keys():
            add=-float("inf")          
            for tr in trans_p.keys():
                add=log_sum(beta[bag[word+1]][tr]+math.log(trans_p[p][tr])+math.log(emi_p[tr][bag[word+1]]),add)
            bet[p]=add
        beta[bag[word]]=copy.deepcopy(bet)
        bet={}
    prob=-float("inf")          
    for i in trans_p.keys():        
        prob=log_sum(math.log(prior[i])+math.log(emi_p[i][bag[0]])+beta[bag[0]][i],prob)
    return prob

for ls in inp:
    at=beeta(ls)
    print at
    
