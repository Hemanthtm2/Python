#!/usr/bin/python 

import string 

name="What is your name"

list=string.split(name)
print list
print string.join(list,'_')
