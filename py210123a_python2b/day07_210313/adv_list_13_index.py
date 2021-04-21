"""
index(value)
index(value, start)
index(value, start, end)
returns the index of the first matched item
"""

odd = [1,2,10,31,5,10,7,9,10,12,14,10]

value = 10

pos = odd.index(value)
print(f"Position is {pos}")

print("Position is {}".format(pos))

# if we are going to delete 10
# index(value) + pop(index) =  remove(value)

start = 3
pos2 = odd.index(value,start)
print(f"Position2 is {pos2}")


#
start = 3
end = 5
if value in odd[start:end]:
    pos3 = odd.index(value, start, end)
    print(f"Position3 is {pos3}")
else:
    print(f"does not exist in the range of [{start}:{end}]")



