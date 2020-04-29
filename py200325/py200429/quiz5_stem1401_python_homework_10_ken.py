"""
For April 29th, 2020. Quiz 5 - stem1401_python_homework_10_ken
"""
# Question 6.2
list1 = [1,2,3,4,5,6]
print(list1[0])
print(list1[5])

# Question 6.3
list1[3] = 999

# Question 6.4
tuple1 = ("Hey","There","You","The","Guy","Hey")

# Question 6.5
# we cannot change items in a tuple / b. No

# Question 6.6
print({1,1,2,2,3,3})
# {1,2,3}

# Question 6.7
dict1 = {
    "Dog" : "Canine",
    "Cat" : "Feline"
}
print(dict1)

a = "1.0"
b = float(a)
print(type(b))

c = 1.0
d = str(c)
print(type(d))

print(int(float("1.0")))