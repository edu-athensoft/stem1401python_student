"""
load game (main program)

load data (game data, account info, map, level info)
load resources  (image, sound/music)

loadMap()
loadImage()
loadSound()
loadData()

loadLevel()

coupled
loosely coupled
tightly coupled

"""

import py201221a_python2_chen.day01_201221.game_v1_2.image.open as imgOpen
import py201221a_python2_chen.day01_201221.game_v1_2.image.change as imgDisplay

import py201221a_python2_chen.day01_201221.game_v1_2.sound.load as sndLoad
import py201221a_python2_chen.day01_201221.game_v1_2.sound.play as sndPlay


def loadMap(mapid):
    print(f"Map {mapid} is loaded.")


def loadImage(imgid):
    print(f"Image {imgid} is loaded.")
    imgOpen.open_img(imgid)
    imgDisplay.display_img(imgid)


def loadSound(sndid):
    print(f"Sound {sndid} is loaded.")
    sndLoad.load_snd(sndid)
    sndPlay.play_snd(sndid)


def loadData(dataid):
    print(f"Game data {dataid} is loaded.")


def loadLevel(levelid):
    mapid = 'map-'+levelid
    imgid = 'img-'+levelid
    sndid = 'snd-'+levelid
    dataid = 'data-'+levelid

    print(f"\nLoading Level of {levelid}...")
    loadMap(mapid)
    loadImage(imgid)
    loadSound(sndid)
    loadData(dataid)
    print(f"Level {levelid} is loaded.\n")



# test main program
# levelid = '1-2'
# loadLevel(levelid)