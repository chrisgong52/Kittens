'''
Created on Aug 9, 2020

@author: Maria
'''

from Deck import Deck
import string
from Player import Player
#import NewPlayerHand
import random
#import pygame

INIT_HAND_SIZE = 4
num_players = 2
current_player = [0]
can_play = []

cards = {"diffuse": 6,
         "nope": 5,
         "attack": 4,
         "favor": 4,
         "see the future": 5,
         "skip": 4,
         "shuffle": 4,
         "cattermelon": 4,
         "beard cat": 4,
         "rainbow-ralphing cat": 4,
         "tacocat": 4,
         "hairy potato cat": 4}

undo = {"diffuse": "undo_diffuse",
        "nope": "undo_nope",
        "attack": "undo_attack",
        "favor": "undo_favor",
        "see the future": "undo_see_future",
        "skip": "undo_skip",
        "shuffle": "undo_shuffle",
        "match": "undo_match",
        "all diff": "undo_five_of_kind"}

'''actions = {"diffuse": ,
           "nope": ,
           "attack": ,
           "favor": ,
           "see the future": ,
           "skip": ,
           "shuffle": }'''

# to allow people with nopes to play
# after card played, check everyone in this
# list to see if they want to play a nope
current_player_list = []

# Give each player a diffuse
def init_diffuse(cards: dict, players: list):
    for player in players:
        player.hand.append("diffuse")
        cards["diffuse"] = cards["diffuse"] - 1
        
# Initialize players and give one diffuse
def initialize_players(cards: dict, num_players: int):
    players = []
    for _ in range(0,num_players):
        players.append(Player())
    init_diffuse(cards, players)
    return players

# If one card has count of 0, remove key from dict before
# making deck
def remove_none(cards: dict):
    remove = []
    for card in cards:
        if cards[card] == 0:
            remove.append(card)
    for card in remove:
        cards.pop(card)

# Have each player draw 4 more card (after diffuse)
# After all drawn, print players' hands  
def initialize_hands(deck: Deck, players: list):
    count = 0
    while(count < INIT_HAND_SIZE):
        for player in players:
            player.draw(deck)
        count = count + 1
    for player in players:
        player.print()

# Insert one less exploding kitten into the deck than
# the count of players
def insert_kittens(deck: Deck, num_kit: int):
    for _ in range(0, num_kit):
        deck.insert_index(random.randint(0,deck.size()-1), "exploding kitten")

# Make the deck and distribute cards to players
# Return the deck that has been created from cards
def init_deck(cards: dict, num_players: int):
    remove_none(cards)
    deck = Deck(cards)
    initialize_hands(deck, players)
    insert_kittens(deck, num_players-1)
    
    return deck
    
    
# Have player draw one card from the deck and print player's hand    
def player_draw(players: list, current_player: list, deck: Deck):
    players[current_player[0]].draw(deck)
    players[current_player[0]].print()
    
# Select cards from hand that are played    
def select_played(players: list, current_player: list):
    return players[current_player[0]].select_played()
    
    
#    CHECKED
# increase the current player by 1
def play_skip(current_player: list, num_players: int):
    if current_player[0] == num_players-1:
        current_player[0] = 0
    else:
        current_player[0] = current_player[0] + 1

#    CHECKED I think
def play_shuffle(deck: Deck):
    deck.shuffle()
    
#    CHECKED
# peek 3 cards then push them back on the deck
def play_see_the_future(player: Player, deck: Deck):
    player.play_future(deck)
    
# target a player, return the int index of the targetted player
def pick_target(players: list, current_player: list):
    while True:
        temp = int(input("Enter player to target (zero based): "))
        if temp < len(players) and temp != current_player[0]:
            return temp
        else:
            print("Enter valid number")

# player selects which cards to give other player
# when targetted            
def pick_card(hand: list):
    while True:
        played = int(input("input index of card to give: "))
        if played < len(hand) and played >= 0:
            return played
    
#    CHECKED
# gets target and makes them draw 2 cards
def play_attack(players: list, current_player: list, deck: Deck):
    #deck.print()
    target = pick_target(players, current_player)
    player_draw(players, [target], deck)
    player_draw(players, [target], deck)
    players[target].print()
    
#    CHECKED
# gets target player, has target player chose a card to remove from hand
# adds the removed card to the current player's hand
def play_favor(players: list, current_player: list):
    target = pick_target(players, current_player)
    hand = players[target].hand
    played = pick_card(hand)
    players[current_player[0]].hand.append(players[target].hand.pop(played))
    
# play three of a kind
def play_three_match(current_player: list, players: list, cards: dict):
    target = pick_target(players)
    card = players[current_player[0]].choose_rand_card(cards)
    
    if card in players[target].hand:
        players[current_player[0]].append(players[target].remove(card))
    else:
        print("Card not in target's hand")
    
    
def check_nope(players: list, current_player: list):
    for player in players:
        if "nope" in player.hand:
            can_play.append(player)
    if players[current_player[0]] not in can_play:
        can_play.append(players[current_player[0]])
    
    
    
def play_action_card(card: string, current_player: list, players: list, deck: Deck):
    if card == "skip":
        #print(current_player)
        play_skip(current_player, len(players))
        #print(current_player)
    if card == "see the future":
        #deck.print()
        play_see_the_future(players[current_player[0]], deck)
        #deck.print()
    if card == "attack":
        play_attack(players, current_player, deck)
    if card == "favor":
        play_favor(players, current_player)
    if card == "shuffle":
        #deck.print()
        play_shuffle(deck)
        #deck.print()
    
#def play_match(cards: list):
#    print(cards)
    
    
    
# Take care of removing cards from hand and pushing
# onto discard pile and undo pile
def play_cards(players: list, cards: list, discard_pile: Deck, undo_pile: Deck, current_player: list, deck: Deck):
    discard_pile.push(cards)
    if len(cards) == 1:
        play_action_card(cards[0], current_player, players, deck)
        undo_pile.push(cards[0])
    elif len(cards) == 2 or len(cards) == 3:
        undo_pile.push("match")
    else:
        undo_pile.push("all diff")
    
# Main function, make player play a card
def take_turn(players: list, current_player: list, deck: Deck, discard: Deck, undo: Deck):
    cont = input("Press enter to continue, \'quit\' to quit: ")
    while cont != "quit":
        cards = players[current_player[0]].select_played()
        while len(cards) != 0:
            play_cards(players, cards, discard, undo, current_player, deck)
            cards = players[current_player[0]].select_played()
            
        player_draw(players, current_player, deck)
        if current_player[0] < len(players)-1:
            current_player[0] = current_player[0] + 1
        else:
            current_player[0] = 0
        cont = input("Press enter to continue, \'quit\' to quit: ")
    

if __name__ == "main":
    discard_pile = Deck({})
    undo_pile = Deck({})
    
    test_deck = Deck({"exploding kitten": 5})
    players = initialize_players(cards, num_players)
    deck = init_deck(cards, num_players)
    player_draw(players, current_player, deck)
    take_turn(players, current_player, deck, discard_pile, undo_pile)