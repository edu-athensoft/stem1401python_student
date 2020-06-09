"""
string - join()
"""

words = ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']

result = ' '.join(words)
print(result, type(result))
print()

result = ''.join(words)
print(result, type(result))
print()

nums = [str(1),str(2),str(3),str(4),str(5),str(6),str(7)]
result = ','.join(nums)
print(result, type(result))
print()

