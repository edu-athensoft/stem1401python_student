"""
module: over

closeLevel() - close a game level

gameover() - close the game and exit, finalizing

"""


def closeLevel(levelid,gamedata):
    """
    close a game level and release all the resources and save game data
    :return:
    """
    print(f"closeLevel of {levelid}")
    closeMap(levelid)
    closeImage(levelid)
    closeSound(levelid)

    saveData(gamedata)


def closeMap(levelid):
    """
    close the specified map
    :param level_id:
    :return:
    """
    print(f"\tcloseMap({levelid})")


def closeImage(levelid):
    """
    close the image of the game level
    :param level_id:
    :return:
    """
    print(f"\tcloseImage({levelid})")


def closeSound(levelid):
    """
    close the sound of the game level
    :param level_id:
    :return:
    """
    print(f"\tcloseSound({levelid})")


def saveData(gamedata):
    """
    save the game data when getting through the game level
    :param gamedata:
    :return:
    """
    print(f"\tsaveData({gamedata})")


def saveAcctInfo(acctInfo):
    print(f"\tsaveAcctInfo({acctInfo})")


def gameover(bgImage, bgMusic, acctInfo):
    """
    to finalize the game program, and release all related resources and save account Info
    the background image
    the background music
    the acct. info.
    :return:
    """
    print("The game is closing...")
    closeImage(bgImage)
    closeSound(bgMusic)
    saveAcctInfo(acctInfo)



# write a unit test for closeLevel()
# LEVEL_ID = '1-2'
# GAME_DATA = 'updated game data string'
# closeLevel(LEVEL_ID, GAME_DATA)

# bgImage = 'bg-image.jpg'
# bgMusic = 'bg-music.mp3'
# acctInfo = 'account info of player'
# gameover(bgImage,bgMusic,acctInfo)