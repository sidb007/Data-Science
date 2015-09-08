__author__ = 'sbalodi'
import sys
import math

a = open('9Cat-Train.labeled', 'r')
o=open('partA4.txt', 'w')


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
        c.append(i[col-1])
    return c
######################
######################
#arity

def arity(data):
    arity=[]
    data=ext_col(arr,len(arr[0]))
    for i in data:
        if i not in arity:
            arity.append(i)
    return arity
######################
#printing array


def print_array(arr):
    for row in arr:
         for col in row:
              sys.stdout.write(col+' ')
    sys.stdout.write('\n')
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
decimel=0
while concept_s>0:
    concept_s/=10
    decimel+=1

print(decimel)
####################################
# iii.
####################################
hypo=1
for i in l:
    hypo*=(i+1)
print(hypo+1)
####################################
# iv.
####################################
##
cc=0 # for rules
tmp=[]
rule=[]
high=0 # for rules

tt=[]
for i in range(len(arr)):
    lev=arity(arr)[0]
    if arr[i][col-1]==lev:
        if high==0:
            rule=arr[i]
            high=1
        else:
            for j in range(col):
                if rule[j]!=arr[i][j]:
                    rule[j]='?'
            if (i+1)%30==0 and i!=0:
                for k in range(len(rule)/2-1):
                    o.write(rule[2*k+1])
                    if (k+1)!=len(rule)/2-1:
                        o.write('\t')
                    else:
                        o.write('\n')

    else:
        if (i+1)%30==0 and i!=0:
                for k in range(len(rule)/2-1):
                    o.write(rule[2*k+1])
                    if (k+1)!=len(rule)/2-1:
                        o.write('\t')
                    else:
                        o.write('\n')



x=0

# for j in tt:
#     for i in range(len(j)/2-1):
#         print(rule[i*2+1])
#         o.write(rule[i*2+1])
#         if i<len(j)/2-2:
#             o.write('\t')


for i in tt:
    for j in range(len(i)):
        sys.stdout.write(i[j])

rule=rule[:-2]

#testing data
b = open('9Cat-Dev.labeled', 'r')
test=to_arr(b)
prob=0.0
pred=[]
def accuracy(d,rule):
    flag=0
    for i in d:
        for j in range(len(i)-2):
            if i[j]==rule[j] or rule[j]=='?':
                continue
            else:
                flag=1
                break
        if flag==0:
            pred.append(arity(d)[0])
        else:
            pred.append(arity(d)[1])
        flag=0
    return pred

pred=accuracy(test,rule)

for i in range(len(test)):
      if pred[i]!=test[i][len(test[1])-1]:
          prob+=1
mis_class=prob/len(test)

print str(mis_class)+arity(arr)[0]

########################################
#  vi.
########################################
#
tr = open(sys.argv[1], 'r')
new_test=to_arr(tr)
new_pred=accuracy(new_test,rule)
flag=0
Ari=arity(ext_col(new_test,20))

for i in new_test:
    for j in range(len(i)-2):
        if i[j]==rule[j] or rule[j]=='?':
            continue
        else:
            flag=1
            break

    if flag==0:
        sys.stdout.write(Ari[0]+'\n')
    else:
        sys.stdout.write(Ari[1]+'\n')
    flag=0