team = [["Robert Master", 220, 340],
        ["Montreal Sprite", 320, 270],
        ["Nova Robert", 450, 380],
        ["Smart Maker", 115, 405],
        ["10 Stars", 100, 330]]
first = None
second = None
third = None
fourth = None
fifth = None
for i in range(len(team)):
# the i actually means the last element of "team"
# in this case, we start with "10 Stars"
    if team[i][1] > team[i][2]:
        first = team[i][0], team[i][1]
# from here, all the different equations involving i are actually from where we want to start looking
# in this case, we start with "Smart Maker"
    if team[i-1][2] > team[i-1][1]:
        second = team[i-1][0], team[i-1][2]
# in this case, we start with "Montreal Sprite"
    if team[i-3][2] > team[i-3][1]:
        third = team[i-3][0], team[i-3][2]
# in this case, we start with "10 Stars"
    if team[i][2] > team[i][1]:
        fourth = team[i][0], team[i][2]
    if team[i-3][1] > team[i-3][2]:
        fifth = team[i-3][0], team[i-3][1]
print(f"{first}: First place")
print(f"{second}: Second place")
print(f"{third}: Third place")
print(f"{fourth}: Fourth place")
print(f"{fifth}: Fifth place")