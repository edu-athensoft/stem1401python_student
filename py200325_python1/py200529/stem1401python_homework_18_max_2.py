"""
Quiz 10
"""

# 2.
product = 1
for i in range(1,11):
    product *= i * 2

print(product)

# 3.
group_191116 = {'Marie'     : 65,
                'Phoebe'    : 78,
                'Sabrina'   : 95,
                'Emma'      : 85,
                'Amy'       : 73,
                'Isabelle'  : 59,
                'Clark'     : 45
}

total_score = 0

for i in group_191116.values():
    total_score += i

average = total_score / len(group_191116)
print("The average score in the class is {}".format(average))

# 4.
# I don't know how to print a table
for i in range(1,10):
    for x in range(1,i+1):
        print("{}*{}={}".format(x,i,x*i))

