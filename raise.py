#!/usr/bin/pyrhon 

def inputnumber():

  x=input('Pick a number')
  if x==17:
    raise ValueError,'17 is a bad number'
  return x

print inputnumber()
