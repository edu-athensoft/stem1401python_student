"""
the full syntax of exception handling
"""

"""
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
"""

try:
    num = int(input("Input a number:"))
    if num <= 0:
        raise ValueError(f"invalid literal for positive int with base 10:'{num}'")

except ValueError as ve:
    print(ve)

else:
    print("Everything fine")

finally:
    print("this is finally clause")



try:
    num = int(input('Please enter a number:'))

    if num <= 0:
        raise ValueError('That is not a positive integer')

except ValueError as ve:
    print(ve)

else:
    print('enter again')

finally:
    print('This is finally clause')



"""
try:
    pass
except:
    pass
finally:
    pass
else:
    pass
"""

