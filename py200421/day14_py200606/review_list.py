"""
review list
"""

# TypeError: '<' not supported between instances of 'str' and 'int'
my_list = [2,'a5',1,'b6',7]
# my_list.sort()



# original password: mylaptop
# encrypt by reversing

original_pwd = ['m','y','l','a','p','t','o','p']
print(original_pwd)
original_pwd.reverse()
new_pwd = original_pwd
print(new_pwd)

result = ''
for i in new_pwd:
    result += i
print("Encrypted password is '{}'".format(result))





