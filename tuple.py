#!/usr/bin/python

t1=('a',)

print type(t1)

t2=('a')

print type(t2)

t3=('a','b','c','d','e','f')

print t3[0]

print "slice of tuple",t3[1:]

t3=('A',)+t3[1:] 

print t3
