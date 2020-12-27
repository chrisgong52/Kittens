'''
Created on Dec 20, 2020

@author: Maria
'''

import tkinter as tk
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


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
global HORIZ_LINE
HORIZ_LINE = 300
global CARDS
CARDS = [45, 105, 165, 225, 285, 355]
global END_BOUND
BOTTOM_BOUND = canvas.winfo_reqheight()
global CARD_COUNT
CARD_COUNT = 5
global BUTTON_2_CLICKED
BUTTON_2_CLICKED = False
global EXIT
EXIT = False



# INSERTING IMAGE
image = Image.open('/Users/Maria/Desktop/Projects/TestImage.jpg')
image = image.resize((450, 350), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
panel = tk.Label(root, image = img)

card_images = {"diffuse": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Diffuse.png",
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






# Make it so that front card is fully seen
def init_cards(left, right, top, num_cards):
    canvas.delete("all")
    if num_cards == 0:
        return
    #canvas.create_line(left, top, right, top)
    card_size = int((right-left)/num_cards)
    indices = []
    for item in range(left, right+1, card_size):
        indices.append(item)
        if item != left:
            canvas.create_line(item-card_size, top, item, top)
        canvas.create_line(item, HORIZ_LINE, item, BOTTOM_BOUND)
    global CARDS 
    CARDS = indices
        
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

    
####################################canvas.bind("<Button-1>", callback)

#canvas.create_line(CARDS[0], HORIZ_LINE, CARDS[len(CARDS)-1], HORIZ_LINE)
#for item in CARDS:
#    canvas.create_line(item, HORIZ_LINE, item, BOTTOM_BOUND)

#init_cards(CARDS[0], CARDS[len(CARDS)-1], HORIZ_LINE, CARD_COUNT)
    

def print_btn2():
    print(BUTTON_2_CLICKED)
    
def on_click(num: int):
    global CARD_COUNT
    #print("Button Clicked " + str(CARD_COUNT+1))
    if num == 1:
        CARD_COUNT = CARD_COUNT + 1
    if num == 2:# and CARD_COUNT > 1:
        CARD_COUNT = CARD_COUNT - 1
    if num == 3:
        global EXIT
        EXIT = True
    init_cards(CARDS[0], CARDS[len(CARDS)-1], HORIZ_LINE, CARD_COUNT)
    #if num == 2:
    #    print("HAS BEEN CLICKED")
    #global BUTTON_2_CLICKED
    #BUTTON_2_CLICKED = True
    


milliseconds_start = int(round(time.time() * 1000))
milliseconds = int(round(time.time() * 1000))
btn1 = tk.Button(root, text = "Add Card", command = lambda:on_click(1))
init_cards(CARDS[0], CARDS[len(CARDS)-1], HORIZ_LINE, CARD_COUNT)
btn2 = tk.Button(root, text = "Remove Card", command = lambda:on_click(2))
btn3 = tk.Button(root, text = "Exit", command = lambda:on_click(3))
btn1.pack()
btn2.pack()
btn3.pack()
canvas.pack()
panel.pack()

#while milliseconds < milliseconds_start + 15000:
while not EXIT:
    canvas.update()
count = 0
    
    
    
    
    
'''
#root = tk.Tk()

#img = ImageTk.PhotoImage(Image.open(path))
#panel = tk.Label(root, image=img)
#panel.pack(side="bottom", fill="both", expand="yes")

def test(e):
    #img2 = ImageTk.PhotoImage(Image.open("/Users/Maria/Desktop/Exploding Kittens/Card Images/ExplodingKitten.png"))
    #panel.configure(image=img2)
    #panel.image = img2
    img2 = Image.open("/Users/Maria/Desktop/Exploding Kittens/Card Images/ExplodingKitten.png")


#root.bind("<Return>", test)
img2 = Image.open("/Users/Maria/Desktop/Exploding Kittens/Card Images/ExplodingKitten.png")
img2.pack()
root.mainloop()
'''

'''while(milliseconds < milliseconds_start + 15000):
    #print(BUTTON_2_CLICKED)
    time.sleep(0.01)
    #print(BUTTON_2_CLICKED)
    
    count = count + 1
    if BUTTON_2_CLICKED:
        print("jksdlf")
        exit()
    milliseconds = int(round(time.time() * 1000))
    
    root.update_idletasks()
    
    root.update()'''
    

'''root = tk.Tk()


def callback(event):
    print("clicked at", event.x, event.y)

canvas= tk.Canvas(root, width=100, height=100)
canvas.bind("<Button-1>", callback)
canvas.pack()

root.mainloop()'''