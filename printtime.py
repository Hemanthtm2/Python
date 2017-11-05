#!/usr/bin/python 

class Time:

  def printTime(time):
    print str(time.h) + ":" + \
        str(time.m) + ":" + \
        str(time.s)

currenttime=Time()

currenttime.h=9
currenttime.m=30
currenttime.s=14

currenttime.printTime()




