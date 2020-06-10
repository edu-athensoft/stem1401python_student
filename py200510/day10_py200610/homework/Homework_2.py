# v1
password = ''
password_correct = False
while not password_correct:
    a = 0
    password2 = []
    password = input('Please input a password:')
    if password == 'q' or password == 'quit':
        print('Program terminated')
        break
    if len(password) < 8:
        print('Your password must be at least 8 characters long.')
        continue
    if password.lower() == password.upper():
        print('You need at least one letter.')
        continue
    if password.lower() == password:
        print('You need to have at least one capital letter.')
        continue
    for i in password:
        try:
            b = int(i)
            a = 1
        except ValueError:
            pass
    if a == 0:
        print('You need at least one digit.')
        continue
    a = 0
    for i in password:
        try:
            int(i)
        except ValueError:
            password2.append(i)
    for i in password2:
        if i.lower() == i.upper():
            a = 1
    if a == 0:
        print("You need at least one symbol.")
        continue
    password_correct = True
    print("Password accepted")

