#!/usr/bin/env python
# -*- coding: utf-8 -*-
#def count_words():
import os,sys
filename=sys.argv[1]
outfile=sys.argv[2]
#print filename
#print outfile
Words={}   
n=0.0
#dictionary
for line in open(filename):
    for str in line.split():
			if Words:
				if Words.has_key(str):
					Words[str]=Words[str]+1
					n=n+1
				else:
					Words.update({str:1})
					n=n+1
			else:
				Words.update({str:1})
				n=n+1
print n				
for key in Words:
	Words[key]=Words[key]/n
print Words
#stdout=sys.stdout
#sys.stdout=open(outfile,'w+')
#for key in Words.iterkeys():
#    print('%d\t%s'%(Words[key],key))
#sys.stdout=stdout