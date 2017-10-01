#!/usr/bin/python 

def inBucket(t,low,high):
  t=[10,20,30,40]
  count=0
  for num in t:
    if low<num<high:
      count=count+1
  return count 

print inBucket('t',20,40)


