"""
[Homework]
3. Write a program to reproduce SyntaxError. Three syntax errors are required
4. Write a program to reproduce IndexError
5. Write a program to reproduce TypeError
"""


class FirstSyntaxError(Exception):
    pass


class SecondSyntaxError(Exception):
    pass


class ThirdSyntaxError(Exception):
    pass


while True:
        sentence = input("Input a sentence: ")
        if any(i.isupper() for i in sentence[0]):
            pass
        else:
            try:
                raise FirstSyntaxError("A sentence must starts with a capital letter. Yours does not start with a capital letter. Please try again!")
            except FirstSyntaxError as fe:
                print(fe)
        if any(i.islower() for i in sentence):
            pass
        else:
            try:
                raise SecondSyntaxError("A sentence is composed of at least one lower letter. Yours does not include one. Please try again!")
            except SecondSyntaxError as se:
                print(se)
        if any(i.isspace() for i in sentence):
            print("Everything is fine! Great job!")
            break
        else:
            try:
                raise ThirdSyntaxError("A sentence must contains at least one space. Yours does not have one. Please try again!")
            except ThirdSyntaxError as te:
                print(te)


