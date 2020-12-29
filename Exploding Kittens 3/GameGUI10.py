'''
Created on Dec 20, 2020

@author: Maria
'''

from tkinter import *
import datetime
import time
import NewCardGenerator
from PIL import ImageTk, Image
import StateTests
from Player2 import Player
from Deck import Deck
from Card import Card
from Actions import Action
import string
import random
import math
from importlib.resources import path
from CardDisplay2 import CardDisplay
from PIL.ImageChops import screen
from NewCardGenerator import current_player
#import webbrowser


root = Tk()
root.state('zoomed')
global CANVAS_WIDTH
CANVAS_WIDTH = 500
canvas = Canvas(root, width=CANVAS_WIDTH, height=500)
global HORIZ_LINE
HORIZ_LINE = 380
global CARDS
CARDS = [45, 105, 165, 225, 285, 345]
global END_BOUND
BOTTOM_BOUND = canvas.winfo_reqheight()
global CARD_COUNT
CARD_COUNT = 5
global BUTTON_2_CLICKED
BUTTON_2_CLICKED = False
global EXIT
EXIT = False
global CARD_IMAGES
global CARD_BUTTONS
global PLAYERS
global DECK
global DISCARD
global CURRENT_PLAYER
CURRENT_PLAYER = [0]
global CARD_WIDTH
global ACTION_LIST
ACTION_LIST = []
CARD_WIDTH = 80
global ACTION_CARDS
ACTION_CARDS = {"draw", "attack", "skip", "favor", "see the future", "shuffle"}



CARD_IMAGES = {"diffuse": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Diffuse.png",
               "nope": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Nope.png",
               "attack": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Attack.png",
               "favor": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Favor.png",
               "see the future": "/Users/Maria/Desktop/Exploding Kittens/Card Images/SeeTheFuture.png",
               "skip": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Skip.png",
               "shuffle": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Shuffle.png",
               "cattermelon": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Cattermelon.png",
               "beard cat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/BeardCat.png",
               "rainbow-ralphing cat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/RainbowCat.png",
               "tacocat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Tacocat.png",
               "hairy potato cat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HairyPotatoCat.png",
               "exploding kitten": "/Users/Maria/Desktop/Exploding Kittens/Card Images/ExplodingKitten.png"}


deck_img = "/Users/Maria/Desktop/Exploding Kittens/Card Images/Deck.png"
open_deck = Image.open(deck_img).resize((80, 120), Image.ANTIALIAS)

deck_photo = ImageTk.PhotoImage(open_deck)

discard_img = "/Users/Maria/Desktop/Exploding Kittens/Card Images/DiscardPile.png"
open_discard = Image.open(discard_img).resize((80, 120), Image.ANTIALIAS)

discard_photo = ImageTk.PhotoImage(open_discard)
CARD_BUTTONS = {"draw": Button(root, image = deck_photo, command = lambda:on_click("add", DECK.pop())),
                "Discard": Button(root, image = discard_photo, command = lambda:on_click("push", PLAYERS[CURRENT_PLAYER[0]].play))}

PLAYERS = []
cards_in_deck = {"diffuse": 4, "see the future": 4, "tacocat": 4}
discard = {}
DECK = Deck(cards_in_deck)
DISCARD = Deck(discard)



def get_player_bounds(player: Player):
    global CARD_WIDTH
    global CANVAS_WIDTH
    hand_size = (len(player.hand)-1)*CARD_WIDTH/2+CARD_WIDTH
    lower = canvas.winfo_reqwidth()/2 - (CARD_WIDTH/2 + 15*len(PLAYERS[0].hand)-1)
    upper = lower + hand_size
    return [lower, upper]
    
def callback(event):
    global PLAYERS
    global CURRENT_PLAYER
    global CARD_WIDTH
    #print("clicked at", event.x, event.y)
    bounds = get_player_bounds(PLAYERS[CURRENT_PLAYER[0]])
    click_x = event.x
    click_y = event.y
    print(click_x)
    if click_y >= HORIZ_LINE and click_x >= bounds[0] and click_x <= bounds[1]:
        dist = click_x - bounds[0]
        ind = int(dist//40+1)
        if ind > len(PLAYERS[CURRENT_PLAYER[0]].hand):
            ind = ind - 1
        ind = ind - 1
        if not PLAYERS[CURRENT_PLAYER[0]].is_selected(ind):
            if PLAYERS[CURRENT_PLAYER[0]].clickable(ind):
                print("clickable")
                PLAYERS[CURRENT_PLAYER[0]].change_state(ind)
                PLAYERS[CURRENT_PLAYER[0]].append_played(ind)
            else:
                PLAYERS[CURRENT_PLAYER[0]].deselect_all()
        else:
            PLAYERS[CURRENT_PLAYER[0]].change_state(ind)
            PLAYERS[CURRENT_PLAYER[0]].deselect_played(ind)
        print("hand: ", end = "")
        print(PLAYERS[CURRENT_PLAYER[0]].hand)
        print("played: ", end = "")
        print(PLAYERS[CURRENT_PLAYER[0]].play)
        print()
    else:
        print("illegal")

    
canvas.bind("<Button-1>", callback)
    

### name is list for push
def on_click(action: string, name: string):
    global CARD_COUNT
    global PLAYERS
    global DISCARD
    global ACTION_LIST
    global ACTION_CARDS
    global DECK
    global CURRENT_PLAYER
    for item in range(len(PLAYERS)):
            print("Player " + str(item+1) + " hand: ", end = "")
            PLAYERS[item].print()
    if action == "add":
        CARD_COUNT = CARD_COUNT + 1
        
        ### for dynamic make current player
        PLAYERS[0].hand.append(name)
        
    if action == "push":
        '''
        CHANGE THIS FOR FORMATTING FOR THE CARDS TO CORRECT DISCARD FORMAT LIKE IN TEST
        '''
        
        
        if len(name) != 0 and StateTests.check_valid(name, ACTION_CARDS, PLAYERS, CURRENT_PLAYER) != "invalid":
            action_list = []
            for item in range(len(PLAYERS[CURRENT_PLAYER[0]].hand)):
                if PLAYERS[CURRENT_PLAYER[0]].is_selected(item):
                    action_list.append(item)
            if len(action_list) > 1:
                action_list = [action_list]
            inds = []
            

            if len(name) != 0 and StateTests.check_valid(name, ACTION_CARDS, PLAYERS, CURRENT_PLAYER) != "invalid":
                if len(name) == 2 or (len(name) == 1 and name[0] == "favor"):
                    inds.append(input("input player to take card from: "))
                    inds.append(input("input index of card to take: "))
                elif len(name) == 3:
                    inds.append(input("input player to take card from: "))
                    inds.append(input("input name of card to take: "))
                elif len(name) == 5:
                    inds.append(input("name of card to take: "))
                elif len(name) == 1 and name[0] == "see the future":
                    input("press enter when done")
                    inds.append("enter")
                    
            ###
            ###    MAKE ACTION LIST LIST FOR EACH PLAYER, ADD CURRENT ACTION LIST TO THAT ONE
            ###    GLOBAL WILL BE PASSED IN TO HAVE SOMETHING FOR EACH PLAYER
            ###
            ACTION_LIST[CURRENT_PLAYER[0]] = action_list
            PLAYERS[CURRENT_PLAYER[0]].deselect_all()
            StateTests.play_card(DECK, DISCARD, PLAYERS, CURRENT_PLAYER, ACTION_LIST, inds)
            print("CARD PLAYED")
            PLAYERS[CURRENT_PLAYER[0]].print()
            print()
        else:
            PLAYERS[CURRENT_PLAYER[0]].deselect_all()
        
        
    if action == "remove":
        CARD_COUNT = CARD_COUNT - 1
        
        ### make selectable
        PLAYERS[0].hand.pop(-1)
    if action == "quit":
        global EXIT
        EXIT = True
    global CARDS
    init_cards(CARDS[0], CARDS[len(CARDS)-1], HORIZ_LINE, CARD_COUNT)
    
# Make it so that front card is fully seen
def init_cards(left, right, top, num_cards):
    if num_cards == 0:
        return
    card_size = int((right-left)/num_cards)
    indices = []
    for item in range(left, right+1, card_size):
        indices.append(item)


# display other players' hands via card back
def init_other_players(host_player: int, left_bound: int, root, canvas):
    global PLAYERS
    global CARD_WIDTH
    print("jflkds")
    ### testing one player
    for item in range(len(PLAYERS)):
        if item != host_player:
            temp = []
            for card in PLAYERS[item].hand:
                temp.append(CardDisplay("card_back", root, canvas, left_bound, 0, 180))
                left_bound = left_bound + CARD_WIDTH/2


milliseconds_start = int(round(time.time() * 1000))
milliseconds = int(round(time.time() * 1000))



init_cards(CARDS[0], CARDS[len(CARDS)-1], HORIZ_LINE, CARD_COUNT)



'''
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )'''


btn2 = Button(root, text = "Remove Card", command = lambda:on_click("remove", ""))
btn3 = Button(root, text = "Exit", command = lambda:on_click("quit", ""))

'''
for item in CARD_BUTTONS.values():
    button = item
    button.configure(highlightbackground='red')
    button.place(relx=0.75, rely=0.5, anchor='center')
    #button.pack()'''


btn2.pack()
btn3.pack()
canvas.pack()


width = (int)((CARDS[-1] - CARDS[0])/(len(CARDS)-1))


#while milliseconds < milliseconds_start + 15000:
p1 = Player()
p2 = Player()
PLAYERS.append(p1)
PLAYERS.append(p2)
p1.draw(DECK)
for player in PLAYERS:
    ACTION_LIST.append([])
p2_hand_size = 3
while(p2_hand_size > 0):
    p2.draw(DECK)
    p2_hand_size = p2_hand_size - 1

for item in CARD_BUTTONS.keys():
    button = CARD_BUTTONS[item]
    #button.configure(highlightbackground='red')
    if item == "draw":
        button.place(relx=0.75, rely=0.5, anchor='center')
    else:
        button.place(relx=0.25, rely=0.5, anchor='center')
        

while not EXIT:
    width = (int)((CARDS[-1] - CARDS[0])/(len(CARDS)-1))
    disp = []
    left_bound = canvas.winfo_reqwidth()/2 - (CARD_WIDTH/2 + 15*len(PLAYERS[0].hand)-1)
    temp_left = left_bound
    top_bound = HORIZ_LINE
    for card in PLAYERS[CURRENT_PLAYER[0]].hand:
        disp.append(CardDisplay(card, root, canvas, temp_left, top_bound, 0))
        temp_left = temp_left + CARD_WIDTH/2
    #init_other_players(CURRENT_PLAYER[0], left_bound, root, canvas)
    
    
    for item in range(len(PLAYERS)):
        if item != CURRENT_PLAYER[0]:
            temp = []
            other_left = canvas.winfo_reqwidth()/2 - (CARD_WIDTH/2 + 15*len(PLAYERS[item].hand)-1)
            for card in PLAYERS[item].hand:
                temp.append(CardDisplay("card_back", root, canvas, other_left, 0, 180))
                other_left = other_left + CARD_WIDTH/2
    #print(canvas.winfo_reqwidth())
    canvas.update()
count = 0
    
