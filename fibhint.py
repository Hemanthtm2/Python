#!/usr/bin/python 

def fibHint(n):
 
 if n==0 or n==1:
   return 1
 else:
   return fibHint(n-1)+fibHint(n-2)

print fibHint(5)

