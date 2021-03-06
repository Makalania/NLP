#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,math

training_english = sys.argv[2]
training_french = sys.argv[1]
test_translate = sys.argv[3]

phi = (1.0+math.sqrt(5.0))/2
resphi = 2.0-phi


##
##train_file = sys.argv[1]
##heldout_file = sys.argv[2]
##test_file = sys.argv[3]
##goodbad_file = sys.argv[4]
##
##fsock_train=open(train_file,'r')
##fsock_heldout=open(heldout_file,'r')
##fsock_test=open(test_file,'r')
##fsock_goodbad=open(goodbad_file,'r')


fsock_train=open('english-senate-0.txt','r')
fsock_heldout=open('english-senate-1.txt','r')


n = {}
tau = {}


##fsock_traineng = open(training_english,'r')
##fsock_trainfre = open(training_french,'r')

##fsock_trainfre = open('french-senate-0.txt','r')
##fsock_traineng = open('english-senate-0.txt','r')
##fsock_test = open('french-senate-2.txt','r')

fsock_trainfre = open(training_french,'r')
fsock_traineng = open(training_english,'r')
fsock_test = open(test_translate,'r')

translationbi = open('translation.txt','w+')
traineng = [x for x in fsock_traineng]
trainfre = [x for x in fsock_trainfre]


tau = {}
n = {}

for i in range(0,len(trainfre)):
    linefre = trainfre[i]
    lineeng = traineng[i]
    for strfre in linefre.split():
            pk = 0.0
            for streng in lineeng.split():
                pk = pk + 1.0                    
            for streng in lineeng.split():
                if n.has_key(streng):
                    if n[streng].has_key(strfre):
                        n[streng][strfre] = n[streng][strfre] + 1.0/pk
                    else:
                        nef = 1.0/pk
                        n[streng].update({strfre:nef})
                else:
                    nef = 1.0/pk
                    n.update({streng:{strfre:nef}})
for eng in n:
    neo = 0.0
    for fre in n[eng]:
        neo = neo + n[eng][fre]
    for fre in n[eng]:
#        if neo != 0:
            if tau.has_key(eng):
                if tau[eng].has_key(fre):
                    tau[eng][fre] = n[eng][fre]/neo
                else:
                    val = n[eng][fre]/neo
                    tau[eng].update({fre:val})
            else:
                val = n[eng][fre]/neo
                tau.update({eng:{fre:val}})

n.clear()



for j in range(0,9):
    for i in range(0,len(trainfre)):
        linefre = trainfre[i]
        lineeng = traineng[i]
        for strfre in linefre.split():
            pk = 0.0
            for streng in lineeng.split():        
                    pk = pk + tau[streng][strfre]
            for streng in lineeng.split():
                if n.has_key(streng):
                    if n[streng].has_key(strfre):
                        n[streng][strfre] = n[streng][strfre] + tau[streng][strfre]/pk
                    else:
                        nef = tau[streng][strfre]/pk
                        n[streng].update({strfre:nef})
                else:
                    nef = tau[streng][strfre]/pk
                    n.update({streng:{strfre:nef}})
                

    for eng in n:
        neo = 0.0
        for fre in n[eng]:
            neo = neo + n[eng][fre]
        for fre in n[eng]:
            tau[eng][fre] = n[eng][fre]/neo




for key in tau:
    for (k,v) in tau[key].items():
        if v<0.2:
            del tau[key][k]



type_train = 0
type_heldout = 0
type_test = 0
token_train = 0.0
token_heldout = 0
token_test = 0
bi_type_train = 0
bi_token_train= 0


train = {}  #dictionary for training data
heldout = {}    #dictionary for develop data
##test = {}   #dictionary for test data
bitrain= {} #dictionary for bigram training data
biheldout= {}   #dictionary for bigram biheldout data
##bitest= {}  #dictionary for bigram test data

# read the data into dictionary
for line in fsock_train:
    for str in ('⊳'+' '+line+'⊳'+' ').split():
                    if train:
                                    if train.has_key(str):
                                                train[str]=train[str]+1
                                                token_train = token_train+1
                                    else:
                                                train.update({str:1})
                                                token_train = token_train+1
                                                type_train = type_train+1
                    else:
                            train.update({str:1})
                            token_train = token_train+1
                            type_train = type_train+1
fsock_train=open('english-senate-0.txt','r')

#fsock_train=open(train_file,'r')
for line in fsock_train:
    temp = '⊳'
    for str in ('⊳'+' '+line+'⊳'+' ').split():
        if str == '⊳' and temp == '⊳':
            temp == '⊳'
        else:
            if bitrain:
                                    if bitrain.has_key(temp+' '+str):
                                                    bitrain[temp+' '+str]=bitrain[temp+' '+str]+1
                                                    bi_token_train = bi_token_train+1
                                    else:
                                                    bitrain.update({temp+' '+str:1})
                                                    bi_token_train = bi_token_train+1
                                                    bi_type_train = bi_type_train+1
            else:
                                bitrain.update({temp+' '+str:1})
                                bi_token_train = bi_token_train+1
                                bi_type_train = bi_type_train+1
        temp = str



for line in fsock_heldout:
    for str in ('⊳'+' '+line+'⊳'+' ').split():
                        if heldout:
                                        if heldout.has_key(str):
                                                    heldout[str]=heldout[str]+1
                                        else:
                                                    heldout.update({str:1})
                        else:
                                heldout.update({str:1})


fsock_heldout=open('english-senate-1.txt','r')


#fsock_heldout=open(heldout_file,'r')
for line in fsock_heldout:
    temp = '⊳'
    for str in ('⊳'+' '+line+'⊳'+' ').split():
        if str == '⊳' and temp == '⊳':
            temp == '⊳'
        else:
            if bitrain:
                                    if biheldout.has_key(temp+' '+str):
                                                    biheldout[temp+' '+str]=biheldout[temp+' '+str]+1
                                                #    print temp+' '+str
                                    else:
                                                    biheldout.update({temp+' '+str:1})
                                                 #   print temp+' '+str
            else:
                                biheldout.update({temp+' '+str:1})
                          #      print temp+' '+str
        temp = str



# This function serve for golden section search algorithm as f(x)
def find_alpha_beta(heldout,train,type_train,token_train,alpha):
    Lh = 0.0    
    for key in heldout:
        if train.has_key(key):
            Lh = Lh + (math.log((train[key]+alpha)/(token_train+alpha*(type_train+1.0))))*heldout[key]
        else:
            Lh = Lh + (math.log(alpha/(token_train+alpha*(type_train+1.0))))*heldout[key]
    return Lh



#golden section search algorithm for value alpha

def golden_section_search_alpha (a,b,c,tau):
    x = 0.0
    if c - b > b - a:
        x = b+resphi * (c-b)
    else:
        x = b-resphi * (b-a)
    if abs(c - a) < tau * (abs(b) + abs(x)):
        return (c + a) / 2.0
    assert find_alpha_beta(heldout,train,type_train,token_train,x) != find_alpha_beta(heldout,train,type_train,token_train,b)
    if abs(find_alpha_beta(heldout,train,type_train,token_train,x)) < abs(find_alpha_beta(heldout,train,type_train,token_train,b)):
 #       print find_alpha_beta(heldout,train,type_train,token_train,x)
        if c-b > b-a:
            return golden_section_search_alpha(b,x,c,tau)
        else:
            return golden_section_search_alpha(a,x,b,tau)
    else:
        if c-b>b-a:
            return golden_section_search_alpha(a,b,x,tau)
        else:
            return golden_section_search_alpha(x,b,c,tau)



alpha = golden_section_search_alpha (0.0,5,16000,0.1)


#calculate the maximum likelyhood
def likelyhood(beta,bitrain,train,alpha,token_train,type_train,bifile_test,file_test):
    L = 0.0
    theta = 0.0
    for key in bifile_test:
        str = key.split()
        str0 = str[0]
        str1 = str[1]
        theta = 0.0
        ## calculate theta w'
        if train.has_key(str1):
            theta = (train[str1]+alpha)/(token_train+alpha*(type_train+1.0))
        else:
            theta = (alpha/(token_train+alpha*(type_train+1.0)))
    #    print (train['the']+alpha)/(token_train+alpha*(type_train+1.0))
        if bitrain.has_key(key):                # if key value exist
                L = L + (math.log((bitrain[key]+beta*theta)/(train[str0]+beta)))*bifile_test[key]
        elif train.has_key(str0):               # if only w exist
                L = L + (math.log((beta*theta)/(train[str0]+beta)))*bifile_test[key]
        else:                                   # if w and w' doesnt exist in train data
                L = L + (math.log(theta))*bifile_test[key]            
    return L

#search for beta
def golden_section_search_beta (a,b,c,tau):
    x = 0.0
    if c - b > b - a:
        x = b+resphi * (c-b)
    else:
        x = b-resphi * (b-a)
    if abs(c - a) < tau * (abs(b) + abs(x)):
        return (c + a) / 2.0
    assert likelyhood(x,bitrain,train,alpha,token_train,type_train,biheldout,heldout) != likelyhood(b,bitrain,train,alpha,token_train,type_train,biheldout,heldout)
    if abs(likelyhood(x,bitrain,train,alpha,token_train,type_train,biheldout,heldout)) < abs(likelyhood(b,bitrain,train,alpha,token_train,type_train,biheldout,heldout)):
        if c-b > b-a:
            return golden_section_search_beta(b,x,c,tau)
        else:
            return golden_section_search_beta(a,x,b,tau)
    else:
        if c-b>b-a:
            return golden_section_search_beta(a,b,x,tau)
        else:
            return golden_section_search_beta(x,b,c,tau)

beta = golden_section_search_beta (0.0,5.0,16000,0.1)


reverse = {}

for key1 in tau:
    for key2 in tau[key1]:
        if reverse.has_key(key2):
            reverse[key2].update({key1:tau[key1][key2]})
        else:
            reverse.update({key2:{key1:tau[key1][key2]}})


def thetaw(ej1,ej):
    thetaw = 0.0
    theta = 0.0     #calculate the beta
    if train.has_key(ej):
        theta = (train[ej]+alpha)/(token_train+alpha*(type_train+1.0))
    else:
        theta = (alpha/(token_train+alpha*(type_train+1.0)))                
       
    if bitrain.has_key(ej1+' '+ej):
        thetaw =  (bitrain[ej1+' '+ej]+beta*theta)/(train[ej1]+beta)
    elif train.has_key(ej1):
        thetaw = beta*theta/(train[ej1]+beta)
    else:
        thetaw = theta
    return thetaw


for line in fsock_test:
    string = ""
    ej1 = "⊳"
    for freword in line.split():
        max=0.0
        english_max = ""
        if reverse.has_key(freword):
            for engword in reverse[freword]:
                val = thetaw(ej1,engword) * reverse[freword][engword]
                if val>max:
                    max = val
                    engword_max = engword
        else:
            engword_max = freword
        ej1 = engword_max
        string = string + engword_max + ' ' 
    print string
    translationbi.write(string)
    translationbi.write('\n')


        

