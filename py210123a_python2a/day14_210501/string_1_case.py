"""
String methods - case

Python String capitalize()                      [yes]
Converts first character to Capital Letter

Python String casefold()                        [no1]
converts to case folded strings

Python String islower()                         [yes]
Checks if all Alphabets in a String are Lowercase

Python String isupper()                         [yes]
returns if all characters are uppercase characters

Python String upper()                           [yes]
returns uppercased string

Python String lower()                           [yes]
returns lowercased string

Python String swapcase()                        [yes]
swap uppercase characters to lowercase; vice versa

Python String title()                           [yes]
Returns a Title Cased String

"""

# string1 = 'abc'
# print(string1.islower())
#
# string1 = 'ABC'
# print(string1.islower())


def mycase(mystr):
    print("1. upper()")
    result = mystr.upper()
    print(result)
    print()

    print("2. lower()")
    result = mystr.lower()
    print(result)
    print()

    print("4. islower()")
    result = mystr.islower()
    print(result)
    print()


# main
str1 = 'xyZ'
print(f"Original string is {str1}\n")

mycase(str1)