import os
from bottle import (get, post, put, redirect, request, response, route, run,
                    template, jinja2_view)
import backend.utils as utils
import backend.db as db
import json

from bottle import static_file, get, Bottle


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./frontend/dist")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./frontend/css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@get('/favicon.ico')
def get_favicon():
    return static_file('favicon.ico', root='../')

@get("/sounds/<filepath:re:.*\.mp3>")
def mp3(filepath):
    return static_file(filepath, root="./frontend/sounds")


@get('/editor')
@jinja2_view('./pages/editor.html')
def editor():
    return {"version" : utils.getVersion()}

@get('/games/<game_id>')
@jinja2_view('./backend/pages/game.html')
def play(game_id):
    currentPlayer = request.get_cookie("player")
    if not currentPlayer:
        redirect("/start")
        return
    currentGame = db.getGame(game_id)
    gamePlayers = db.getGamePlayers(game_id)
    return {"version" : utils.getVersion(), "game":currentGame, "players":gamePlayers}

@get('/game_status/<game_id>')
def status(game_id):
    currentPlayer = request.get_cookie("player")
    currentGame = db.getGame(game_id)
    gamePlayers = db.getGamePlayers(game_id)
    response.content_type = 'application/json'
    return json.dumps({"game":currentGame,"players":gamePlayers, "user":currentPlayer}, default=utils.json_serial)

@post('/games/<game_id>/players')
def join(game_id):
    currentGame = db.getGame(game_id)
    result = "failed"
    if currentGame['status'] == "open":
        playerName = request.get_cookie("player")
        db.joinGame(game_id, playerName)
        result = "success"
    response.content_type = 'application/json'
    return json.dumps({"result":result}, default=utils.json_serial)

@put('/games/<game_id>/players')
def ready(game_id):
    currentGame = db.getGame(game_id)
    result = "failed"
    if currentGame:
        playerName = request.get_cookie("player")
        db.playerReady(game_id, playerName)
        result = "success"
    response.content_type = 'application/json'
    return json.dumps({"result":result}, default=utils.json_serial)

@post('/players')
def newPlayer():
    playerName = request.forms.get("name")
    db.createPlayer(playerName)
    response.set_cookie("player", playerName, None, max_age=3600000, path='/')
    redirect("/games")


@post('/games')
def create():
    db.createGame(request.forms.get("name"))
    redirect("/games")

@get('/games')
@jinja2_view('./pages/games.html')
def games():
    currentPlayer = request.get_cookie("player")
    if not currentPlayer:
        redirect("/start")
        return
    return {"version" : utils.getVersion(), "games": db.getAvailableGames()}


@get('/start')
@jinja2_view('./pages/start.html')
def start():
    return {"version" : utils.getVersion()}

@get('/game/<game_id>')
@jinja2_view('./backend/pages/game.html')
def game(game_id):
    return {"version" : utils.getVersion()}

@get('/')
@jinja2_view('./pages/index.html')
def landing():
    return {"version" : utils.getVersion()}

run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
