"""

1, 2, 3, 4, ..., 20 ?
product = 1x2x3x....x20
"""

product = 1

"""
product x 1 -> product
product x 2 -> product
...

product x 20 -> product
"""

for i in range(1,21):
    product = product * i

print("Product is {}".format(product))

"""
2432902008176640000
2432902008176640000
"""