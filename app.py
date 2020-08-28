from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route('/')
def defaultRoute():
    return 'Server is up'

@app.route('/index')
def index():
    # This function is called when you register your Battlesnake on play.battlesnake.com
    # It controls your Battlesnake appearance and author permissions.
    # TIP: If you open your Battlesnake URL in browser you should see this data
    return {
        "apiversion": "1",
        "author": "Team Snaking Nooglers",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Personalize
        "head": "default",  # TODO: Personalize
        "tail": "default",  # TODO: Personalize
    }

@app.route('/start')
def start():
    # This function is called everytime your snake is entered into a game.
    # cherrypy.request.json contains information about the game that's about to be played.
    # TODO: Use this function to decide how your snake is going to look on the board.
    print("START")
    return "ok"

@app.route('/move')
def move():
    # This function is called on every turn of a game. It's how your snake decides where to move.
    # Valid moves are "up", "down", "left", or "right".
    # TODO: Use the information in cherrypy.request.json to decide your next move.
    # Choose a random direction to move in
    possible_moves = ["up", "down", "left", "right"]
    move = random.choice(possible_moves)

    print(f"MOVE: {move}")
    return {"move": move}

@app.route('/end')
def end():
    # This function is called when a game your snake was in ends.
    # It's purely for informational purposes, you don't have to make any decisions here.
    print("END")
    return "ok"
