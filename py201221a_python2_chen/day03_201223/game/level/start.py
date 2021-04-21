"""
module: start

game entrance

init() -  initializing
    load bg img
    load bg music
    load account info

start()
    load a game level
    users play the level
    sys close the level

    if the player wants to continue to play,
        he/she can press 'y'
    else
        he/she can press 'n' or any other words
        the start() function comes to end

close()

"""

import time

import py201221a_python2_chen.day03_201223.game.level.load as gmlvLoad
import py201221a_python2_chen.day03_201223.game.level.over as gmlvOver

# import py201221a_python2_chen.day03_201223.game.level.over as gmlvOver


def init():
    print("init()")

    bgImgName = bgImage
    bgMusicName = bgMusic
    acctInfoData = acctInfo

    loadImage(bgImgName)
    loadSnd(bgMusicName)
    loadAcctInfo(acctInfoData)


def start():
    print("start()")

    while True:

        # step 1. load a game level
        print("Please choose a game level:", end="")
        level_id = input()
        game_data = 'game data'
        gmlvLoad.loadLevel(level_id, game_data)
        print()

        # step 2. user plays a game level
        print(f"Player is playing the game level of {level_id}...")
        seconds = 5
        for i in range(seconds):
            print(f"{i + 1}")
            time.sleep(1)
        game_data = "updated game data"
        print(f"Player finished the game level of {level_id}")
        print()

        # step 3. close the game level and release all related resources
        gmlvOver.closeLevel(level_id, game_data)

        print("Do you want to continue?",end="")
        result = input()

        # if the player press 'y' , then continue
        # otherwise the game level stops and exit from the loop
        if result == 'y' or result =='Y':
            pass
        else:
            break


def close():
    # print("close()")

    bgImgName = bgImage
    bgMusicName = bgMusic
    acctInfoData = acctInfo

    gmlvOver.gameover(bgImage, bgMusic, acctInfo)


def loadImage(bgImgName):
    print(f"loadImage({bgImgName})")


def loadSnd(bgMusicName):
    print(f"loadSnd({bgMusicName})")


def loadAcctInfo(acctInfoData):
    print(f"loadAcctInfo({acctInfoData})")



# main program

# set global variable/constant
bgImage = 'bg-img.jpg'
bgMusic = 'bg-music.mp3'
acctInfo = 'player1001-acctinfo'

print("=====================")
print("=== My Funny Game ===")
print("===    Ver 1.0    ===")
print("=====================")
print("\n\n")


init()
print()

start()
print()

close()



