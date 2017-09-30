#!/usr/bin/python 

def fact(n):
  if not isinstance(n,int):
    print "Factorial is only for integers"
    return -1
  elif n<0:
    print "Number shuold be +ve integer"
    return -1
  elif n==1:
    return 1
  else:
    return n*fact(n-1)

print fact(6)
#print fact(1.5)
#print fact(5)
   
