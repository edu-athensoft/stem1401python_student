"""
load game (main program)

load data (game data, account info, map, level info)
load resources  (image, sound/music)

loadLevel()
    loadMap()
    loadImage()
    loadSound()
    loadData()
"""

def loadMap(mapid):
    print(f"map of {mapid} has been loaded.")


def loadImage(img_name):
    print(f"load bg Image ({img_name})")


def loadMusic(snd_name):
    print(f"load bg Music ({snd_name})")


def loadData(game_data):
    print(f"load game data ({game_data})")


def loadLevel(levelid):
    level_map = "map-"+levelid
    level_img = "img"+levelid
    level_music = "music"+levelid
    level_data = "data"+levelid

    loadMap(level_map)
    loadImage(level_img)
    loadMusic(level_music)
    loadData(level_data)


# main program for test
# levelid = "level:1-1"
# loadLevel(levelid)

