"""
you can input a Name again and again from keyboard

Bonsoir, the Name!

if you input 'Eva'
print out   Bonjour, Eva
and then exit the program
"""

def greeting(name):
    print("Bonsoir {}".format(name))

while True:
    name = input("Input your name:")
    if 'eva' == name.lower():
        print('Bonjour {}'.format(name))
        break
    else:
        greeting(name)

