#!/usr/bin/python

prev={0:1,1:1}

def dictFact(n):

  if prev.has_key(n):
     return prev[n]
  else:
     newvalue=n*dictFact(n-1)
     prev[n]=newvalue
     return newvalue

print dictFact(10)
