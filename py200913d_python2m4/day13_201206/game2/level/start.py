"""
start the game, the entrance of the game
init()
loadImage()
loadMusic()
loadAccountInfo()
start()
"""

import py200913d_python2m4.day13_201206.game2.level.load as gmlevel_load

import time

def init():
    print("init()")


def loadImage(img_name):
    print(f"load bg Image ({img_name})")


def loadMusic(snd_name):
    print(f"load bg Music ({snd_name})")


def loadAccountInfo(acct_info):
    print(f"load account info ({acct_info})")


def start():
    print(f"game started.\n\n")

    while True:
        # test load only one level
        print("\nselect level:",end="")
        # levelid = "level:1-1"
        levelid = input()

        gmlevel_load.loadLevel(levelid)

        # user starts playing game
        print()
        print("user are playing game...")
        for i in range(3):
            print(i+1)
            time.sleep(1)
        print("user finished playing.")
        print()

        print("Do you want to exit?[y|n]")
        toexit = input()

        if toexit == 'y':
            break


# main program
print("=====================")
print("=== My Funny Game ===")
print("===    Ver 1.0    ===")
print("=====================")
print("\n\n")

init()

bg_img = "bgimg.png"
loadImage(bg_img)

bg_music = "bgmusic.mp3"
loadMusic(bg_music)

acct_info = "acct_info.txt"
loadAccountInfo(acct_info)

start()