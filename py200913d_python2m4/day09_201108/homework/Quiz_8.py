"""
Quiz 8

1. +, -, *, /, //, %, **
2. ==, >, <, >=, <=,      !=
3. and,or          not
4. &               & | >> << >>>
5. is, is not
6. in, not in
7.  x += 1 -> x = x + 1
8.
9. list1 = [1, 2, 4, 3, 5]
   list2 = [1, 2, 4, 3, 5]


   if list1 == list2:
       print("The lists are identical")
   else:
       print("The lists are not identical")

10.
input("Today is:")

Today = days_of_week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

if Today == Monday:
    print("It will be a Wednesday after 100 days")
if Today == Tuesday:
    print("It will be a Thursday after 100 days")
if Today == Wednesday:
    print("It will be a Sunday after 100 days")
if Today == Thursday:
    print("It will be a Saturday after 100 days")
if Today == Friday:
    print("It will be a Sunday after 100 days")
if Today == Saturday:
    print("It will be a Monday after 100 days")
if Today == Sunday:
    print("It will be a Tuesday after 100 days")


"""

# question 9.
list1 = [1, 2, 4, 3, 5]
list2 = [1, 2, 4, 3, 5]

# value, ==
if list1 == list2:
    print("The lists are identical")
else:
    print("The lists are not identical")
print()


# is identical
if list1 is list2:
    print("The lists are identical")
else:
    print("The lists are not identical")

print()


list1[0] = 99
print("list1", list1)

print("list2", list2)



#
list1 = [1, 2, 4, 3, 5]
list2 = list1
list1[0] = 999
print("list1", list1)

print("list2", list2)







b1 = True
b2 = False

result = b1 and b2
# print(result)

"""
AND
b1      b2
TRUE    TRUE    TRUE
FALSE   TRUE    FALSE
TRUE    FALSE   FALSE
FALSE   FALSE   FALSE
"""


result = b1 or b2
# print(result)

"""
OR
b1      b2
TRUE    TRUE    TRUE
TRUE    FALSE   TRUE
FALSE   TRUE    TRUE
FALSE   FALSE   FALSE
"""

result = not b1
# print(result)


result = not b2
# print(result)



sentence = "This is a sentence to test."
# Is 'a'/'A' in the sentence?
# expected result -> True

result1 = 'b' in sentence
if result:
    print("There is letter b in the sentence.")

result2 = 'B' in sentence
if result:
    print("There is no letter B in the sentence.")

result = result1 or result2
if result:
    print(result, "There exists")
else:
    print(result, "There not exists")


sentence = "These were sentences to test."
# Is 'a'/'A' in the sentence?
# expected result -> False


word = 'abcd'

word = ('a','b','c','d')

# for c in word:
#     print(c)






















