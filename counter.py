#!/usr/bin/python 

def Counter():
  word=raw_input("Enter the word you want to check:\n")
  count=0
  for char in word:
   if char == 'a':
     count=count+1
  print count

Counter() 
