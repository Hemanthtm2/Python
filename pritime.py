#!/usr/bin/python 


class Time:
  pass

time=Time()
time.hr=10
time.mi=20
time.se=00

def printT(time):
  print  str(time.hr) + ":" + \
         str(time.mi) + ":" + \
         str(time.se)


printT(time)

