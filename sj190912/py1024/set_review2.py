# assuming that everyone of us plays video game
# me = {'wow', 'lol', 'wot', 'minecraft', 'roblox'}

person1 = {'wow', 'lol', 'wot', 'minecraft', 'roblox'}
person2 = {'bns','perfect world', 'wow', 'black desert','wot', 'maple story2'}

#
all_games = person1 | person2
print(all_games)

all_games = person1.union(person2)
print(all_games)

#
shared_games = person1 & person2
print(shared_games)

shared_games = person1.intersection(person2)
print(shared_games)

# person1 exclusive
person1_only = person1.difference(person2)
print('person1 only',person1_only)

# person2 exclusive
person2_only = person2.difference(person1)
print('person2 only',person2_only)