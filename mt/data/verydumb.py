#!/usr/bin/env python

import sys

training_english = sys.argv[1]
training_french = sys.argv[2]
test_french = sys.argv[3]
##test = sys.argv[3]

n = {}
tau = {}


##fsock_traineng = open(training_english,'r')
##fsock_trainfre = open(training_french,'r')

##fsock_trainfre = open('english-senate-0.txt','r')
##fsock_traineng = open('french-senate-0.txt','r')
##fsock_test = open('french-senate-2.txt','r')
##translation = open('translation.txt','w+')



fsock_trainfre = open(training_french,'r')
fsock_traineng = open(training_english,'r')
fsock_test = open(test_french,'r')
translation = open('translation.txt','w+')



traineng = [x for x in fsock_traineng]
trainfre = [x for x in fsock_trainfre]


tau = {}
n = {}

for i in range(0,len(trainfre)):
    linefre = trainfre[i]
    lineeng = traineng[i]
#    if len(linefre.split())<10 and len(lineeng.split())<10:
    for strfre in linefre.split():
            pk = 0.0
            for streng in lineeng.split():
                pk = pk + 1.0                    
            for streng in lineeng.split():
                if n.has_key(streng):
                    if n[streng].has_key(strfre):
                        n[streng][strfre] = n[streng][strfre] + 1.0/pk
                          #  n[streng][strfre] = n[streng][strfre] + tau[streng][strfre]/pk
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

max = 0.0
maxdic = {}
for key in tau:
    for word in tau[key]:
        if tau[key][word]>max:
            max = tau[key][word]
            key1 = key
            key2 = word
    maxdic.update({key1:key2})
    max = 0.0


            
for line in fsock_test:
    string = ""
    for engstr in line.split():
        max = 0
        fre = ""
        if maxdic.has_key(engstr):
            fre = maxdic[engstr]
        else:
            fre = engstr
        string = string + fre + ' '
    print string
    translation.write(string)
    translation.write('\n')