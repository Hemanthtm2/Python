#!/usr/bin/python 

def printmult(n):
  i=1
  while i<=6:
   print n*i,'\t',
   i=i+1
  print

def printTable(high):
 i=1
 while i <= high:
   printmult(i) 
   i=i+1

print printTable(7)
