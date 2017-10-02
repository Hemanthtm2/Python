#!/usr/bin/python 
letterc={}

for letter in "Mississippi":
  letterc[letter]=letterc.get(letter,0)+1
  
print letterc

letteritems=letterc.items()
print letteritems
#letteritems=letter.sort()
#print letteritems
