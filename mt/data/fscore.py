#!/usr/bin/env python

import sys

progoutputfile = sys.argv[1]
correctfile = sys.argv[2]
##
##
##fsock_progoutput = open(progoutputfile,'r')
##fsock_correct = open(correctfile,'r')



fsock_progoutput = open(progoutputfile,'r')
fsock_correct = open(correctfile,'r')

tokens = 0.0
correctwords = 0.0
shouldreturn = 0.0

##original = [x for x in fsock_original]
progoutput = [x for x in fsock_progoutput]
correct = [x for x in fsock_correct]



a = 0
for i in range(0,len(progoutput)):
##    line1 = original[i].split()
    line2 = progoutput[i].split()
    line3 = correct[i].split()

    if len(line2)>10:
        a= a+1
    else:
        tokens = tokens + len(line2)
        shouldreturn = shouldreturn + len(line3)
        for j in range(0,len(line2)):
            if line2[j] in line3:
                correctwords = correctwords + 1



correctness = 2*(correctwords/tokens*correctwords/shouldreturn/(correctwords/tokens+correctwords/shouldreturn))
print correctness
