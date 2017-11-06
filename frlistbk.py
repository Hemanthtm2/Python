#!/usr/bin/python

import copy 
class Point:
  def __init__(self,x=0,y=0):
     self.x=x
     self.y=y
  def __str__(self):
    return '(' + str(self.x) + "," + str(self.y) + ')'
  def reverse(self):
    self.x,self.y=self.y,self.x

  
def fAndb(front):
    back=copy.copy(front)
    back.reverse()
    print str(front)+str(back)



mylist=[1,2,3,4]

print fAndb(mylist)

p=Point(3,4)

print fAndb(p)
