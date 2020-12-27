'''
Created on Dec 20, 2020

@author: Maria
'''

from tkinter import *
import datetime
import time
import NewCardGenerator
from PIL import ImageTk, Image
from Player import Player
import cv2

class CardDisplay:
    
    def __init__(self, name, root, canvas, left_bound, top_bound, height):
        self.card_images = {"diffuse": "/Users/Maria/Desktop/Exploding Kittens/Card Images/Diffuse.png",
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
               "exploding kitten": "/Users/Maria/Desktop/Exploding Kittens/Card Images/ExplodingKitten.png",
               "highlight diffuse": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedDiffuse.png",
               "highlight nope": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedNope.png",
               "highlight attack": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedAttack.png",
               "highlight favor": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedFavor.png",
               "highlight see the future": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedSeeTheFuture.png",
               "highlight skip": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedSkip.png",
               "highlight shuffle": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedShuffle.png",
               "highlight cattermelon": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedCattermelon.png",
               "highlight beard cat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedBeardCat.png",
               "highlight rainbow-ralphing cat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedRainbowCat.png",
               "highlight tacocat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedTacocat.png",
               "highlight exploding kitten": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedExplodingKitten.png",
               "highlight hairy potato cat": "/Users/Maria/Desktop/Exploding Kittens/Card Images/HighlightedHairyPotatoCat.png"}
        self.default_width = 80
        image = self.card_images[name]
        open_image = Image.open(image).resize((self.default_width, height), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(open_image)
        temp = canvas.create_image(left_bound, top_bound, anchor = NW, image = self.photo)
        self.height = height
        self.left_bound = left_bound
        self.top_bound = top_bound
        self.canvas = canvas
        '''open_card = Image.open(self.card_images[name]).resize((80, 120), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(open_card)
        self.button = Button(root, image = photo)
        self.button.place(relx=left_bound, rely=380/500, anchor='center')'''
        #self.root = root
    
    def action(self):
        pass
    
    def pack(self):
        pass
    '''def highlight(self, player: Player, index):
        image = self.card_highlight[player.hand[index]]
        open_image = Image.open(image).resize((self.default_width, self.height), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(open_image)
        temp = self.canvas.create_image(self.left_bound, self.top_bound, anchor = NW, image = self.photo)'''