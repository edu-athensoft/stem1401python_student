"""
over, terminate the game

release resources
pause sounds
close images
save game data, status


saveData()
closeMap()
closeImage()
closeSound()
saveAccountInfo()

"""

import py201221a_python2_chen.day01_201221.game_v1_2.image.close as imgClose

import py201221a_python2_chen.day01_201221.game_v1_2.sound.pause as sndPause

def saveData(dataid):
    print(f"Game data {dataid} is saved.")


def closeMap(mapid):
    print(f"Map {mapid} is closed.")


def closeImage(imgid):
    print(f"Image {imgid} is closed.")
    imgClose.close_img(imgid)


def closeSound(sndid):
    print(f"Sound {sndid} is closed.")
    sndPause.pause_snd(sndid)

def saveAccountInfo(account_info):
    print(f"Account info {account_info} saved.")


def closeLevel(levelid, accountInfo):
    mapid = 'map-' + levelid
    imgid = 'img-' + levelid
    sndid = 'snd-' + levelid
    dataid = 'data-' + levelid

    saveData(dataid)
    closeMap(mapid)
    closeImage(imgid)
    closeSound(sndid)
    saveAccountInfo(accountInfo)


def gameover(bgImage, bgMusic, accountInfo):
# def gameover():
    # 2. finalize game
    # 2.1 close bgImage
    # 2.2 close bgMusic
    # 2.3 save AccountInfo
    # bgImage = "bg-img.jpg"
    # bgMusic = "bg-music.mp3"
    # accountInfo = "acct-info"
    closeImage(bgImage)
    closeSound(bgMusic)
    saveAccountInfo(accountInfo)

    print(f"Game Over.")


# test main program
# levelid = '1-2'
# accountInfo = "acct-info"
# closeLevel(levelid, accountInfo)

