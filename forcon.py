#!/usr/bin/python 

prefixes="JKLMNOPQ"
suffix="ack"

for letter in prefixes:
 
 if letter == "O":
    result=letter+'u'+suffix
    print result
 elif letter == "Q":
    result=letter+'u'+suffix
    print result  

 else:
   result1=letter+suffix 
   print result1

