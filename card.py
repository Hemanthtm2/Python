#!/usr/bin/python 

class Card:

   suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
   rankList = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King"]

   def __init__(self,suit=0,rank=2):
     self.suit=suit
     self.rank=rank

   def __str__(self):
     return(self.rankList[self.rank] + " of " + self.suitList[self.suit])

   def __cmp__(self,other):
     if self.suit>other.suit:
        return 1
     if self.suit<other.suit:
        return -1
     if self.rank>other.rank:
        return 1
     if self.rank<other.rank:
        return -1
     return 0 




card1=Card(1,11)

print card1

#print card1.suitList[1]

card2=Card(1,3)
card3=Card(1,4)

print card2<card3
