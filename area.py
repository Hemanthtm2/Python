#!/usr/bin/python 

import math
def areaF(radius):
  return math.pi*radius**2

rad=raw_input("Enter the value of radius")
rad=int(rad)
print areaF(rad)

