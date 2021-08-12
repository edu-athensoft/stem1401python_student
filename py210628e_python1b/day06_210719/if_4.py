"""
to help your parent to make a decision on whether you should switch on the air conditioner?

when it is greater than 24 c,
  we switch on the air-c
otherwise,
  we don't use the air-c

[modeling]
abstract and extract
condition temp >?24

abstract
mimic, mock

pseudo-code

temp <- a certain temperature number T
T = 24

if temp > T
   print : we switch on the air-c
else
   print : we don't use the air-c

"""

# Kevin
# sensor
temp = float(input("Please enter current temp: "))

T = 24
if temp > T:
    print('switch on the air-c')
else:
    print('don\'t switch')

