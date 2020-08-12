"""
Specifying multiple specific errors

the order of exception occurring

Why to specify errors?
for better performance
"""


# import sys

random_list = ['a',0,2]

for entry in random_list:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except ValueError as e:
        print(f"Oops, {e.__class__} occurred")
        print()
    except (TypeError, ZeroDivisionError) as e:
        print(f"Oops, {e.__class__} occurred")
        print()
    except Exception as e:
        print(f"Oops, {e.__class__} occurred")
        print()

print(f"The reciprocal of {entry} is {r}")
