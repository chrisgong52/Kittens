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
from Player import Player
from Deck import Deck
from Card import Card
from Actions import Action
import string
import random
import math
from importlib.resources import path
from CardDisplay2 import CardDisplay
from PIL.ImageChops import screen


'''root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)'''
root = Tk()
root.state('zoomed')
canvas = Canvas(root, width=500, height=500)
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
#open_deck = Image.open(deck_img).resize((60, 100), Image.ANTIALIAS)
open_deck = Image.open(deck_img).resize((80, 120), Image.ANTIALIAS)

photo = ImageTk.PhotoImage(open_deck)
CARD_BUTTONS = {"draw": Button(root, image = photo, command = lambda:on_click("add", DECK.pop()))}

PLAYERS = []
cards_in_deck = {"diffuse": 1, "see the future": 1, "tacocat": 3}
DECK = Deck(cards_in_deck)


        
# Dectect which card was selected
def check_card_clicked():
    pass

def callback(event):
    print("clicked at", event.x, event.y)
    if event.y > HORIZ_LINE and event.x > CARDS[0] and event.x < CARDS[len(CARDS)-1]:
        for card in range(len(CARDS)-1):
            if event.x > CARDS[card] and event.x < CARDS[card+1]:
                print("Card " + str(card+1))
                break
        print("legal")
    else:
        print("illegal")

    
canvas.bind("<Button-1>", callback)
    

def on_click(action: string, name: string):
    global CARD_COUNT
    global PLAYERS
    #print("Button Clicked " + str(CARD_COUNT+1))
    if action == "add":
        CARD_COUNT = CARD_COUNT + 1
        
        ### for dynamic make current player
        PLAYERS[0].hand.append(name)
    if action == "remove":# and CARD_COUNT > 1:
        CARD_COUNT = CARD_COUNT - 1
        
        ### make selectable
        PLAYERS[0].hand.pop(-1)
    if action == "quit":
        global EXIT
        EXIT = True
    global CARDS
    #print(len(CARDS))
    init_cards(CARDS[0], CARDS[len(CARDS)-1], HORIZ_LINE, CARD_COUNT)
    
# Make it so that front card is fully seen
def init_cards(left, right, top, num_cards):
    #canvas.delete("all")
    #global CARDS 
    #print(len(CARDS))
    if num_cards == 0:
        return
    #canvas.create_line(left, top, right, top)
    card_size = int((right-left)/num_cards)
    indices = []
    for item in range(left, right+1, card_size):
        indices.append(item)
        #if item != left:
        #    canvas.create_line(item-card_size, top, item, top)
        #canvas.create_line(item, HORIZ_LINE, item, BOTTOM_BOUND)
    #CARDS = indices


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
CARD_WIDTH = 80
height = 120

#while milliseconds < milliseconds_start + 15000:
p1 = Player()
p1.draw(DECK)
while not EXIT:
    width = (int)((CARDS[-1] - CARDS[0])/(len(CARDS)-1))
#     while not DECK.isEmpty():
#         p1.draw(DECK)
    PLAYERS.append(p1)
    for item in CARD_BUTTONS.values():
        button = item
        button.configure(highlightbackground='red')
        button.place(relx=0.75, rely=0.5, anchor='center')

    disp = []
    left_bound = canvas.winfo_reqwidth()/2 - (CARD_WIDTH/2 + 15*len(PLAYERS[0].hand)-1)
#     left_bound = (canvas.winfo_reqwidth()/2)/500 - 40*(len(PLAYERS[0].hand)-1)/500
    top_bound = HORIZ_LINE
    for card in PLAYERS[0].hand:
        disp.append(CardDisplay(card, root, canvas, left_bound, top_bound, height))
        left_bound = left_bound + CARD_WIDTH/2
    canvas.update()
count = 0
    
