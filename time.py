#!/usr/bin/python 

class Time:
 pass
time=Time()

time.hour=11
time.minute=59
time.second=00

t1=Time()
t1.hour=20
t1.minute=45
t1.second=60

t2=Time()
t2.hour=12
t2.minute=40
t2.second=55

currenttime=Time()
currenttime.hour=30
currenttime.minute=60
currenttime.second=70


breadtime=Time()
breadtime.hour=90
breadtime.minute=80
breadtime.second=60

def printTime(time):
  print str(time.hour) + ":" + \
        str(time.minute) + ":" + \
        str(time.second)
  


def addTime(t1,t2):
  sum=Time()
  sum.hour=t1.hour+t2.hour
  sum.minute=t1.minute+t2.minute
  sum.second=t1.second+t2.second

  if sum.second >= 60:
    sum.second = sum.second - 60
    sum.minute = sum.minute + 1
  if sum.minute >= 60:
    sum.minute = sum.minute - 60
    sum.hour = sum.hour + 1
  return sum

def increment(time,second):

  time.second=time.second+second
  

#print printTime(time)
#print addTime(t1,t2)

doneTime=addTime(currenttime,breadtime)

printTime(doneTime)
print increment(time,40)
