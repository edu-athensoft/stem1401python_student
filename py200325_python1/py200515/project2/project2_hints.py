"""
how to choose variable name and datatype for your data set
"""

"""
qty_n
desc_n
price_n
amount_n

list?
tuple?
set?
dictionary?

1. quantity of names (variable) decreased much
2. list access data item using loop by index(ing)
"""
item0 = [1, 'Front', 100, 0]
item1 = [2, 'New', 15, 0]
item2 = [3, 'labor', 5, 0]
items= [item0, item1, item2]

items = [[1, 'Front', 100, 0],
        [2, 'New', 15, 0],
         [3, 'labor', 5, 0]]

items[0][3] = items[0][0] * items[0][2]
items[1][3] = items[1][0] * items[1][2]
items[2][3] = items[2][0] * items[2][2]

subtotal = items[0][3] + items[1][3] + items[2][3]
tax_rate = None
total = None



# variables -> String template

line1='|========================================|'

print(line1)
print()
print(line1)
print()
print(line1)


# ========================
# mix list and tuple
([],[],[])
[(),(),()]








