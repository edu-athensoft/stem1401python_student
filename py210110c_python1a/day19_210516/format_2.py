"""
String formatting

Number formatting for signed numbers
"""

# show the + sign
num = 12.23
num2 = -12.23
print("|{:f}| |{:f}|".format(num, num2))
print("|{:+f}| |{:+f}|".format(num, num2))

# show space for + sign
print("|{: f}| |{: f}|".format(num, num2))
