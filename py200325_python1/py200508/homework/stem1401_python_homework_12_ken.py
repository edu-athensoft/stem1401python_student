"""
For May 8th, 2020.
Quiz 6 - stem1401_python_homework_12_ken
"""

# Question 8. Didn't understand the "output a 3x2 matrix"
# and make it "3 rows and 4 columns"


# Determines whether or no there will be a newline.
length_of_row = 0

matrix1 = [
    [1, 2],
    [4, 5],
    [5, 3]
]

# for loop : go through each row
for array in matrix1:
    # for loop : go through every value
    for value in array:
        # print a value with a space and don't add a newline
        print(value, " ", end="")
        """if the number of times a value has been printed 
        is a multiple of the length of a row -> print newline"""
        length_of_row += 1
        if length_of_row%len(array) == 0:
            print("\n")




# Question 9.0.

print("Dimensions of a box output")

print("The dimension of the box is {}{}{}".format("width: "+"10"+"cm, " , "height: "+"20"+"cm, ", "depth: "+"30"+"cm."))


# Question 9.1.

width = input("Please input the width of the box in cm: ")
height = input("Please input the height of the box in cm: ")
depth = input("Please input the depth of the box in cm: ")


# Using placeholders and default order of width, height and depth.
print("The dimension of the box is {}, {}, {}.".format("width: "+str(width)+"cm" , "height: "+str(height)+"cm", "depth: "+str(depth)+"cm"))

# Question 9.2.

# Using named placeholders.
print("The dimension of the box is {depth}, {height}, {width}.".format(width = "width: "+str(width)+"cm" , height = "height: "+str(height)+"cm", depth = "depth: "+str(depth)+"cm"))

# Question 9.3.

print("The dimension of the box is {height}, {depth}, {width}.".format(width = "width: "+str(width)+"cm" , height = "height: "+str(height)+"cm", depth = "depth: "+str(depth)+"cm"))




