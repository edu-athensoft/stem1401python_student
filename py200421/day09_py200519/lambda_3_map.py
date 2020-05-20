"""
map()

original_list=[1,2,3,4,5,6,7,8]

expected_list=[2,4,6,8,10,14,16]


"""
original_list = [1, 2, 3, 4, 5, 6, 7, 8]
original_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

a = map(lambda x: 2 * x, original_tuple)
print(a, type(a))

# b = list(a)
b = tuple(a)
print(b)
