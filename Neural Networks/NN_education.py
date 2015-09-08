import sys
import csv
import random
import math
import numpy as np
import time

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

def arity(data):
    arity=[]
    for i in data:
        if i not in arity:
            arity.append(i)
    return arity
    
def sigmoid(x):
    b=1/math.exp(x)
    c=1/(1+b)
    return c
    


a=open(sys.argv[1],'rb')
l=csv.reader(a)
x=[]

b=open(sys.argv[2],'rb')
l2=csv.reader(b)
x2=[]


for i in l:
    x.append(i)
    
for i in l2:
    x2.append(i)
nor=[]

nor=[]
def list2ListOfMatrix2(non_transposed_list):
    tx=transpose(non_transposed_list)
    txn=[]
    for i in tx:
        temp=np.asmatrix(i[1:],dtype=float)
        temp1=(temp)/100.0
        #nor.append(np.linalg.norm(temp))
        #temp=temp/np.linalg.norm(temp)
        txn.append(temp1)
        temp=[]
    return txn

lmx2=list2ListOfMatrix2(x2)

lmx3=list2ListOfMatrix2(x)

class perceptron:
    def __init__(self):
        self.data=0.0
        self.lyr=None
        self.ff=[]
        self.fb=[]
        self.wtf=[]
        self.wtb=[]
        self.delta=0.0


def new_layer(num,l_name):
    layer=[]
    for i in range(num):
        ob=perceptron()
        ob.lyr=l_name
        layer.append(ob)
    return layer

def connect_lyr(lyr1,lyr2):
    for i in range(len(lyr1)):
        for j in range(len(lyr2)):
            lyr1[i].ff.append(lyr2[j])
            lyr1[i].wtf.append(random.uniform(-.01,.01))
#
#    for i in range(len(lyr2)):
#        for j in range(len(lyr1)):
#            lyr2[i].fb.append(lyr1[j])
#            lyr2[i].wtb.append(lyr1[j].wtf[i])

            
def config(inp,hid,out):
    #input layer
    lyr=[]
    lyr.append(new_layer(inp,'i'))    
    lyr.append(new_layer(hid,'h'))
    lyr.append(new_layer(out,'o'))
    connect_lyr(lyr[0],lyr[1])
    connect_lyr(lyr[1],lyr[2])   
#    for i in range(inp):
#        lyr[0][i].data=mat[i]
    return lyr

def for_pass(nn,data,i):
    for j in range(len(nn[0])):
        nn[0][j].data=data[j][0,i]
    for i in [1,2]:
        for j in range(len(nn[i])):
            sum=0.0        
            for k in nn[i-1]:
                sum+=k.wtf[j]*k.data
            nn[i][j].data=sigmoid(sum)
    return nn[2][0].data   
    

def train(nn,data,l_rate,data2):
    start_time = time.time()
    err_p=10000.0
    error=1000.0    
    err_p2=10000.0
    error2=1000.0    
    while((time.time()-start_time<50)and(err_p>error)):        
        l_rate-=0.0008
            #l_rate-=0.001
        for i in range(data[0].size):
            pred=for_pass(nn,data,i)
            nn[2][0].delta=nn[2][0].data*(1-nn[2][0].data)*(data[len(data)-1][0,i]-nn[2][0].data)     
    
            for j in [1]:
                for k in range(len(nn[j])):
                    summ=0.0                
                    for l in range(len(nn[j][0].ff)):
                        summ+=nn[j][k].wtf[l]*nn[j][k].ff[l].delta
                    nn[j][k].delta=nn[j][k].data*(1-nn[j][k].data)*summ
            
            for j in [0,1]:
                for k in range(len(nn[j])):
                    for l in range(len(nn[j][k].ff)):
                        del_wt=l_rate*nn[j][k].data*nn[j][k].ff[l].delta
                        nn[j][k].wtf[l]=nn[j][k].wtf[l]+del_wt
        err_p=error
        err=0.0
        for i in range(data[0].size):
            err=err+(data[len(data)-1][0,i]-for_pass(nn,data,i))**2
        if (random.uniform(0,1))>0.5:
            print err
        error=err
        
    print 'TRAINING COMPLETED! NOW PREDICTING.'
    
    pred=[]        
    for i in range(data2[0].size):
        pred.append(for_pass(nn,data2,i))
    pred1=(np.asmatrix(pred)*100.0).tolist()
    for i in range(len(pred1[0])):
        print pred1[0][i]
        
        
nn=config(5,6,1)
#train(nn,lmx3,0.001,lmx2)
train(nn,lmx3,1,lmx2)