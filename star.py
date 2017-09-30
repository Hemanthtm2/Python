#!/usr/bin/python 


def countD(x):
  if x==0:
    print "Enter a star to continue"
  else:
    print x
    countD(x-1)

countD(10)
