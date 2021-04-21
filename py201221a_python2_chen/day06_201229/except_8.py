"""
to catch specific exception


"""

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/ int(entry)
        break

    except ValueError as ve:
        print(ve)
        print("Please input a compatible literal for int()")
        print()

    except ZeroDivisionError as zde:
        print(zde)
        print("Please do not do division with 0")
        print()

print("The reciprocal of", entry, 'is', r)