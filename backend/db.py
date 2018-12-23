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
            sql = "SELECT * FROM game where status = 0"
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



def createGame(name):
    sequence = utils.generateSequence()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO game (name, sequence) VALUES ('{}', '{}')".format(name, sequence) 
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
            connection.commit()
            gamePlayers = cursor.execute("SELECT * FROM playergame WHERE game = '{}'".format(game_id))
            readyPlayers = cursor.execute("SELECT * FROM playergame WHERE game = '{}' AND status = 'ready'".format(game_id))
            if gamePlayers == readyPlayers:
                sql = "UPDATE game SET status = 'on' WHERE id = '{}' ".format(game_id)
                cursor.execute(sql)
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