#!/usr/bin/python 

import random 
def listRandom(n):
  s=[0]*n
  for i in range(n):
    s[i]=random.random()
  return s

print listRandom(10)
