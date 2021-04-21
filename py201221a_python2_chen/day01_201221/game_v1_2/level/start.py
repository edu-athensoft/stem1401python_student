"""
start the game, the entrance of the game

init() - initializing
loadImage() - load background image
loadSound() - load background music
loadAcctInfo() - load user's account information

start()
    user selects a level
    sys loads level data and all resources (import load)
    user plays game
    user select exit or continue
        if continue, then repeat
        else exit
"""

import py201221a_python2_chen.day01_201221.game_v1_2.level.load as gmlvLoad
import py201221a_python2_chen.day01_201221.game_v1_2.level.over as gmlvOver

import py201221a_python2_chen.day01_201221.game_v1_2.image.open as imgOpen
import py201221a_python2_chen.day01_201221.game_v1_2.image.change as imgDisplay

import py201221a_python2_chen.day01_201221.game_v1_2.sound.load as sndLoad
import py201221a_python2_chen.day01_201221.game_v1_2.sound.play as sndPlay


import time

def init():
    print("Starting...")


def loadImage(image_name):
    print(f"load bg image {image_name}")
    imgOpen.open_img(image_name)
    imgDisplay.display_img(image_name)


def loadSound(sound_name):
    print(f"load bg music {sound_name}")
    sndLoad.load_snd(sound_name)
    sndPlay.play_snd(sound_name)

def loadAcctInfo(account_info):
    print(f"load account info {account_info}")


def start():
    """

    :return:
    """

    while True:
        # levelid = '1-1'
        print("\nPlease choose a level:", end="")
        levelid = input()

        # load level data and resources
        gmlvLoad.loadLevel(levelid, )

        # user starts to play game
        print(f"user starts to play")
        for i in range(3):
            print(i+1)
            time.sleep(1)
        print(f"user stops playing\n")

        # 1. closeLevel
        gmlvOver.closeLevel(levelid,account_info)

        # exit ?
        print("\nDo you want to continue? [y|n]")
        # if user press 'y', then continue
        # else exit
        tocontinue = input()
        # if toexit == 'y':
        #     continue
        # else:
        #     break
        if tocontinue != 'y':
            break


# main program
print("=====================")
print("=== My Funny Game ===")
print("===    Ver 1.0    ===")
print("=====================")
print("\n\n")


init()

bgImg = "bg-img.jpg"
loadImage(bgImg)

bgMusic = "bg-music.mp3"
loadSound(bgMusic)

account_info = "acct-info"
loadAcctInfo(account_info)

print("\nGame started.")

start()

gmlvOver.gameover(bgImg,bgMusic,account_info)
# gmlvOver.gameover()


# 3. test