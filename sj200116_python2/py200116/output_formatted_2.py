"""
formatted output
String format()
"""

# review

# greeting1 = "Good evening, Athens!"
# greeting2 = "Good evening, Yixuan!"
# greeting3 = "Good evening, Youran!"
# greeting4 = "Good evening, Chengjun!"
# greeting5 = "Good evening, Leon!"

name1 = "Athens"
name2 = "Yixuan"
name3 = "Youran"
name4 = "Chengjun"
name5 = "Leon Li"

greeting = "Good evening, {}! Can I have your full name, Mr./Miss {}?"

print(greeting.format(name5, name5))
# why we are using variables

greeting = "Good evening, {}! Can I have your full name, Mr./Miss {}?"

print(greeting.format("Leon", "Leon"))




