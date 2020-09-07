"""
[Homework]
1. Write a Python program to get a list, sorted in increasing order
   by the last element in each tuple from a given list of non-empty tuples.
   Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
   Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
2. Write a Python program to remove duplicates from a list.
3. Write a Python program to check a list is empty or not.
4. Write a Python program to clone or copy a list.
5. Write a Python program to find the list of words
   that are longer than 3 from a given list of words.
   The given words:  "The quick brown fox jumps over the lazy dog"
"""

# 1. Question
# list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(0, len(list1)):
#     print(list1[i][1])
#
#     if i-1 < i:
#         list1[i][1] = i


# print(list1)

# Question 2.
print("Question 2.")
list1 = [1, 2, 2, 3, 4, 55, 55]
for i in list1:
    n = list1.count(i)
    if n >= 2:
        list1.remove(i)

print(list1)

# Question 3.
print("Question 3.")
list1 = [1, 2, 2, 3, 4, 55, 55]
list2 = []
list3 = []  # Example, answer is True
if list3 == list2:
    print(f"The condition is {True}")
else:
    print(f"The condition is {False}")

if list1 == list2:
    print(f"The condition is {True}")
else:
    print(f"The condition is {False}")

# Question 4.
print("Question 4.")
list1 = [1, 2, 2, 3, 4, 55, 55]
list_copy = list1.copy()
print("This is copy of list1", list_copy)

# Question 5.
print("Question 5.")
sentence = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
for i in sentence:

    if len(i) > 3:
        print(i, end=" ")


