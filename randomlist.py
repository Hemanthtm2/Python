#!/usr/bin/python 
import random 
def randList(n):
 s=[0]*n

 for i in range(n):
   s[i]=random.random()
 return s

print randList(8)
