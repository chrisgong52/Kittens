'''
Created on Sep 16, 2020

@author: Maria
'''

import string
import random

class Deck:
    # initialize the deck the first time
    def __init__(self, card_dict: dict):
        ### For manual tests
        if type(card_dict) == list:
            self.deck = card_dict
        else:
            self.deck = self.initialize_deck(card_dict)
            
    def __eq__(self, other):
        if len(self.deck) != len(other.deck):
            return False
        for item in range(len(self.deck)):
            if self.deck[item] != other.deck[item]:
                return False
        return True
    
    def isEmpty(self):
        return len(self.deck) == 0
    
    def to_dict(self):
        temp = {}
        for item in self.deck:
            if item in temp:
                temp[item] = temp[item] + 1
            else:
                temp[item] = 1
        
    def len(self):
        return len(self.deck)
        
    # put cards from dictionary into random list
    def initialize_deck(self, deck: dict):
        out = []
        while (deck):
            temp = random.choice(list(deck.keys()))
            out.append(temp)
            deck[temp] = deck[temp] - 1
            if(deck[temp] == 0):
                deck.pop(temp)
        return out
    
    # shuffle cards in deck by putting into dict then reinitializing list
    def shuffle(self):
        ### TEMPORARY FOR TESTING
        self.deck.append(self.deck.pop(0))
        
        ### REAL THING
        '''temp_dict = {}
        for card in self.deck:
            if temp_dict.__contains__(card):
                temp_dict[card] = temp_dict[card] + 1
            else:
                temp_dict[card] = 1
        self.deck = self.initialize_deck(temp_dict)'''
        
        

    # return top card of deck
    def peek(self):
        return self.deck[-1]
    
    def pop(self):
        temp = self.deck.pop(-1)
        return temp
    
    def push(self, card: string):
        self.deck.append(card)
        
    # removes index inputted (0 based), doesn't check bounds
    def remove(self, index: int):
        return self.deck.pop(index)
        
    def print(self):
        print(self.deck)
        
    def size(self):
        return len(self.deck)
    
    def insert_index(self, index: int, value: string):
        self.deck.insert(index, value)
        
    def __len__(self):
        return len(self.deck)
    
    def ins_rand(self, card: string):
        self.deck.insert(random.randint(0, len(self.deck)-1), card)