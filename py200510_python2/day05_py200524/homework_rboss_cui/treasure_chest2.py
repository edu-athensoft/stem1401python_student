print('Input quit if you wanna leave')
print('The chances of the chest is: \n Normal         63.7979999% \n Magic                  25% \n '
      'Rare                   10% \n Legendary               1% \n Ancient Legendary     0.2% \n Mythic              0.002% \n '
      'Secret          0.0000001%')
normal = 0
magic = 0
rare = 0
leg = 0
ancient_leg = 0
mythic = 0
secret = 0
chest = 0
while True:
 x = input('Enter (1) if you want to open a chest, enter (3) if u want to open 3 chests, enter (quit) if you want to quit:')
 from random import randint as rand
 a = rand(1,1000000000)
 if x == '1':
  if a < 637979999:
    result = 'Normal'
    normal += 1
  elif 637979999 <= a < 887979999:
    result = 'Magic!'
    magic += 1
  elif 887979999 <= a < 987979999:
    result = 'Rare!!'
    rare += 1
  elif 987979999 <= a < 997979999:
    result = 'Legendary!!!'
    leg += 1
  elif 997979999 <= a < 999979999:
    result = 'Ancient Legendary!!!!'
    ancient_leg += 1
  elif 999979999 <= a < 999999999:
    result = 'Mythic!!!!! Your lucky'
    mythic += 1
  elif a == 1000000000:
    result = 'Secret!!!!!! Your luck is insane!'
    secret += 1
  print('You got a {}'.format(result))
  chest += 1
  print('You opened {} chests'.format(chest))
 if x == '3':
     for i in range(3):
         a = rand(1, 1000000000)
         if a < 637979999:
             result = 'Normal'
             normal += 1
         elif 637979999 <= a < 887979999:
             result = 'Magic!'
             magic += 1
         elif 887979999 <= a < 987979999:
             result = 'Rare!!'
             rare += 1
         elif 987979999 <= a < 997979999:
             result = 'Legendary!!!'
             leg += 1
         elif 997979999 <= a < 999979999:
             result = 'Ancient Legendary!!!!'
             ancient_leg += 1
         elif 999979999 <= a < 999999999:
             result = 'Mythic!!!!! Your lucky'
             mythic += 1
         elif a == 1000000000:
             result = 'Secret!!!!!! Your luck is insane!'
             secret += 1
         print('You got a {}'.format(result))
         chest += 1
         print('You opened {} chests'.format(chest))
 while x != '1' and x != 'quit' and x != '3':
    x = input('Enter (1) if you want to open a chest, enter (3) if u want to open 3 chests, enter (quit) if you want to quit:')
 if x == 'quit':
    print(' Congrats!!')
    print(' You opened {} chests'.format(chest))
    print(' You got {} Normals \n You got {} Magics \n You got {} Rares \n You got {} Legendaries \n You got {} Ancient Legendaries \n '
          'You got {} Mythics \n You got {} Secrets'.format(normal,magic,rare,leg,ancient_leg,mythic,secret))
    break