#!/usr/bin/python 

class Point:

  def __init__(self,x=0,y=0):
     self.x=x
     self.y=y

  def __str__(self):
     
    return '(' + str(self.x) + ','  + str(self.y) + ')'

  def __add__(self,other):
     
    return Point(self.x+other.x,self.y+other.y)

p1=Point(3,2)
p2=Point(4,5)

p3=p1+p2

print p3


p=Point()

print p
