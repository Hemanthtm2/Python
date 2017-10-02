#!/usr/bin/python

f=open("test.txt","w")
f.write("line one\nline two\nline three\n")
f.close()

f=open("test.txt","r")
print f.readline()
print f.readline()
print f.readline()
