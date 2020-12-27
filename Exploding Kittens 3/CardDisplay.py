'''
Created on Dec 20, 2020

@author: Maria
'''

from tkinter import *
import datetime
import time
import NewCardGenerator
from PIL import ImageTk, Image
import cv2

class CardDisplay:
    def __init__(self, name, root, canvas, left_bound, top_bound, width, height):
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
               "exploding kitten": "/Users/Maria/Desktop/Exploding Kittens/Card Images/ExplodingKitten.png"}
        image = self.card_images[name]
        open_image = Image.open(image).resize((width, height), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(open_image)
        temp = canvas.create_image(left_bound, top_bound, anchor = NW, image = self.photo)
        #Button(root, image = self.photo).pack(side=BOTTOM)
        #self.root = root
        
    def pack(self):
        pass