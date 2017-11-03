#!/usr/bin/python 
import pickle
f=open("vh.txt","w")
pickle.dump(1,f)
pickle.dump([1,2,3],f)
f.close()
f=open("vh.txt","r")
print pickle.load(f)
print pickle.load(f)
f.close()
