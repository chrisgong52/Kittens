'''
Created on Sep 18, 2020

@author: Maria
'''

import string
import random
from Deck import Deck
from Card import Card

class Action:
    def __init__(self):
        self.actions = {"diffuse": self.diffuse,
                        "nope": self.nope,
                        "attack": self.attack,
                        "favor": self.favor,
                        "see the future": self.see_the_future,
                        "skip": self.skip,
                        "shuffle": self.shuffle,
                        "match 2": self.match_two,
                        "match 3": self.match_three,
                        "different": self.different,
                        "draw": self.draw}
        
    def print(self):
        print(self.name, self.img)
        
    def peek_the_future(self, deck: Deck):
        count = 0
        out = []
        while count < 3:
            out.append(deck.pop())
            count = count + 1
        return out
        
    def push_deck(self, deck: Deck, pushed: list):
        for card in reversed(pushed):
            deck.push(card)
            #self.hand.remove(card)
        
    def attack(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        ###
        # INSERT A WAIT FOR NOPE
        ###
        print("ATTACK")
        ### DON'T INCREMENT HERE
        #######current_player[0] = current_player[0] + 1 if current_player[0] + 1 < len(players) else 0
        
        ### DON'T DRAW TWICE, BUT MAKE TAKE TWO TURNS
        ### Increment by 3 because 1 subtracted off the bat every time attack[0] > 0
        if attack[0] == 0:
            attack[0] = attack[0] + 1
        else:
            attack[0] = attack[0] + 2
        
    def draw(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        print("DRAWING ACTION")
        players[current_player[0]].draw(deck)
        
    def favor(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        ###
        # INSERT A WAIT FOR NOPE
        ###
        print("FAVOR")
        ''' dynamic input
        ### target = int(input("Enter target index: "))'''
        target = int(inds[0])
        inds.pop(0)
        while target > len(players)-1 or target < 0 and len(target.hand) > 0 or target == current_player[0]:
            target = int(input("Enter valid index: "))
            
        ###########
        # HAVE TARGET PICK THE CARD
        ###########
        ind = players[target].get_ind()
        players[current_player[0]].hand.append(players[target].hand.pop(ind))   
        
    def see_the_future(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        ###
        # INSERT A WAIT FOR NOPE
        ###
        print("SEE THE FUTURE")
        temp = self.peek_the_future(deck)
        print(temp)
        if inds[0] != 'enter':
            input("Hit enter when done")
        inds.pop(0)
        self.push_deck(deck, temp)
        
    def skip(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        print("SKIP")
        current_player[0] = current_player[0] + 1
        return current_player
        
    def shuffle(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        print("SHUFFLE")
        deck.shuffle()
        return deck
        
    def nope(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        pass
        print("NOPE")
        
    def diffuse(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        pass
        print("DIFFUSE")
        
    def match_two(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        print("MATCH 2")
        ''' dynamic input
        ### target = int(input("Enter target index: "))'''
        target = int(inds[0])
        inds.pop(0)
        while target > len(players)-1 or target < 0 and len(target.hand) > 0 or target == current_player[0]:
            target = int(input("Enter valid index: "))
            ### RESETS OTHER INDEX SO CAN RESELECT INDEX TO TAKE
            inds[0] = -1
        ''' dynamic input
        ###ind = int(input("Enter which card to take: "))'''
        #print("inds: ", end = "")
        #print(inds)
        ind = int(inds[0])
        inds.pop(0)
        while ind > len(players[target].hand)-1 or ind < 0:
            ind = int(input("Enter valid card to take: "))
        taken = players[target].hand.pop(ind)
        players[current_player[0]].hand.append(taken)
        print("taken card: " + taken)
        
    def match_three(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        print("MATCH 3")
        ''' dynamic input
        ### target = int(input("Enter target index: "))'''
        target = int(inds[0])
        inds.pop(0)
        while target > len(players)-1 or target < 0 and len(target.hand) > 0 or target == current_player[0]:
            target = int(input("Enter valid index: "))
        ''' dynamic input
        ### name = input("Enter name of card to take: ")'''
        name = inds[0]
        inds.pop(0)
        ### don't give second chance, just one chance to enter card to take
        ###while name not in self.card_names:
        ###    name = int(input("Enter valid card to take: "))
        if name in players[target].hand:
            players[current_player[0]].hand.append(players[target].hand.remove(name)) 
        
    def different(self, deck: Deck, current_player: list, players: list, attack: list, discard: Deck, inds: list):
        print("DIFFERENT")
        ''' dynamic input
        ### name = input("Enter a card in the discard pile: ")'''
        name = inds[0]
        inds.pop(0)
        while name not in discard.deck():
            name = input("Enter a valid card in the discard pile: ")
        players[current_player[0]].append(name)
        discard.remove(name)
    
    def action(self, deck: Deck, current_player: list, players: list, attack: list, action: list, discard: Deck, inds: list):
        self.actions[action](deck, current_player, players, attack, discard, inds)
        
        