"""
list method - count()

Returns the count of number of items passed as an argument

"""

my_list = ['p','r','o','b','l','e','m'] * 3

# how many times of 'o' ?

# solution 1.
target = 'p'

count = 0
for item in my_list:
    if item == target:
        print(item)
        count = count + 1
print("The target of {t} occurs for {cnt} times.".format(t=target, cnt=count))


# solution 2. count()
cnt = my_list.count(target)
print("The target of {t} occurs for {cnt} times.".format(t=target, cnt=cnt))

# start = 2
cnt = my_list.count(target)
print("The target of {t} occurs for {cnt} times.".format(t=target, cnt=cnt))

