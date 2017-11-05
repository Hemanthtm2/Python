#!/usr/bin/python 


class Time:

 pass

t=Time()
t.hour=10
t.minute=30
t.second=00

def convertSec():

  minute=t.hour*60+t.minute
  second=minute*60+t.second
  return second 

print convertSec()
  
