'''
Created on Dec 28, 2020

@author: Maria
'''

from flask import Flask, render_template
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



@app.route("/")
@app.route("/home")
def hello_world():
    #webbrowser.open(url='http:127.0.0.1:5000', new=2)
    return "<p>Hello, World!</p>"

@app.route("/about")
def about_page():
    return render_template('page.html')

@app.route("/list")
def list_display():
    return render_template('list_display.html', player = p1, images = images, len = len(p1.hand))

if __name__ == "__main__":
    app.run(debug = True)
    
    
"""

Test HTML code

/*div
        {
            background-color: green;
            width: 200px;
            height: 200px;
            color: white;
            margin-top: 50px;
        }
        .Attack_card{
            background-color: white;
            width: 120px;
            height: 200px;
            margin-top: 400px;
            margin-left: 800px;
            position: relative;
            z-index: 11;
        }
        .Diffuse_card{
            background-color: white;
            width: 120px;
            height: 200px;
            margin-left: -170px;
            z-index: 100;
        }
        .See_the_future_card{
            background-color: white;
            width: 120px;
            height: 200px;
            margin-left: -225px;
            z-index: -1;
        }*/
        /*.wrapper{
            display grid;
            grid-template-columns: 70% 30%;
        }*/
    <! </style>
    
    
    
    <div class="grid-item"><img class="Diffuse_card" src="static/Diffuse.png" alt="test"></div>
    <div class="grid-item"><img class="Attack_card" src="static/Attack.png" alt="test"></div>
    <div class="grid-item"><img class="See_the_future_card" src="static/SeeTheFuture.png" alt="test"></div>  
    <div class="grid-item"><img class="Cattermelon" src="static/Cattermelon.png" alt="test"></div>
    
    
    <! --
    <div class="grid-item">5</div>
      <div class="grid-item">6</div>  
      <div class="grid-item">7</div>
    <div class="grid-item">8</div>
    <div class="grid-item">9</div>  
    -->
    
    
    
    <! <img class="Attack_card" src="static/Attack.png" alt="test">
    <! <img class="Diffuse_card" src="static/Diffuse.png" alt="test">
    <! <img class="See_the_future_card" src="static/SeeTheFuture.png" alt="test">
    <! <div class="wrapper">
    <!     <img class="Attack_card" src="static/Attack.png" alt="test">
    <!     <img class="Diffuse_card" src="static/Diffuse.png" alt="test">
    <! </div>
    
    <div class="item-1"><img src="static/Attack.png"/></div>
        <div class="item-2"><img src="static/Diffuse.png"/></div>
        <div class="item-3"><img src="static/SeeTheFuture.png"/></div>
    
    <div class="photo"><img src="static/Attack.png" /> </div>

<h1> list display </h1>
{% for item in temp %}
    <h1>{{ item }}</h1>
{% endfor %}

    <! -- <img src="static/Diffuse.png"><! -- alt= width="100" height="200" /


<input type="image" id="test" src="static/Diffuse.png" "alt= width="100" height="200">

    <! -- <img src=" {{ url_for('static', filename = "Diffuse.png", width=100, height = 200, mode='crop') }}" />
"""