#!/usr/bin/python 

f=open("text.dat","w")

print f

f.write("Just opening a file")
print f
f.close()
f=open("text.dat","r")
print f.read()

print f
