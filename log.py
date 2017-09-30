#!/usr/bin/python

import math

def printLogof(x):
  if x<=0:
    print "Positive numbers only, please."
    return
  else:

    result = math.log(x)
    print "The log of x is", result

printLogof(2)
printLogof(-2)
