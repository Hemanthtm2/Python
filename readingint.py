#!/usr/bin/python 


h=100

f=open("filec.txt","w")
f.write(str(h))

f=open("filec.txt","r")
print f.read()
f.close()
