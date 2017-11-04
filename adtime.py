#!/usr/bin/python 

class Time:
  pass

t1=Time()
t2=Time()

t1.h=10
t1.m=5
t1.s=0

t2.h=11
t2.m=4
t2.s=0

def addTime(t1,t2):

 sum=Time()
 sum.h=t1.h+t2.h
 sum.m=t1.m+t2.m
 sum.s=t1.s+t2.s
 return sum

print addTime(t1,t2)

ctime=Time()
ctime.h=9
ctime.m=14
ctime.s=50

btime=Time()
btime.h=3
btime.m=50
btime.s=0

doneTime(ctime,btime)

print 
