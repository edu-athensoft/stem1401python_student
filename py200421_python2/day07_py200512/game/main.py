"""
main app of game
"""

import py200421.day06_py200509.game.level.load as lvlload
import py200421.day06_py200509.game.level.start as lvlstart
import py200421.day06_py200509.game.level.stop as lvlstop



print("==== My Game Main UI ====")

# level pck start.gameinit()
lvlstart.gameinit()

# level pck load.load("save-name-1")
# level pck load.loadnew()
lvlload.loadnew()



# level pck start.gamestart()
lvlstart.gamestart()

# level pck start.gameplay("scene-1")
lvlstart.gameplay("scene 1-1")



# level pck stop.save("save-name-1")
lvlstop.save("save-name-1")

# level pck stop.gamestop()
lvlstop.gamestop()


print("==== End of Game ====")

