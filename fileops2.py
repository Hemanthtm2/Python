#!/usr/bin/python 


def fileops(file1,file2):

  f1=open("file1","r")
  f2=open("file2","w")

  while True:
   text=f1.read(50) 
   if text=="":
     break
   f2.write(text)
  f1.close()
  f2.close()
  return

fileops("fil1.txt","fil2.txt")
