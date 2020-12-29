'''
Created on Dec 28, 2020

@author: Maria
'''

from flask import Flask
import tkinter
import webbrowser

app = Flask(__name__)


@app.route("/")
def hello_world():
    #webbrowser.open(url='http:127.0.0.1:5000', new=2)
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug = True)

