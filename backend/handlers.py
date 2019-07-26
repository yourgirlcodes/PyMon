from bottle import (Bottle, get, post, put, redirect, request, response, jinja2_view)
import json
from backend import utils
from backend import controller
from backend import page_handlers

app = Bottle()

@app.get('/games/<game_id>/status')
def status(game_id):
    currentPlayerName = request.get_cookie("player")
    gameStatus = controller.generateGameStatus(game_id, currentPlayerName)
    return utils.jsonResponse(response, gameStatus)

@app.post('/games/<game_id>/players')
def joinGameHandler(game_id):
    playerName = request.get_cookie("player")
    result = controller.joinGame(game_id, playerName)
    return utils.jsonResponse(response, {"result":result})

@app.put('/games/<game_id>/players')
def playerReadyHandler(game_id):
    playerName = request.get_cookie("player")
    result = controller.markPlayerReady(game_id, playerName)
    return utils.jsonResponse(response, {"result":result})

@app.post('/games/<game_id>/turn')
def turnHandler(game_id):
    playerName = request.get_cookie("player")
    color = utils.reqBody(request.body, "color")
    result = controller.playTurn(game_id, playerName, color)
    return utils.jsonResponse(response, {"result":result})

@app.post('/players')
def newPlayerHandler():
    playerName = request.forms.get("name")
    avatar = request.forms.get("avatar")
    controller.createPlayer(playerName, avatar)
    response.set_cookie("player", playerName, None, max_age=3600000, path='/')
    redirect("/games")

@app.post('/games')
def create():
    controller.createGame(request.forms.get("name"), request.get_cookie("player"))
    redirect("/games")

@app.error(404)
@jinja2_view('./backend/pages/404.html')
def error404(error):
    return {"version" : utils.getVersion()}

@app.get('/winners')
def create():
    page_handlers.winners