"""
using lambda

original list is [1,2,3,4,5,6,7,8,9,10]
how to get a list of [4,8,12,16,20]
"""

orginal_list = [1,2,3,4,5,6,7,8,9,10]
result_list = list(map(lambda x:2*x, filter(lambda x:x%2==0, orginal_list)))
print(result_list)