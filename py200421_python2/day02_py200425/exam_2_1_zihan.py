non_valid = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
input_list = list(input("Please input a string:     "))
output_list = ""
for i in input_list:
    if i not in non_valid:
        output_list = output_list + i
print(output_list)