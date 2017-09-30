#!/usr/bin/python 

def absoluteF(x):
  if 0<x<10:
    return x
  else:
    return 0

inp=raw_input("Enter the value")
inp=int(inp)
print absoluteF(inp)
