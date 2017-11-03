#!/usr/bin/python

class Point:

 pass

p1=Point()
p2=Point()
p1.x=10
p1.y=20
p2.x=10
p2.y=20

def checkPoint(p1,p2):

 if p1.x==p2.x and p1.y==p2.y:
    return True
 else:
    return False 


print checkPoint(p1,p2)



