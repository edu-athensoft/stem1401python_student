# program 2
"""
# plan:
1. define characters
2. input the string
3. create "counting"
4. define a counter function
3. count the number of each character using the counter
4. print the result of each character
"""
# program:
characters = '''abcdefghijklmnopqrstuvwxyz1234567890, ./;'#][{}~@:<>?"`¬\|'''
user_str = input("Write your string and I will count the number of time each character is occurring: ")
for characters in user_str:
    counting = {}

    def counter(user_str):
        for characters in user_str:
            try:
                counting[characters] += 1
            except KeyError:
                counting[characters] = 1
        return counting

print(counter(user_str))

