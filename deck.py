#!/usr/bin/python 

#from card import Card

class Deck:

  def __init__(self):
    self.cards=[]
    for suit in range(4):
      for rank in range(1,14):
        self.cards.append(Card(suit,rank))


def printCard(self):

  for cards in self.cards:
     print cards

#print printCard(cards)


