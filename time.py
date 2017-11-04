#!/usr/bin/python 

class Time:
 pass
time=Time()

time.hour=11
time.minute=59
time.second=00


#print time.hour

def timeDisplay(time):

  return time.hour,time.minute,time.second



print timeDisplay(time)
