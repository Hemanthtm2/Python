#!/usr/bin/python 
class Time:
  pass

t1=Time()
t1.hr=10
t1.mi=20
t1.se=00
t2=Time()
t2.hr=15
t2.mi=30
t2.se=00

def addTime(t1,t2):
  sum=Time()
  sum.hr=t1.hr+t2.hr
  sum.mi=t1.mi+t2.mi
  sum.se=t1.se+t2.se
  return sum 

print addTime(t1,t2)
