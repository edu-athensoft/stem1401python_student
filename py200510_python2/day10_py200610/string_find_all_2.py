"""
yield (generate)
function
iterator
compare with return
"""

org_str = "abc xxxab xxx123 xxxeee ffxxx"
sub_str = "xxx"

# expected result: return 4 positions


def findall(org_str, sub_str):
    start = 0
    while True:
        start = org_str.find(sub_str, start)

        if start == -1:
            return
        yield start
        start = start + len(sub_str)

print(list(findall(org_str, sub_str)))


