#!/usr/bin/python 
import copy
class Point:

  pass

p1=Point()

p1.x=10
p1.y=20

p2=Point()

p2=copy.copy(p1)

if p1==p2:

  print True 

else:

  print False

print p1

print p2
