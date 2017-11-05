#!/usr/bin/python 

class Time:

  pass

time=Time()
time.h=10
time.m=20
time.s=00

def printTime(time):
  print str(time.h) + ":" + \
        str(time.m) + ":" + \
        str(time.s)


currenttime=Time()

currenttime.h=9
currenttime.m=30
currenttime.s=14

print printTime(currenttime)





