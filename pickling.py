#!/usr/bin/python 
import pickle
f=open("apache.txt","w")
pickle.dump(12.3,f)
pickle.dump([1,2,3],f)
f.close()
f=open("apache.txt","r")
#f.close()
print pickle.load(f)
print pickle.load(f)
#f.close()
