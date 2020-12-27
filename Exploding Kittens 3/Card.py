'''
Created on Sep 16, 2020

@author: Maria
'''

'''
Created on Sep 16, 2020

@author: Maria
'''

import string
from Deck import Deck
from Player import Player

class Card:
    def __init__(self, name: str, pic: str):
        self.name = name
        self.img = pic
        self.card_names = ["diffuse", "nope", "attack", "favor", "see the future", "skip", "shuffle", "cattermelon", "beard cat", "rainbow-ralphing cat", "tacocat", "hairy potato cat"]
        self.basic = ["cattermelon", "beard cat", "rainbow-ralphing cat", "tacocat", "hairy potato cat"]
        