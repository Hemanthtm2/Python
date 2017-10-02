#!/usr/bin/python 

f=open("name.txt","w")
f.write("My name is Python!!!")
f.close()
#name=f.read()
#print name

f=open("name.txt","r")

#print "\n", f.read()

print f.read(7)
print f.read(1000004)
