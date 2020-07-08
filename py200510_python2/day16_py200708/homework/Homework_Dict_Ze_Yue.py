"""
Ze Yue Li
7/7/2020
Exercises on Dictionary
1. Write a Python script to sort (ascending and descending) a dictionary by value.
2. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
3. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
4. Write a Python script to check whether a given key already exists in a dictionary.
5. Write a Python program to iterate over dictionaries using for loops.
6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

# Question 1
my_dict = {'a': 37, 'b': 45, 'c': 39}
list1 = []
for i in list(my_dict):
    list1.append(my_dict[i])
list2 = sorted(list1)
print(list2)
dict2 = {'1': list2[0], '2': list2[1], '3': list2[2]}
print(dict2)

my_dict = {'a': 37, 'b': 45, 'c': 39}
list1 = []
for i in list(my_dict):
    list1.append(my_dict[i])
list2 = sorted(list1, reverse=True)
print(list2)
dict2 = {'1': list2[0], '2': list2[1], '3': list2[2]}
print(dict2)


# Question 2
my_dict = {1: 10, 2: 20}
my_dict[3] = 30
print(my_dict)


# Question 3
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
dict4 = {}
for i in list(dict1):
    dict4[i] = dict1[i]
for i in list(dict2):
    dict4[i] = dict2[i]
for i in list(dict3):
    dict4[i] = dict3[i]
print(dict4)


# Question 4
dict3 = {5:50, 6:60}
print(5 in dict3)



# Question 5
dict3 = {5:50, 6:60, 7:70, 8:80, 9:90}
for i in dict3:
    print(i, dict3[i])


# Question 6
num = 5
dict1 = {}
for i in range(1, num+1):
    dict1[i] = i*i
print(dict1)