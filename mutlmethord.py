#!/usr/bin/python 

class Point:

  def __init__(self,x=0,y=0):

   self.x=x
   self.y=y

  def __str__(self):

   return '(' + str(self.x) + "," + str(self.x) + ')' 


  def __mul__(self,other):
    return self.x*other.x,self.y*other.y

  def __rmul__(self,other):
    return Point(other*self.x,other*self.y)

def multAdd(x,y,z):
   return x*y+z
 

p1=Point(3,4)

p2=Point(2,6)

print multAdd(p1,p2,2)

