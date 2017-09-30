#!/usr/bin/python 
import math
def distance(x1,y1,x2,y2):
  dx=x2-x1
  dy=y2-y1
  sq=dx**2+dy**2
  result=math.sqrt(sq)
  return result
def area(radius):
  return math.pi*radius**2

def area2(xc,yc,xp,yp):
  radius=distance(xc,yc,xp,yp)
  result=area(radius)
  return result

print area2(1,2,4,6)
