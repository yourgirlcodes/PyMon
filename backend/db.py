import pymysql
import backend.utils as utils
###### https://www.db4free.net/phpMyAdmin/index.php

# Connect to the database
connection = pymysql.connect(host='db4free.net',
                             user='slideshowbuilder',
                             password='slideshowbuilder',
                             db='slideshowbuilder',
                             charset='utf8',
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)

def getAvailableGames():
    games = []
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM game"
            cursor.execute(sql)
            games = cursor.fetchall()
    except:
        pass
    return games

def getGame(game_id):
    game = {}
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM game where id = {}".format(game_id)
            cursor.execute(sql)
            game = cursor.fetchone()
    except Exception, e:
        print(repr(e))
        pass
    return game

def getGamePlayers(game_id):
    players = []
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM playergame where game = {} ORDER BY created".format(game_id)
            cursor.execute(sql)
            players = cursor.fetchall()
    except Exception, e:
        print(repr(e))
        pass
    return players



def createGame(name, creator):
    sequence = utils.generateSequence()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO game (name, sequence, creator) VALUES ('{}', '{}', '{}')".format(name, sequence, creator) 
            cursor.execute(sql)
            connection.commit()
    except Exception, e:
        print(repr(e))


def joinGame(game_id, player_id):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO playergame (game, player) VALUES ('{}', '{}')".format(game_id, player_id) 
            cursor.execute(sql)
            connection.commit()
    except Exception, e:
        print(repr(e))
        return False
    return True

def playerReady(game_id, player_id):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE playergame SET status = 'ready' WHERE game = '{}' AND player='{}'".format(game_id, player_id) 
            cursor.execute(sql)
            gamePlayers = cursor.execute("SELECT * FROM playergame WHERE game = '{}'".format(game_id))
            readyPlayers = cursor.execute("SELECT * FROM playergame WHERE game = '{}' AND status = 'ready'".format(game_id))
            if gamePlayers == readyPlayers:
                sql = "UPDATE game SET status = 'on' WHERE id = '{}' ".format(game_id)
                cursor.execute(sql)
                sql = "UPDATE playergame SET status = 'turn' WHERE game = '{}' ORDER BY created DESC LIMIT 1".format(game_id)
                cursor.execute(sql)
            connection.commit()
    except Exception, e:
        print(repr(e))
        return False
    return True

def correctTurn(game_id, playerName, newStep):
    try:
        with connection.cursor() as cursor:
            print("here1")
            sql = "UPDATE game SET step = '{}' WHERE id = '{}'".format(newStep, game_id) 
            cursor.execute(sql)
            print("here2")
            nextPlayerQuery = cursor.execute("SELECT player FROM playergame WHERE game = {} AND status <> 'failed' AND created < (SELECT created FROM playergame WHERE status='turn' AND game = {}) LIMIT 1".format(game_id,game_id))
            if not nextPlayerQuery:
                nextPlayerQuery = cursor.execute("SELECT player FROM playergame WHERE game = '{}' AND status <> 'failed' ORDER BY created DESC LIMIT 1".format(game_id))
            nextPlayerName = cursor.fetchone()["player"]
            print(str(nextPlayerName))
            updates = cursor.execute("UPDATE playergame SET status = (case when status= 'turn' then 'ready' when player = '{}' then 'turn' else 'ready' end) WHERE game = '{}' AND status <> 'failed'".format(nextPlayerName, game_id))
            connection.commit()
    except Exception, e:
        print(repr(e))
        return False
    return True

def wrongTurn(game_id, playerName):
    try:
        with connection.cursor() as cursor:
            nextPlayerQuery = cursor.execute("SELECT player FROM playergame WHERE game = {} AND status <> 'failed' AND created < (SELECT created FROM playergame WHERE status='turn' AND game = {}) LIMIT 1".format(game_id,game_id))
            if not nextPlayerQuery:
                nextPlayerQuery = cursor.execute("SELECT player FROM playergame WHERE game = '{}' AND status <> 'failed' ORDER BY created DESC LIMIT 1".format(game_id))
            nextPlayerName = cursor.fetchone()["player"]
            print(str(nextPlayerName))
            updates = cursor.execute("UPDATE playergame SET status = (case when status = 'turn' then 'failed' when player = '{}' then 'turn' else 'ready' end) WHERE game = '{}' AND status <> 'failed'".format(nextPlayerName, game_id))
            connection.commit()
    except Exception, e:
        print(repr(e))
        return False
    return True

def win(game_id):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE game SET status = 'won' WHERE id = '{}'".format(game_id) 
            cursor.execute(sql)
            updates = cursor.execute("UPDATE playergame SET status = 'won'  WHERE game = '{}' AND status <> 'failed'".format( game_id))
            connection.commit()
    except Exception, e:
        print(repr(e))
        return False
    return True



def createPlayer(player_name):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO player (id) VALUES ('{}')".format(player_name) 
            cursor.execute(sql)
            connection.commit()
    except Exception, e:
        print(repr(e))
        return False
    return True