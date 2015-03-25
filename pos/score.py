#!/usr/bin/env python
# -*- coding: utf-8 -*-
#def count_words():
import os,sys,math
import copy
testing = sys.argv[1]
fsock_test = open(testing,'r')
result1 = sys.argv[2]
fsock_result = open(result1,'r')


#fsock_test = open(testing)
#fsock_result = open(result)

##fsock_test=open("data/wsj22.txt")
##fsock_result = open("data/result.txt")

test = []
predict = []

for line in fsock_test:
    line = line.split()
    tags = []
    for i in range(0,len(line)):
        if i%2 == 1:
            tags.append(line[i]) 
    test.append(copy.copy(tags))


for line in fsock_result:
    line = line.split()
    labels = []
    for i in range(0,len(line)):
        if i%2 == 1:
            labels.append(line[i])
    predict.append(copy.copy(labels))


#print len(test)
#print len(predict)
      
def percentage(test,predict):
    total = 0.0
    correct = 0.0
    for i in range(0,len(test)):
        for j in range(0,len(test[i])):
#            print len(test[i])
#            print len(predict[i])
            if test[i][j] == predict[i][j]:
                correct +=1
            total +=1
    return (correct/total)

print percentage(test,predict)
