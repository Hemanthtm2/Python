#!/usr/bin/python 

f1=open("fileX.txt","w")

print f1

f1.write("Hello Python!")
x=50

f1.write(str(x))
f1=open("fileX.txt","r")

print f1.read()


