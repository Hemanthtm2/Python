#!/usrbin/python 

opps={'true':'false','right':'left'}

alias=opps
copy=opps.copy()

opps['true']='right'
print id(opps)
print id(alias)
print id(copy)
print alias
print copy
