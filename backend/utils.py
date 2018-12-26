from datetime import date, datetime

def getVersion():
    return "0.0.1"

GAME_LENGTH = 3

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def generateSequence():
    import random
    colors = ["red", "blue", "green", "yellow"]
    return ''.join(colors[random.randint(0,len(colors) - 1)] + "," for _ in range(GAME_LENGTH))[:-1]
