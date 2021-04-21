"""
open a file
error-free
to avoid program crushing

"""

# import os
# import os.path
try:
    print("Start opening file...")
    filepath = "../day10_201114/review1.py"
    print("\t"+filepath)
    file = open(filepath)

    print("Closing...")
    file.close()

except FileNotFoundError as fe:
    print(fe)

except IOError as ioe:
    print(ioe)

except Exception as e:
    print(e)

print("Done.")