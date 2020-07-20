"""
file close()

close safely in finally clause of try structure
"""

"""
try:
    f = open("file5_mode_r.txt")
    print("file opened.")

    f.close()
    print("file closed.")

except Exception as e:
    print(e)
"""

"""
try:
    f = open("file5_mode_r.txt")
    print("file opened.")

    raise ValueError("my value error")

    f.close()
    print("file closed.")

except Exception as e:
    print(e)

finally:
    pass
"""


try:
    f = open("file5_mode_r.txt")
    print("file opened.")

    raise ValueError("my value error")

except Exception as e:
    print(e)
    
finally:
    f.close()
    print("file closed.")
