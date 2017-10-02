#!/user/bin/python 

previous={0:1,1:1}

def fib(n):

  if previous.has_key(n):
    return previous[n]
  else:
    newvalue=fib(n-1)+fib(n-2)
    previous[n]=newvalue
    return newvalue

print fib(10)
