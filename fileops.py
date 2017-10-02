#!/usr/bin/python 

def copyFiles(oldf,newf):
  f1=open("oldf","r")
  f2=open("newf","w")
  #f1.write("Hello this is python tuitorial")
  while True:
    text=f1.read(50)
    if text=="":
      break
    f2.write(text)

  f1.close()
  f2.close()
  return

copyFiles("old.txt","new.txt")
