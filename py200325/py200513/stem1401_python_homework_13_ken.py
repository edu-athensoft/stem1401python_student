"""
For May 13th, 2020.
stem1401_python_homework_12_ken
Number Formatting.
"""

# d - Decimal integer
# --- Padding ---
# 5 total characters, pad the right with "y"
print("{:y<5d}".format(123))
# 6 total characters, pad the left with "w"
print("{:w>6d}".format(123))
# --- Alignment ---
# Right align with width 20
print("{:20d}".format(123))
# Left align with width 10 (like normal since left aligned is default)
print("{:<10d}".format(123))
# Center align with width 23
print("{:^23d}".format(123))


# c - Corresponding Unicode Character of 123
print("{:c}".format(1123))


# b - Binary
print("Your number in binary is 0b{:b}".format(int(input("Write down a number in decimal: "))))


# o - Octal
print("Your number in octal is 0o{:o}".format(int(input("Write down a number in decimal: "))))


# x - Hexadecimal lowercase
print("Your number in hexadecimal is 0x{:x}".format(int(input("Write down a number in decimal: "))))



# X - Hexadecimal Uppercase
print("Decimal to Hexadecimal color code")
digits_1_2 = int(input("Please write down your first integer ranging from 0 to 255: "))
digits_3_4 = int(input("Please write down your second integer ranging from 0 to 255: "))
digits_5_6 = int(input("Please write down your third integer ranging from 0 to 255: "))
if 0<=digits_1_2<=255 and 0<=digits_3_4<=255 and 0<=digits_5_6<=255:
    # Using the padding to have 6 characters for the hex by adding 0 when not enough
    print("Here is a color in hexadecimal that corresponds to your three inputs : {:0>2X}{:0>2X}{:0>2X}".format(digits_1_2, digits_3_4, digits_5_6))
else:
    print("You've entered an input that does not correspond to the requirements.")
    quit()



# e - Exponential notation
some_scientific_data_that_is_needed_in_standard_notation = float(input("Input the speed of light as a decimal number (km/s): "))
print("The speed of light is {:e}km/s.".format(some_scientific_data_that_is_needed_in_standard_notation))



# % - Percentage
n_boys = 12
n_girls = 13
n_total = n_boys + n_girls
print("{:%} of the class is composed of boys.".format(n_boys / n_total))