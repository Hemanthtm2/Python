#!/usr/bin/python 
from card import Card
card=Card()
class Deck:
  
   def __init__(self):
     self.cards=[]
     for suit in range(4):
       for rank in range(1,13):
         return self.cards.append(Card(suit,rank))

   def __str__(self):
     s=""
     for i in range(len(self.cards)):
       s = s + " "*i + str(self.cards[i]) + "\n"
     return s

deck = Deck()
print deck 
