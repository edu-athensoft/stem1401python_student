"""
module 7. exception handling

the order of except blocks
"""

# import module sys to get the type of exception
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        # reciprocal
        break
    # except Exception as e:
    #     print("Oops!", e.__class__, "occurred.")
    #     print("Next entry.")
    #     print()
    except ValueError as ve:
        print(ve)
        print()
    except (ZeroDivisionError, TypeError) as zde:
        print(zde)
        print()
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)