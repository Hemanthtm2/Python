#!/usr/bin/python 

def exist(filename):
 try:
   f=open(filename)
   f.close()
   return True
 except IOError:
   return False

print exist("tes.txt")
print exist("oo.txt")


