"""
datetime.time
time object

"""


from datetime import time

#
default = time()
print(f"default time is {default}")

# hour, min, second
time2 = time(11,22,58)
print(time2)

# time2 = time(11,22,66)
# print(time2)

# time2 = time(11,60,45)
# print(time2)

# 0..23
time2 = time(23,36,45)
print(time2)

# time2 = time(24,36,45)
# print(time2)

time2 = time(hour=21, minute=37, second=47)
print(time2)


time3 = time(hour=21)
print(time3)

time3 = time(hour=21, minute=37)
print(time3)

time3 = time(minute=37)
print(time3)


# microsecond
time4 = time(microsecond=37)
print(time4)

time4 = time(hour=21, minute=37, second=47, microsecond=37)
print(time4)