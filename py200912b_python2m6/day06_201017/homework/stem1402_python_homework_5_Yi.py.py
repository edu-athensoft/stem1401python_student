# 1

def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

# 2

def mult():
    my_dict = {'data1':100,'data2':-54,'data3':247}
    result = 1
    for key in my_dict:
        result=result * my_dict[key]

    print(result)
print(mult())

# 3

def max_min():
    my_dict = {'x': 500, 'y': 5874, 'z': 560}

    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

    print('Maximum Value: ', my_dict[key_max])
    print('Minimum Value: ', my_dict[key_min])

print(max_min())

# 4

def rem(x):
    result = {}

    for key,value in dict.items():
        if value not in result.values():
            result[key] = value

    print(result)

dict = { 'first' : 10, 'second' : 15, 'third' : 20, 'four' : 10, 'five' : 20}

print(rem(dict))