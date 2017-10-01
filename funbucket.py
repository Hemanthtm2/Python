#!/usr/bin/python 

def inBucket(t,low,high):
  t=[10,20,30,40,50,60,70,80,100]
  count=0
  for num in t:
    if low<num<high:
      count=count+1
  return count 

#a=[10,20,30,40,50,60,70,80,100]
print inBucket('t',20,100)


