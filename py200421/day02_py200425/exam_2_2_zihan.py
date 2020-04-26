input_list = list(input("Please input a string:     "))
input_character = str(input("Please input a character:      "))
no_of_times = 0
for i in input_list:
    if i == input_character:
        no_of_times += 1
print(no_of_times)