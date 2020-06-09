"""
string - concatenate
"""

str1 = 'Hello'
str2 = 'world'
print("str1 is {}, str 2 is {}".format(str1, str2))


# using +
print("str1 + str2 is {}".format(str1+str2))

# using *
times = 4
targetstr = str2

print("repeating target string of {} by {} times: {}".format(targetstr, times, targetstr*times))

def gen_str(targetstr, times):
    return targetstr * times

print(gen_str(str1+str2,3))


# directly concatenate
print("===")
str3 = 'Hello''world'
print("str3 = ",str3)

str3 = 'Hello' 'world'
print("str3 = ",str3)

str3 = 'Hello'  'world'
print("str3 = ",str3)

str3 = 'Hello','world'
print("str3 = ", str3)

x, y = (1,2)
print(x)
print(y)

str3 = ('Hello' 
        'world')
print("str3 = ",str3)
