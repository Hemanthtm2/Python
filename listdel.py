#!/usr/bin/python 

list=['a','b','c','d','e','f']
print "List is\t",list
i=raw_input("Enter the item you want to delete from the list:\n")
i=int(i)
del list[i]
print list



