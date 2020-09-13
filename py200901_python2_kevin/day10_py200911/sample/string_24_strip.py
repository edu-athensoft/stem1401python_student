"""
strip()
lstrip()
rstrip()

remove space chars on left and right
"""

# Example 1.
str1 = "  book  "
print(f"|{str1}| ,  {len(str1)}")

str2 = str1.strip()
print(f"|{str2}| ,  {len(str2)}")
print()


# Example 2.
str1 = " \nbook\t  "
print(f"|{str1}| ,  {len(str1)}")

str2 = str1.strip()
print(f"|{str2}| ,  {len(str2)}")
print()


# Example 3.
str2 = str1.lstrip()
print(f"|{str2}| ,  {len(str2)}")


# Example 4.
str2 = str1.rstrip()
print(f"|{str2}| ,  {len(str2)}")
print()

# Example 5
str3 = ' bo ok '
str3 = str3.strip()
print(f'|{str3}|')

