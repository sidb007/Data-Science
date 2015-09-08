import sys
import csv
import math
a=open(sys.argv[1],'rb')
l=csv.reader(a)
x=[]
for i in l:
    x.append(i)

########################################################################################################################
#                                               TRANSPOSE
########################################################################################################################
def transpose(x):
    n_row=len(x)
    n_col=len(x[0])
    t_x=[]
    t_xx=[]

    for i in range(0,n_col):
        for j in range(0,n_row):
            t_x.append(x[j][i])
        t_xx.append(t_x)
        t_x=[]
    return t_xx

########################################################################################################################
#                                               ARITY
########################################################################################################################

def arity(data):
    arity=[]
    for i in data:
        if i not in arity:
            arity.append(i)
    return arity

########################################################################################################################
#                                               ENTROPY
########################################################################################################################

def entropy(l):
    art=arity(l)
    ent=0
    l_len=len(l)
    for i in art:
        c=l.count(i)*1.0
        c/=l_len
        ent+=c*(-math.log(c,2))

    return ent

########################################################################################################################
#                                            CONDITIONAL ENTROPY
########################################################################################################################

def cond_entropy(y,x):
    z=zip(x,y)
    sub=[]
    cond_ent=0.0
    arty=arity(x)
    l_len=len(z)
    for i in arty:
        for j in z:
            if j[0]==i:
                sub.append(j[1])
        ent=entropy(sub)
        sub=[]
        c=x.count(i)*1.0
        c/=l_len
        cond_ent+=c*ent
    return cond_ent

########################################################################################################################
#                                               MUTUAL ENTROPY
########################################################################################################################

def mut_info(y,x):
    mut_inf=entropy(y)-cond_entropy(y,x)
    return mut_inf

t_x=transpose(x)
y=t_x[len(t_x)-1][1:]
sys.stdout.write('entropy: '+str(entropy(y))+'\n')
arty=arity(y)
arr=[]
for i in arty:
    arr.append(y.count(i)*1.0)
sys.stdout.write('error: '+ str(min(arr)/(arr[0]+arr[1])))
# t_x[len(t_x)-1][1:].count()