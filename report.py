#!/usr/bin/python 

#wages={Hemanth:100,Varada:50,Vasanth:25}

def report(wages):

  students=wages.keys()
  for student in students:
    print "%s %12d" %(student,wages[student])



wages={"Hemanth":100,"Varada":50,"Vasanth":25}

report(wages)
