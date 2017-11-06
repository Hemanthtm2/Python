#!/usr/bin/python 

class Point:

  def __init__(self,x=0,y=0):
      self.x=x
      self.y=y


  def __str__(self):
     return '(' + str(self.x) + "," + str(self.y) + ')'




def multadd(x,y,z):
     return x*y+z

print multadd(2,3,4)

p1=Point(3,2)
p2=Point(2,1)

