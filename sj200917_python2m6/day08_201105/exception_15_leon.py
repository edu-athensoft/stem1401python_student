try:
    num = int(input("Enter a number:"))

    if num %2 !=0:
        raise ValueError;

except AssertionError as ae:
    print("Not Even")
except ValueError as ae:
    print("Not Even")

else:
    try:
        reciprocal = 1 / num
        print(reciprocal)
    except ZeroDivisionError as zde:
        print("Zero Division Error")
    finally:
        try:
            if num >= 0:
                print("Ok")

        except ValueError as ve:
            print("Fail")
    print()


