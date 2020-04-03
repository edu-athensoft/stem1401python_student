import random
# random number value
rand_num = random.randint(1, 101)
# intro
print("Welcome to the Guessing Game!")
# difficulty
print("1. I'm too young to die")
print("2. Hey, not too rough")
print("3. Hurt me plenty")
print("4. Ultra-Violence")
print("5. Nightmare")
print("6. ULTRA-NIGHTMARE!! (for Chads only)")
difficultystr = input("Please input your choice:")
difficulty = int(difficultystr)

chances = 0

# number of chances
if difficulty == 1:
    chances = 30
if difficulty == 2:
    chances = 25
if difficulty == 3:
    chances = 20
if difficulty == 4:
    chances = 15
if difficulty == 5:
    chances = 10
if difficulty == 6:
    chances = 5


# gameplay
flag = True
print("The game has started.")
print("You have", chances, "chances. Good Luck!")

while flag:
    input_int = int(input("Please input a number:"))
    chances -= 1
    if input_int < rand_num:
        print("Your number is too small.")
        print("You have", chances, "chances left.")
    elif input_int > rand_num:
        print("Your number is too big.")
        print("You have", chances, "chances left.")
    elif input_int == rand_num:
        print("Great! You guessed the number!")
        flag = False
    if chances == 0:
        print("The number was", rand_num, "Y̷̝͕̊͒͐ͅo̷͓̠̲̒̕u̵̳̝͈̿͜ŗ̸̫̪̖̓ ̷͔͆͂s̵̻̺͎̺͒o̷̘̥̚u̶͕͛̇̎l̴̦̗͋̏̓̑ ̴̺̤͒w̵̦̳͆͠ī̷̝̾̀͝l̵̢̝̤̀̓̆ͅl̸͇̭̀͌̈́͝ ̷̲͙̣͌͝n̵̦̳͂͋̒͘o̷̮͆̽̈́w̵͎̱̏̈̍͠ ̴̠̗͙̖̍̀̊̅b̵͓̦̣̂̉e̵̡͔͑̾ ̸̢̥̻̀̚͜͝ç̷͔̻̏̄̅o̴̱̤̥̿̔n̸̡̖̄s̸̨͈̯͑͊ú̸̧̮͘m̸̬͔̀e̴͍̖͝d̶̠̠̔͜͝")
        flag = False

