# import random
# classes = ['bandit guy', 'knight guy', 'elf guy', 'demon guy', 'gay guy']
# who_tf_are_you = 'gay guy'
# your_luck = 0
# for i in range(1000):
#     if (random.choice(classes)) == who_tf_are_you:
#         your_luck = your_luck + 1
#     else:
#         pass
# print(round(your_luck/1000*100))


import random
classes = ['bandit guy', 'knight guy', 'elf guy', 'demon guy', 'gay guy']

def testing_prob(x):
    your_luck = 0
    for i in range(1000):
        if (random.choice(classes)) == x:
            your_luck += 1
        else:
            pass
    print(round(your_luck / 1000 * 100))

testing_prob('gay guy')
testing_prob('bandit guy')
testing_prob('knight guy')
testing_prob('elf guy')
testing_prob('demon guy')