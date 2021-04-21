"""
My simple converter

kilometers -> miles
"""
input('=== Kilometers to miles converter ===')

kilometer = (float(input("Please enter the number of kilometers that you want to convert:")))

mile = kilometer * 0.621371

if kilometer <= 0:
    print("Please enter a number grater than 0")
else:
    print(print("{} kilometers is equal to {} miles".format(kilometer,mile)))

