#!/usr/bin/python

def head(list):
  return list[:]


numbers=[1,2,3]
print head(numbers)

def headdel(list):
  del list[0]
  print list

num=['a','b','c']
headdel(num)

def tailin(list):
  list[-1]="H"
  print list 
name=["aa","bb","cc","dd"]
tailin(name)
