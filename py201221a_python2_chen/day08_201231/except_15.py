"""
demo of
try:
    pass
finally:
    pass
"""
print("main program")

try:
    print("starting ...")
    raise ValueError("My value error")

# except ValueError as ve:
#     print(ve)

finally:
    print("message in finally clause")


print("end")