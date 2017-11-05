#!/usr/bin/python 

class Point:

  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
  def __str__(self):
    return '(' + str(self.x) + "," + str(self.y) + ')'

  def __add__(self,other):
    return Point(self.x+other.x,self.y+other.y)
  def __sub__(self,other):
    return Point(self.x-other.x,self.y-other.y)
  def __mul__(self,other):
    return self.x*other.x+self.y*other.y
  def __rmul__(self,other):
    return Point(other*self.x,other*self.y)


p6=Point(4,5)
p7=Point(6,8)

p9=2*p6

print p9 

p8=p6*p7

print p8


p3=Point(9,5)
p4=Point(6,3)

p5=p3-p4

print p5


p1=Point(2,3)
p2=Point(4,5)

p3=p2+p1

print p3




pobj=Point(3,2)

print pobj

pobj1=Point()

print pobj1
