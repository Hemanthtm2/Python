#!/usr/bin/python

class Point:

 def __add__(self,other):
     return Point(self.x+other.x,self.y+other.y)

p1=Point(3,2)
p2=Point(4,5)
p3=p1+p2

print p3
