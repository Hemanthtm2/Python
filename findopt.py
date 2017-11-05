#!/usr/bin/python 
def find(str,ch,start=0):
 index=start
 while index < len(str):
   if str[index]==ch:
      return index
   index=index+1
 return -1


print find("Apple","p",2)


