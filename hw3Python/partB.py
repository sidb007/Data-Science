__author__ = 'sbalodi'
import math
import sys
a = open('4Cat-Train.labeled', 'r')

# for 2-d array
def to_arr(a):
    data=a.readlines()
    no_lines=sum(1 for line in data)
    arr=['' for x in range(no_lines)]
    for line in range(no_lines):
        data[line]=data[line].rstrip()
        data[line]=data[line].replace('\t',' ')
        arr[line]=data[line].split(' ')
        #arr[line]=data[line].split('\t')
    # number of columns
    return arr

arr=to_arr(a)
col=len(arr[0])
no_lines=sum(1 for line in arr)


######################
#extract column

def ext_col(data,col):
    c=[]
    for i in data:
        c.append(i[col])
    return c
######################
######################
#arity

def arity(data):
    arity=[]
    for i in data:
        if i not in arity:
            arity.append(i)
    return arity
######################
######################
#printing array


def print_array(arr):
    for row in arr:
         for col in row:
              sys.stdout.write(col+' ')
    sys.stdout.write('\n')
#######################

#######################
#net array



#######################

####################################
# i.
####################################
no_col=sum(1 for col in arr[0])
level=[]
l=[]
for i in range(no_col/2-1):
    for j in range(no_lines):
        if arr[j][i*2+1] not in level:
            level.append(arr[j][i*2+1])
    l.append(len(level))
    level=[]
input_space=1
for i in l:
    input_space*=i
print(input_space)

####################################
# ii.
####################################
concept_s=1L
for i in range(input_space):
    concept_s*=2

sys.stdout.write(str(concept_s)+'\n')

####################################
# iii.
####################################
vs=[]
in_s=[]
t2=[]
t1=[]
for i in range(0,65536):
    x=bin(i)[2:]
    x=str(x)
    while(len(x)<16):
        x='0'+x
    vs.append(x)



for i in arr:
        for j in range(0,10):
            if j%2!=0:
                t1.append(i[j])
        t2.append(t1)
        t1=[]

arit=[]
for i in range(len(arr[0])/2-1):
    coll=ext_col(arr,i*2+1)
    arit.append(arity(coll))

cs=[]

for i in arit[0]:
    for j in arit[1]:
        for k in arit[2]:
            for l in arit[3]:
                  cs.append([i,j,k,l])


fs=[]
tt=0
indx=0
tmp=0
ind=[]

for i in t2:
    if i[-1]=='high':
        for j in cs:
            if i[:-1]==j:
                indx=cs.index(j)
                for k in vs:
                     if k[indx]=='0':
                        ind.append(k)
    if i[-1]=='low':
        for j in cs:
            if i[:-1]==j:
                indx=cs.index(j)
                for k in vs:
                      if k[indx]=='1':
                        ind.append(k)

my_set=set(ind)
for i in my_set:
    vs.remove(i)

print len(vs)

############################

c = open('4Cat-Dev.labeled', 'r')
arr2=to_arr(c)
cp=0
cn=0
pos=[]
neg=[]
flag=0
t5=[]

for i in arr2:
    for j in range(0,9):
        if j%2!=0:
            t1.append(i[j])
    t5.append(t1)
    t1=[]

for i in t5:
        for j in cs:
            if i==j:
                indx=cs.index(j)
                for k in vs:
                     if k[indx]=='1':
                         cp+=1
                     else:
                         cn+=1
        print str(cp)+' '+str(cn)
        cp=0
        cn=0
