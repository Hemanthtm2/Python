#!/usr/bin/python 

def filecopy(oldf,newf):

  f1=open("oldf","r")
  f2=open("newf","w")
  while True:
   text=f1.readline()
   if text=="":
     break
   if text[0]=="#":
     continue
   f2.write(text)
  f1.close()
  f2.close()
  return

filecopy('oldf','newf') 
