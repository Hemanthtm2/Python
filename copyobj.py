#!/usr/bin/python 
import copy
class Point:
 pass

p1=Point()
p1.x=2
p1.y=3
p2=copy.copy(p1)

print p1
print p2

 
