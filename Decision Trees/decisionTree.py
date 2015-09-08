import sys
import csv
import math
import copy

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




########################################################################################################################
#                                               Node Class
########################################################################################################################



class my_node:
    def __init__(self):
        self.data=[]
        self.attr=-99
        self.parent=None
        self.l_node=None
        self.r_node=None
        self.depth=0
        self.id=''
        self.gain=[]
        self.ari=''

##############################################################
#####               Classification Function               ####
##############################################################

def classify(y):
    arty=arity(y)
    if len(arty)!=1:
        c1=y.count(arty[0])
        c2=y.count(arty[1])
        if c1>c2:
            return arty[0]
        else:
            return arty[1]
    else:
        return arty[0]



########################################################################################################################
#                                                   ID3
########################################################################################################################



def ID3(node):
#    print node.id
    gain=[]
    df=node.data
    y_l=len(df)
    y=df[y_l-1][1:]
    for i in df[:-1]:
        gain.append(mut_info(y,i[1:]))
    node.gain=gain
#     print mut_info(y,df[1][1:])
#     print y
#     print df[1][1:]

    ind_max=node.gain.index(max(node.gain))
#     print max(node.gain)
#     print 'index split'
#     print ind_max
#     print 'arity at split'
#     print node.ari
    ar=arity(df[ind_max][1:])
    if max(node.gain)<.1 or node.depth==2 or len(ar)==1:
        node.type=classify(y)
        node.attr=-1
#         print str(node.id)+' ends here with gain ='+str(max(node.gain))
#         print 'type of node'
#         print node.type

        return 1
    else:
        ar=arity(df[ind_max][1:])
        ar=sorted(ar,reverse=True)
        node.attr=ind_max
#         print node.attr
        df1=transpose(df)
        l_n=[]
        r_n=[]
        l_n.append(df1[0])
        r_n.append(df1[0])
        for j in df1[1:]:
            if ar[0]==j[ind_max]:
                 l_n.append(j)
            else:
                 r_n.append(j)
        l_nod=my_node()
        r_nod=my_node()
        l_nod.data=transpose(l_n)
        r_nod.data=transpose(r_n)
        l_nod.depth=node.depth+1
        r_nod.depth=node.depth+1
        l_nod.id=node.id+'_l'+str(l_nod.depth)
        r_nod.id=node.id+'_r'+str(r_nod.depth)
        ar=sorted(ar,reverse=True)
        l_nod.ari=ar[0]
#         print '@@@@@'
#         print l_nod.ari
        r_nod.ari=ar[1]
        l_nod.parent=node
        r_nod.parent=node
        node.l_node=l_nod
        node.r_node=r_nod
#         print '******'
#         print len(node.data)
        ID3(node.l_node)
        ID3(node.r_node)

######################################################################################################################
#                                              TRAVERSE                                                              #
######################################################################################################################

error=[]
type=[]
id=[]
def traverse(node):
    df=node.data
    df_t=transpose(df)
    y_l=len(df)-1
    y=df[y_l]
    ar=arity(y[1:])
    ar=sorted(ar,reverse=True)
    ###############
    if node.attr==-1:
        if node.depth>1:
            for i in range(0,node.depth):
                sys.stdout.write(' ')
            sys.stdout.write('|')
        #  attr for split
        sys.stdout.write(str(node.parent.data[node.parent.attr][0])+' = ')
        #  value for split
        sys.stdout.write(str(df_t[node.parent.attr][1])+': ')
    #####################
        #  +/-
        if len(ar)==1:
            cc=y.count(ar[0])
#             sys.stdout.write(str(cc))
            prev_ar=sorted(arity(node.parent.data[(len(node.parent.data)-1)][1:]),reverse=True)
            if ar[0]==prev_ar[0]:
                sys.stdout.write('['+str(cc)+'+/'+'0'+'-]\n')
            else:
                sys.stdout.write('['+'0'+'+/'+str(cc)+'-]\n')



#             if ar[0]==prev_ar[0]:
#                     sys.stdout.write('#['+str(cc)+'+/'+'0'+'-]')

#             else:
#                     sys.stdout.write('['+'0'+'+/'+str(cc)+'-]')

        else:
            c1=ar[0]
            c2=ar[1]
            sys.stdout.write('['+str(y.count(c1))+'+/'+str(y.count(c2))+'-]\n')

#         error.append(y.count(node.type))

#         type.append(node.type)
#         id.append(y.count(node.type))
        bias=(y[1:].count(node.type))
        err=len(y[1:])-bias
        error.append(err)

    #######################
    else:

            if  node.id=='r':

                c1=ar[0]
                c2=ar[1]
                sys.stdout.write('['+str(y.count(c1))+'+/'+str(y.count(c2))+'-]\n')
            #       node.data[0][node.attr]
            else:

                if node.depth>1:
                    sys.stdout.write('|')
                    for i in range(0,node.depth):
                        sys.stdout.write(' ')


                 #  attr for split
                sys.stdout.write(str(node.parent.data[node.parent.attr][0])+' = ')
                #  value for split
                sys.stdout.write(str(df_t[1][node.parent.attr])+': ')
#                 sys.stdout.write(str(df_t[node.parent.attr][1])+': ')
#                 #str(df_t[node.parent.attr][1])+': **'
                #  +/-
                #  +/-
                if len(ar)==1:
                    cc=y.count(ar[0])
        #             sys.stdout.write(str(cc))
                    if ar[0]==node.type:
                        sys.stdout.write('['+str(cc)+'+/'+'0'+'-]\n')
                    else:
                        sys.stdout.write('['+'0'+'+/'+str(cc)+'-]\n')
                else:

                    c1=ar[0]
                    c2=ar[1]
                    sys.stdout.write('['+str(y.count(c1))+'+/'+str(y.count(c2))+'-]\n')
            l_n=[]
            r_n=[]
            l_n.append(df_t[0])
            r_n.append(df_t[0])
            split_by=arity(df[node.attr][1:])
            split_by=sorted(split_by, reverse=True)
        #             print split_by
            for j in df_t[1:]:
                if split_by[0]==j[node.attr]:
                     l_n.append(j)
                else:
                     r_n.append(j)
            node.l_node.data=transpose(l_n)
            node.r_node.data=transpose(r_n)
            traverse(node.l_node)
            traverse(node.r_node)


######################################################################################################################
#                                              TRAVERSE for testing                                                  #
######################################################################################################################

error=[]
type=[]
id=[]
def traverse_t(node):
    df=node.data
    df_t=transpose(df)
    y_l=len(df)-1
    y=df[y_l]
    ar=arity(y[1:])
    ar=sorted(ar,reverse=True)
    ###############
    if node.attr==-1:
        bias=(y[1:].count(node.type))
        err=len(y[1:])-bias
        error.append(err)

    #######################
    else:
        l_n=[]
        r_n=[]
        l_n.append(df_t[0])
        r_n.append(df_t[0])
        split_by=arity(df[node.attr][1:])
        split_by=sorted(split_by, reverse=True)
    #             print split_by
        for j in df_t[1:]:
            if split_by[0]==j[node.attr]:
                 l_n.append(j)
            else:
                 r_n.append(j)
        node.l_node.data=transpose(l_n)
        node.r_node.data=transpose(r_n)
        traverse_t(node.l_node)
        traverse_t(node.r_node)



#################################################################################################################################
#                                                         SETUP                                                                 #
#################################################################################################################################



a=open(sys.argv[1],'rb')


l=csv.reader(a)
x=[]


b=open(sys.argv[2],'rb')
ll=csv.reader(b)
test=[]

for i in l:
    x.append(i)

for i in ll:
    test.append(i)

t_x=transpose(x)
test_t=transpose(test)


# temp=[]
# new_y=t_x[len(t_x)-1]
# temp.append(new_y[0])
# for i in new_y[1:]:
#     temp.append(i[:1])
# asd=(t_x[1:len(t_x)-1])
# asd.append(temp)



#################################################################################################################################
#                                                       TRAINING                                                                #
#################################################################################################################################

no=my_node()
no.data=t_x
no.id='r'
ID3(no)
traverse(no)
err=sum(error)/float((len(no.data[0])-1))
sys.stdout.write('error(train): '+str(err))

#################################################################################################################################
#                                                       TESTING                                                                 #
#################################################################################################################################
error=[]
n1=copy.deepcopy(no)
n1.data=test_t
traverse_t(n1)
err=sum(error)/float((len(n1.data[0])-1))
sys.stdout.write('\nerror(test): '+str(err))

