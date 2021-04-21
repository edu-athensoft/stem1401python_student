# ex 1.
# create a list with 6 items
# i.e
fruits = ['apple','pineapple','orange',
          'watermelon','peach','grape']
print(fruits)

sports = ['basketball', 'football', 'hockey',
          'baseball', 'soccer', 'gymnastic']
print(sports)

animals = ['dog','cat','horse',
           'mouse','cow','bird']
print(animals)

drinks = ['coca cola', '7up', 'Sprite', 'soda water', 'Red Bull', 'Monster Energy']
print(drinks)


# ex 2.
# add a sequence no to your first item
# i.e. 'apple' => '1.apple'
# ['1.apple', 'pineapple', 'orange', 'watermelon', 'peach', '6.grape']
animals = ['dog','cat','horse','mouse','cow','bird']
animals[0] = '1.dog'
animals[5] = '6.bird'
print(animals)

print("=====")
mylist = ['basketball', 'football', 'hockey', 'baseball', 'soccer', 'gymnastic']
print(mylist)
mylist[0] = '1.basketball'
print(mylist)
mylist[5] = '6.gymnastic'
print(mylist)

#
mylist = ['coca cola', '7up', 'Sprite', 'soda water', 'Red Bull', 'Monster Energy']
mylist[0] = '1.coca cola'
print(mylist)
mylist[5] = '6.Monster Energy'
print(mylist)


# add a sequence no to your last item
# i.e. 'grape' => '6.grape'

# mylist = ["a",'b','c']
# mylist[0] = '1.a'
# print(mylist)


# calculate how many items you have in the list?
# your codes go here
num = len(mylist)
print("There are", num, "items in the list.")

# Expected Result on console: 'There are 6 items in the list.'

num = len(sports)
print("There are", num, "items in the list")

