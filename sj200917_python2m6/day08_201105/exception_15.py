"""
try:
    pass
except:
    pass
except:
    pass
else:
    pass
finally:
    pass
"""


try:
    num = int(input("Enter a number: "))

    if num %2 != 0:
        raise ValueError;

except ValueError as ve:
    print("Invalid value!")

else:
    try:
        # num = "abc"
        reciprocal = 1 / num
        print(reciprocal)

    except ZeroDivisionError as zde:
        print("ZeroDivisionError")
    except ValueError as ve:
        print("Invalid value")
    except TypeError as ve:
        print("Invalid data type")
    except Exception as e:
        print("Internal error!")

finally:
    print("finally block")
    print("program completed.")

