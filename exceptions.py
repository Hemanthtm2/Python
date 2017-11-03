#!/usr/bin/python


filename=raw_input("Enter the file name")
try:
  f=open("filename","r")
except IOError:
  print "There is no file named",filename


