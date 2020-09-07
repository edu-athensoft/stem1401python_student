"""
list.count() - returns the count of number of items passed as an argument
"""

list1 = ['abc1','abc2','abc3','abc1','abc2','abc2','abc3','abc4','abc1','abc2','abc3']


target = 'abc1'

# for-loop, if
count = 0
for word in list1:
    if target == word:
        count += 1
print("count of {} = {}".format(target, count))

# list.count()
result = list1.count(target)
print("result of {} = {}".format(target, result))