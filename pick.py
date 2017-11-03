#!/usr/bin/python 
import pickle 

f=open("tes.txt","w")
pickle.dump(1,f)
pickle.dump(2,f)
pickle.dump([1,2,3],f)
f.close()

f=open("tes.txt","r")
x=pickle.load(f)
print x
print type(x)
y=pickle.load(f)
print y
print type(f)
z=pickle.load(f)
print z
print type(z)


