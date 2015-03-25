#!/usr/bin/env python
# -*- coding: utf-8 -*-
#def count_words():
import os,sys,math

rules = sys.argv[1]
words = sys.argv[2]
out = sys.argv[3]

##fsock_words = open("data/wsj24.txt",'r')
##frules = open("data/wsj2-21.blt",'r')
##out = open("data/out.txt",'w')


fsock_words = open(words,'r')
frules = open(rules,'r')
out = open(out,'w')





def treeBank(frules):
    treeBank = {}
    unary = {}
    counts = {}
    for line in frules:
        line = line.split()
        if counts.has_key(line[1]):
            counts[line[1]]+=int(line[0])
        else:
            counts[line[1]]=int(line[0])
    frules = open("data/wsj2-21.blt",'r')

    for line in frules:
        line = line.split()
        lhs = line[1]
        rhs1 = line[3]
        rhs2 = None
        if len(line) >= 5:
            rhs2 = line[4]
        prob = float(line[0])/counts[line[1]]
        if rhs2 == None:
            if unary.has_key(rhs1):
                unary[rhs1].append([lhs,prob])
            else:
                unary[rhs1]=[[lhs,prob]]
        else:
            if treeBank.has_key(rhs1):
                if treeBank[rhs1].has_key(rhs2):
                    treeBank[rhs1][rhs2].append([lhs,prob])
                else:
                    treeBank[rhs1][rhs2]=[[lhs,prob]]
            else:
                treeBank.update({rhs1:{rhs2:[[lhs,prob]]}})
##            if treeBank.has_key((rhs1,rhs2)):
##                treeBank[(rhs1,rhs2)].append([lhs,prob])
##            else:
##                treeBank[(rhs1,rhs2)]=[[lhs,prob]]
    return treeBank,unary


def fill(chart,i,k,binary,unary,word):
    if k == i+1:
        chart[i][k][word] = (word,None,None,1)

        
##    for j in range(i+1,k):
##        for key1 in chart[i][j]:
##            for key2 in chart[j][k]:
##                label1 = key1
##                label2 = key2
##                c1 = chart[i][j][key1]
##                c2 = chart[j][k][key2]
##                if binary.has_key((label1,label2)):
##                    lists = binary[(label1,label2)]
##                    for b in range(len(lists)):
##                        list = lists[b]
##                        lhs = list[0]
##                        prob = list[1]
##                        u = c1[-1]*c2[-1]*prob
##                        c = (lhs,c1,c2,u)
####                    if len(chart[i][k]) != 0:
##                        if chart[i][k].has_key(lhs):
##                            if chart[i][k][lhs][-1] >= c[-1]:
##                                continue
##                            else:
##                                chart[i][k][lhs] = c
##                        else:
##                            chart[i][k][lhs] = c



    for j in range(i+1,k):
        for key1 in chart[i][j]:
            c1 = chart[i][j][key1]
            if binary.has_key(key1):
                D = binary[key1]
                for key in D:
                    if chart[j][k].has_key(key):
                        c2 = chart[j][k][key]
                        lists = binary[key1][key]
                        for b in range(len(lists)):
                            list = lists[b]
                            lhs = list[0]
                            prob = list[1]
                            u = c1[-1]*c2[-1]*prob
                            c = (lhs,c1,c2,u)
                            if chart[i][k].has_key(lhs):
                                if chart[i][k][lhs][-1] >= c[-1]:
                                    continue
                                else:
                                    chart[i][k][lhs] = c
                            else:
                                chart[i][k][lhs] = c
    
##            
##            for key2 in chart[j][k]:
##                label1 = key1
##                label2 = key2
##                c1 = chart[i][j][key1]
##                c2 = chart[j][k][key2]
##                if binary.has_key((label1,label2)):
##                    lists = binary[(label1,label2)]
##                    for b in range(len(lists)):
##                        list = lists[b]
##                        lhs = list[0]
##                        prob = list[1]
##                        u = c1[-1]*c2[-1]*prob
##                        c = (lhs,c1,c2,u)
####                    if len(chart[i][k]) != 0:
##                        if chart[i][k].has_key(lhs):
##                            if chart[i][k][lhs][-1] >= c[-1]:
##                                continue
##                            else:
##                                chart[i][k][lhs] = c
##                        else:
##                            chart[i][k][lhs] = c


    index = 1
    while index == 1:
        index = 0
        for labc in chart[i][k].keys():
        #    print labc
            if unary.has_key(labc):
                lists = unary[labc]
                c = chart[i][k][labc]
                for j in range(len(lists)):
                    list = lists[j]
                    lhs = list[0]
                    prob = list[1]
                    n = (lhs,c,None,prob*c[-1])
              #      print lhs,n
                    if chart[i][k].has_key(lhs):
                        if chart[i][k][lhs][-1] >= n[-1]:
                            continue
                        else:
                            index = 1
                     #       print n,lhs,1,labc
                            chart[i][k][lhs] = n
                    else:
                        index = 1
                     #   print n,lhs,2,labc
                        chart[i][k][lhs] = n



        

def Dfs(root,string):
    if root == None:
        return string
    if root[1] == None and root[2] == None:
        string = string + " "+root[0]
        return string
    string = string+ " " + "("+(root[0])
    string = Dfs(root[1],string)
    string = Dfs(root[2],string)
    string = string + ")"
 
    return string






(binary,unary) = treeBank(frules)


for line in fsock_words:
    line = line.split()
    if len(line) <=25:
        L = len(line)
        chart = [[{} for i in range(L+1)] for j in range(L+1)]
        for i in range(1,L+1):
            for s in range(0,L+1-i):
                word = line[s]
                fill(chart,s,s+i,binary,unary,word)
  #      print chart[0][L]["TOP"]
        string = ""
##        result = ""
        string = Dfs(chart[0][L]["TOP"],string)
##        for i in range(len(string)):
##            result = result +
        string = string[1:]+"\n"
        out.write(string)
    else:
        sting = "*IGNORE*"+"\n"
        out.write(string)
        


    



