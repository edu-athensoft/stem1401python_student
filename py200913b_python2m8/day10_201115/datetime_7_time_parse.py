"""
datetime.time
time object

"""


from datetime import time

time4 = time(hour=21, minute=37, second=47, microsecond=37)
print(time4)

# parsing
print(f"hour={time4.hour}")
print(f"minute={time4.minute}")
print(f"second={time4.second}")
print(f"microsecond={time4.microsecond}")


time4 = time(hour=21, minute=37, microsecond=37)
print(time4)

# parsing
print(f"hour={time4.hour}")
print(f"minute={time4.minute}")
print(f"second={time4.second}")
print(f"microsecond={time4.microsecond} {type(time4.microsecond)}")
print(f"ms={time4.microsecond/1000}")