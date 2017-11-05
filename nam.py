#!/usr/bin/python 

class Name:

  def printName(name):
     print str(name.n1) 
     print str(name.n2)
    

  def __init__(self,n1="Hemanth",n2="Varada"):
     self.n1=n1
     self.n2=n2

curname=Name("hh","jj")
#name.n1="A"
#name.n2="B"
curname.printName()

