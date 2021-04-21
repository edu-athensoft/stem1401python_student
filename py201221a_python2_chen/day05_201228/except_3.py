"""
why do we need exception handling?

detect errors
capture errors
handling errors

exit code 0
exit code 1
"""

try:
    num = float(input("Enter a number:"))

except Exception as e:
    print(e)

