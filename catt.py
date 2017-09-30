#!/usrbin/python 

def printTwice(bruce):
  print bruce,bruce

def catTwice(part1,part2):
  cat=part1+part2
  printTwice(cat) 

chapt1="Chapter one is C\n"
chapt2="Chapter two is C++\n"
catTwice(chapt1,chapt2)
