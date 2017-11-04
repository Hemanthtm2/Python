#!/usr/bin/python 

class Point:
  pass


p1=Point()

p1.x=10

p1.y=20

p2=Point()
p2.x=15
p2.y=25

p2=p1

if p1==p2:
  print True 

else:

  print False

def samePoint(p1,p2):

  if p1.x==p2.x and p1.y==p2.y:
    print  True
  else: 
    print  False 

print samePoint(p1,p2)



  

