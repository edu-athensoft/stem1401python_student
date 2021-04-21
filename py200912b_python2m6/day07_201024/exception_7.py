"""
catching specific exceptions
and print out error message

keyword:    as
"""


print("=== start ===")
mylist = ['5','a','0','2','3']


for value in mylist:
    try:
        result = 1 / int(value)
        print(result)
        print()
    except ValueError as ve:
        print(ve)
        print()
    except ZeroDivisionError as zde:
        print(zde)
        print()
    except TypeError as te:
        print(te)
        print()
    except Exception:
        print("Error")
        print()

print("=== end ===")





