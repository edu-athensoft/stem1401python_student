"""
module load

to load a game level (by levelid)
    load game map for that level
    load images for that level
    load sounds for that level
    load game data of the player

facade



"""


def loadLevel(levelid, gamedata):
    print(f"loadLevel of {levelid}")
    loadMap(levelid)
    loadImage(levelid)
    loadSound(levelid)
    loadData(gamedata)


def loadMap(levelid):
    print(f"\tloadMap({levelid})")


def loadImage(levelid):
    print(f"\tloadImage({levelid})")


def loadSound(levelid):
    print(f"\tloadSound({levelid})")


def loadData(gamedata):
    print(f"\tloadData({gamedata})")



# write test code here before you integrate it into main module
# LEVEL_ID = '1-2'
# GAME_DATA = 'game data string'
# loadLevel(LEVEL_ID, GAME_DATA)

