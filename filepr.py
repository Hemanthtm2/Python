#!/usr/bin/python 


#f1=open("mytext.txt","w")
#f1=open("mytext.txt","r")

f1=open("mytext.txt","w")
f1.write("My number isi %d" %50)
f1.close()
f1=open("mytext.txt","r")
f1.read()
