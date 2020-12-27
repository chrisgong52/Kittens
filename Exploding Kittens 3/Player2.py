'''
Created on Sep 16, 2020

@author: Maria
'''

import string
from Deck import Deck

class Player:
    def __init__(self):
        self.hand = []
        self.basic = ["cattermelon", "beard cat", "rainbow-ralphing cat", "tacocat", "hairy potato cat"]
        self.actions = {1: self.action_card, 2: self.match, 3: self.match, 5: self.different}
        self.play = []

    def __contains__(self, key: string):
        return key in self.hand
    
    def __eq__(self, other):
        if len(self.hand) != len(other.hand):
            return False
        for item in range(len(self.hand)):
            if self.hand[item] != other.hand[item]:
                return False
        return True
            
    def action_card(self, indices: list):
        if self.hand[indices[0]] not in self.basic and indices[0] < len(self.hand) and (self.hand[indices[0]] != "diffuse" and "exploding kitten" not in self.hand):
            return [self.hand.pop(indices[0])]
        return []
        
    def match(self, indices: list):
        for item in range(len(indices)-1):
            if self.hand[indices[item]] != self.hand[indices[item + 1]]:
                return []
        self.remove_played(indices)
        return ["match " + str(len(indices))]
    
    def different(self, indices: list):
        temp = []
        for item in range(len(indices)):
            if self.hand[item] in temp:
                return []
        self.remove_played(indices)
        return ["different"]
        
    def draw(self, deck: Deck):
        self.hand.append(deck.pop())
    
    def print(self):
        print(self.hand)
        
    def check_for_kitten(self):
        if "exploding kitten" in self.hand:
            return True
        return False
    
    def lose(self):
        if self.check_for_kitten():
            if "diffuse" not in self.hand:
                return True
        return False
    
    # string list of indices
    def str_to_int(self, l: list):
        if l[0] == "draw":
            return l
        out = []
        for item in l:
            out.append(int(item))
        return out
    
    def valid_ind(self, indices: list):
        for item in indices:
            if item >= len(self.hand):
                return False
        return True
    
    def remove_played(self, indices: list):
        out = []
        for card in range(len(indices)):
            #print(self.hand[indices[card] - card])
            out.append(self.hand.pop(indices[card]-card))
        #print(out)
        return out
    
    def play(self, deck: Deck):
        indices = self.str_to_int(input("Input indices of cards to play: ").split())
        if indices[0] == "draw":
            return ['draw']
        # or self.actions[len(indices)](indices) == []????? (In while, but not sure if necessary and extra call to actions
        ### This is to make sure the thing isn't draw, check before for draw and return accordingly
        ### fails if wrong indices inputted
        while not self.valid_ind(indices) or (len(indices) == 1 and self.hand[indices[0]] == "diffuse" and "exploding kitten" not in self.hand) or len(indices) not in self.actions.keys() or (len(indices) == 1 and self.hand[indices[0]] in self.basic):
            indices = self.str_to_int(input("Input valid indices of cards to play: ").split())
        return self.actions[len(indices)](indices)
    
    def get_ind(self):
        ind = int(input("Enter index: "))
        while ind < 0 or ind > len(self.hand)-1:
            ind = int(input("Enter valid index: "))
        return ind
    
    def get_card_name(self):
        name = input("Enter card name: ")
        while name not in self.hand:
            name = input("Enter valid name: ")
        return name
        
    def select(self, index: int):
        self.hand[index] = "highlight " + self.hand[index]
    
    def deselect(self, index: int):
        self.hand[index] = self.hand[index][10:]
        
    def is_selected(self, index: int):
        return self.hand[index][0:4] == "high"
    
    def change_state(self, index: int):
        #print(self.hand[index])
        if self.hand[index][0:4] == "high":
            self.deselect(index)
        else:
            self.select(index)
            
    def clickable(self, index):
        if len(self.play) == 2:
            if self.play[0] == self.play[1]:
                return self.hand[index] == self.play[0]
            else:
                return self.hand[index] != self.play[0] and self.hand[index] != self.play[1]
        elif len(self.play) == 3:
            temp = []
            for item in self.play:
                if item in temp:
                    return False
                temp.append(item)
            if self.hand[index] in temp:
                return False
            return True
        elif len(self.play) < 4:
            return True
        elif len(self.play) == 4:
            temp = []
            for item in self.play:
                if item in temp:
                    return False
                temp.append(item)
            return True
        else:
            return False
        
    def deselect_all(self):
        for item in range(len(self.hand)):
            if self.is_selected(item):
                self.deselect(item)
        self.play = []
                
    def append_played(self, index: int):
        if self.is_selected(index):
            self.play.append(self.hand[index][10:])
        else:
            self.play.append(self.hand[index])
        #print(self.hand[index])

    def deselect_played(self, index: int):
        self.play.remove(self.hand[index])
        #print(self.hand[index])
        
    def remove(self, ind: int):
        self.hand.pop(ind)
        
    def play_empty(self):
        return len(self.play) == 0
    
    
    