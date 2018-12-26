from bottle import (Bottle, get, post, put, redirect, request, response, route, template, jinja2_view, static_file)
import backend.utils as utils
import backend.db as db
import json
app = Bottle()

@app.get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./frontend/dist")

@app.get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./frontend/css")

@app.get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./frontend/images")

@app.get('/favicon.ico')
def get_favicon():
    return static_file('favicon.ico', root='./')

@app.get("/sounds/<filepath:re:.*\.mp3>")
def mp3(filepath):
    return static_file(filepath, root="./frontend/sounds")

@app.get('/games/<game_id>')
@jinja2_view('./backend/pages/game.html')
def play(game_id):
    currentPlayer = request.get_cookie("player")
    currentGame = db.getGame(game_id)
    if not currentPlayer or not currentGame:
        redirect("/start")
        return
    gamePlayers = db.getGamePlayers(game_id)
    return {"version" : utils.getVersion(), "game":currentGame, "players":gamePlayers}

@app.get('/games/<game_id>/status')
def status(game_id):
    currentPlayerName = request.get_cookie("player")
    currentPlayer = {"name":currentPlayerName}
    currentGame = db.getGame(game_id)
    currentGame["sequence"] = currentGame["sequence"].split(",")
    gamePlayers = db.getGamePlayers(game_id)
    currentPlayer["status"] = "viewer"
    failedPlayers = 0
    for p in gamePlayers:
        if p["status"] == "failed":
            failedPlayers = failedPlayers + 1
        if p["player"] == currentPlayerName:
            currentPlayer["status"] = p["status"]
    if failedPlayers and failedPlayers == len(gamePlayers):
        currentGame["status"] = "over"
    response.content_type = 'application/json'
    return json.dumps({"game":currentGame,"players":gamePlayers, "user":currentPlayer}, default=utils.json_serial)

@app.post('/games/<game_id>/players')
def join(game_id):
    currentGame = db.getGame(game_id)
    result = "failed"
    if currentGame['status'] == "open":
        playerName = request.get_cookie("player")
        db.joinGame(game_id, playerName)
        result = "success"
    response.content_type = 'application/json'
    return json.dumps({"result":result}, default=utils.json_serial)

@app.put('/games/<game_id>/players')
def ready(game_id):
    currentGame = db.getGame(game_id)
    result = "failed"
    if currentGame:
        playerName = request.get_cookie("player")
        db.playerReady(game_id, playerName)
        result = "success"
    response.content_type = 'application/json'
    return json.dumps({"result":result}, default=utils.json_serial)

def playTurn(game, color):
    sequence = game["sequence"].split(",")
    step = game["step"]
    print(str(step) + " ---- " + str(sequence[step]))
    return color == sequence[step]


@app.post('/games/<game_id>/play')
def playerTurn(game_id):
    currentGame = db.getGame(game_id)
    result = "failed"
    if currentGame:
        playerName = request.get_cookie("player")
        postdata = json.load(request.body)
        color = postdata["color"]
        correct = playTurn(currentGame, color)
        if correct:
            print("yoyoyoyoy")
            newStep = currentGame["step"] + 1
            if newStep == utils.GAME_LENGTH:
                db.win(game_id)
            else:
                print("sssssss")
                db.correctTurn(game_id, playerName, newStep)
        else:
            print("3333333")
            db.wrongTurn(game_id, playerName)
        result = "success"
    response.content_type = 'application/json'
    return json.dumps({"result":result}, default=utils.json_serial)

@app.post('/players')
def newPlayer():
    playerName = request.forms.get("name")
    db.createPlayer(playerName)
    response.set_cookie("player", playerName, None, max_age=3600000, path='/')
    redirect("/games")


@app.post('/games')
def create():
    db.createGame(request.forms.get("name"), request.get_cookie("player"))
    redirect("/games")

@app.get('/games')
@jinja2_view('./backend/pages/games.html')
def games():
    currentPlayer = request.get_cookie("player")
    if not currentPlayer:
        redirect("/start")
        return
    return {"version" : utils.getVersion(), "games": db.getAvailableGames()}


@app.get('/start')
@jinja2_view('./backend/pages/start.html')
def start():
    currentPlayer = request.get_cookie("player")
    if currentPlayer:
        redirect("/games")
        return
    return {"version" : utils.getVersion()}

@app.get('/test/<game_id>')
def test(game_id):
    db.correctTurn(game_id, "imc", 0)
    return {"version" : utils.getVersion()}

@app.get('/game/<game_id>')
@jinja2_view('./backend/pages/game.html')
def game(game_id):
    return {"version" : utils.getVersion()}

@app.get('/')
@jinja2_view('./backend/pages/index.html')
def landing():
    return {"version" : utils.getVersion()}