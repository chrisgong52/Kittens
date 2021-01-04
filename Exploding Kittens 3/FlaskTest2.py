'''
Created on Dec 28, 2020

@author: Maria
'''

from flask import Flask, render_template, request, redirect, jsonify, make_response
import tkinter
from tkinter import *
import webbrowser
from Player2 import Player

app = Flask(__name__)

root_global = tkinter.Tk()
canvas_global = Canvas(root_global, width=1000, height=500)
l = [1,2,3,4,5,6,7,8]
p1 = Player()
p1.hand.append("attack")
p1.hand.append("cattermelon")
p1.hand.append("see the future")
p1.hand.append("diffuse")
p1.hand.append("tacocat")
p1.hand.append("skip")
p1.hand.append("exploding kitten")

p2 = Player()
p2.hand.append("nope")
p2.hand.append("shuffle")
p2.hand.append("favor")
p2.hand.append("rainbow-ralphing cat")
p2.hand.append("beard cat")

players = [p1, p2]
hand_sizes = []
for item in players:
    print(len(item.hand))
    hand_sizes.append(len(item.hand))
images = {"diffuse": "static/Diffuse.png",
          "nope": "static/Nope.png",
          "attack": "static/Attack.png",
          "favor": "static/Favor.png",
          "see the future": "static/SeeTheFuture.png",
          "skip": "static/Skip.png",
          "shuffle": "static/Shuffle.png",
          "cattermelon": "static/Cattermelon.png",
          "beard cat": "static/BeardCat.png",
          "rainbow-ralphing cat": "static/RainbowCat.png",
          "tacocat": "static/Tacocat.png",
          "hairy potato cat": "static/HairyPotatoCat.png",
          "exploding kitten": "static/ExplodingKitten.png",
          "highlight diffuse": "static/HighlightedDiffuse.png",
          "highlight nope": "static/HighlightedNope.png",
          "highlight attack": "static/HighlightedAttack.png",
          "highlight favor": "static/HighlightedFavor.png",
          "highlight see the future": "static/HighlightedSeeTheFuture.png",
          "highlight skip": "static/HighlightedSkip.png",
          "highlight shuffle": "static/HighlightedShuffle.png",
          "highlight cattermelon": "static/HighlightedCattermelon.png",
          "highlight beard cat": "static/HighlightedBeardCat.png",
          "highlight rainbow-ralphing cat": "static/HighlightedRainbowCat.png",
          "highlight tacocat": "static/HighlightedTacocat.png",
          "highlight exploding kitten": "static/HighlightedExplodingKitten.png",
          "highlight hairy potato cat": "static/HighlightedHairyPotatoCat.png",
          "card_back": "static/CardBack.png"}

button_functions = {"diffuse": "diffuse_pressed(this.id);",
          "nope": "nope_pressed(this.id);",
          "attack": "attack_pressed(this.id);",
          "favor": "favor_pressed(this.id);",
          "see the future": "see_the_future_pressed(this.id);",
          "skip": "skip_pressed(this.id);",
          "shuffle": "shuffle_pressed(this.id);",
          "cattermelon": "cattermelon_pressed(this.id);",
          "beard cat": "beard_cat_pressed(this.id);",
          "rainbow-ralphing cat": "rainbow_ralphing_cat_pressed(this.id);",
          "tacocat": "tacocat_pressed(this.id);",
          "hairy potato cat": "hairy_potato_cat_pressed(this.id);",
          "exploding kitten": "exploding_kitten_pressed(this.id);",
          "highlight diffuse": "highlight_diffuse_pressed(this.id);",
          "highlight nope": "highlight_nope_pressed(this.id);",
          "highlight attack": "highlight_attack_pressed(this.id);",
          "highlight favor": "highlight_favor_pressed(this.id);",
          "highlight see the future": "highlight_see_the_future_pressed(this.id);",
          "highlight skip": "highlight_skip_pressed(this.id);",
          "highlight shuffle": "highlight_shuffle_pressed(this.id);",
          "highlight cattermelon": "highlight_cattermelon_pressed(this.id);",
          "highlight beard cat": "highlight_beard_cat_pressed(this.id);",
          "highlight rainbow-ralphing cat": "highlight_rainbow_ralphing_cat_pressed(this.id);",
          "highlight tacocat": "highlight_tacocat_pressed(this.id);",
          "highlight exploding kitten": "highlight_exploding_kitten_pressed(this.id);",
          "highlight hairy potato cat": "highlight_hairy_potato_cat_pressed(this.id);"}



@app.route("/")
@app.route("/home")
def hello_world():
    #webbrowser.open(url='http:127.0.0.1:5000', new=2)
    return "<p>Hello, World!</p>"

@app.route("/about")
def about_page():
    return render_template('page.html')

@app.route("/list", methods = ["GET", "POST"])
def list_display():
    if request.method == "POST":
        print("sdljkf")
        req = request.get_json()
        print("received")
        print(req)
        res = make_response(jsonify({"message": "JSON received"}), 200)
        
        ### jsonify TRANSLATES PYTHON STUFF TO JSON OBJECT
        
        return res
    return render_template('list_display2.html', players = players, images = images, lens = hand_sizes, button_functions = button_functions)

#@app.route("/list/test", methods = ["GET", "POST"])
#def create_button():
    

if __name__ == "__main__":
    app.run(debug = True)
    
