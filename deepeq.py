#!/usr/bin/python

class Point:
  pass

p1=Point()

p1.x=2
p1.y=3

p2=Point()

p2.x=2
p2.y=3

def samePoint(p1,p2):
  if p1.x==p2.x and p1.y==p2.y:
    return True
  else:
    return False

print samePoint(p1,p2)
