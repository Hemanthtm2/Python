#!/usr/bin/python 

import pickle
f=open("nginx.txt","w")
pickle.dump(1.2,f)
pickle.dump([10,20,30],f)

f.close()

f=open("nginx.txt","r")
x=pickle.load(f)
print f
y=pickle.load(f)

print y

print type(x)

print type(y)






