#!/usr/bin/env python
# -*- coding: utf-8 -*-
#def count_words():
import os,sys,math


training = sys.argv[1]
fsock_train = open(training)
testing = sys.argv[2]
fsock_test = open(testing)
result1 = sys.argv[3]
fsock_result = open(result1,"w")

##training = sys.argv[1]
##fsock_train = open(training,'r')

#fsock_train=open("data/wsj2-21.txt",'r')
#fsock_test=open("data/wsj22.txt")
#fsock_result = open("data/result.txt",'w')


deita = {}
tau = {}
label = []

for line in fsock_train:
    line = ("⊲ ⊲ "+line+" ⊲ ⊲ ").split()
#    line = line.split()
    for i in range(0,len(line)-2):
        if i%2 == 1:
            if tau:
                if tau.has_key(line[i]):
                    if tau[line[i]].has_key(line[i-1]):
                        tau[line[i]][line[i-1]] = tau[line[i]][line[i-1]]+1
                    else:
                        tau[line[i]].update({line[i-1]:1.0})
                else:
                    tau.update({line[i]:{line[i-1]:1.0}})
            else:
                tau.update({line[i]:{line[i-1]:1.0}})
            if deita:
                if deita.has_key(line[i]):
                    if deita[line[i]].has_key(line[i+2]):
                        deita[line[i]][line[i+2]] = deita[line[i]][line[i+2]]+1
                    else:
                        deita[line[i]].update({line[i+2]:1.0})
                else:
                    deita.update({line[i]:{line[i+2]:1.0}})
            else:
                deita.update({line[i]:{line[i+2]:1.0}})
            if line[i] not in label:
                label.append(line[i])
tauyx = {}
deitay = {}
ny = 0.0
nytau = 0.0
w = 0.0
for y in deita:
    ny = 0.0
    for yprime in deita[y]:
        ny +=deita[y][yprime]
    for yprime in deita[y]:
        if deitay.has_key(y):
            deitay[y].update({yprime:(deita[y][yprime])/(ny)})
        else:
            deitay.update({y:{yprime:((deita[y][yprime])/(ny))}})

for y in tau:
    w = 0.0
    nytau = 0.0 
    for x in tau[y]:
        nytau +=tau[y][x]
        w +=1
#    tauyx.update({(y,"*UNK*"):(1.0)/(nytau+w)})
    for x in tau[y]:
        if tau[y][x] == 1:
            if tauyx.has_key((y,"*UNK*")):
                tauyx[(y,"*UNK*")]=tauyx[(y,"*UNK*")]+(1.0)/(nytau+w)
            else:
                tauyx.update({(y,"*UNK*"):(1.0)/(nytau+w)})
        tauyx.update({(y,x):((tau[y][x]+1.0)/(nytau+w))})




for line in fsock_test:
    line = line.split()
    DPu = [[0.0 for x in range((len(line)/2))] for y in range(len(tau))]
    tag = [[0.0 for x in range((len(line)/2))] for y in range(len(tau))]
    i = 0
    for i in range(0,len(label)):
        if deitay["⊲"].has_key(label[i]):
            if tauyx.has_key((label[i],line[0])):
                DPu[i][0] = deitay["⊲"][label[i]]*tauyx[(label[i],line[0])]
                tag[i][0] = i

        i +=1
    
    for j in range(2,len(line)):
        if j%2 == 0:
            for k in range(0,len(label)):

                maxtau = 0.0
                position = 0

                for h in range(0,len(label)):
                    temp = 0.0
                    if DPu[h][j/2-1] == 0:
                        continue
                    if deitay[label[h]].has_key(label[k]):
                        if tauyx.has_key((label[k],line[j])):
                            temp = DPu[h][j/2-1]*deitay[label[h]][label[k]]*tauyx[(label[k],line[j])]
                            if temp > maxtau:
                                maxtau = temp
                                position = h    
                DPu[k][j/2] = maxtau
                tag[k][j/2] = position


##    for i in range(0,len(label)):
##        print DPu[i][len(line)/2-2]
##    for i in range(0,len(label)):
##        print DPu[i][len(line)/2-1]           
    position = 0
    for i in range(0,len(label)):
        maxtau = 0.0
        if DPu[i][-1]==0:
            continue
    #    print label[i]
        
        if deitay[label[i]].has_key("⊲"):
            temp = DPu[i][-1]*deitay[label[i]]["⊲"]
        if temp > maxtau:
            maxtau = temp
            position = i
    result = [0]*(len(line)/2)
    for i in range(len(line)/2-1,-1,-1):
        result[i] = label[position]
        position = tag[position][i]
    string = ""
    for i in range(0,len(result)):
        string = string + line[i]+" "+result[i]+" "
    fsock_result.write(string+"\r\n")
    

       
            
        
