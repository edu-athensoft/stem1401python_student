"""
find max and min from 10 given numbers

1. find max
2. find min


1. find max
fetch each number one by one and compare it with the current max
when all numbers have been finished scanning,
the current max number is the result.

pseudo-code

given a0 to a9 as List
(hard code)

set a0 as current max

scan and compare
  a0 >? max
  if true, a0 -> max

  a1 >? max
  if true, a1 -> max
  else do nothing

  a2 >? max
  if true, a2 -> max
  else do nothing

  ...

  a9 >? max
  if true, a2 -> max
  else do nothing

print out the final result
"""

# input
a0 = 4
a1 = 500
a2 = 8
a3 = 12
a4 = 43
a5 = 15
a6 = 8
a7 = 4
a8 = 300
a9 = 21

# max = a0
# min = a0

max = min = a0

if a0 > max:
    max = a0
if a0 < min:
    min = a0

if a1 > max:
    max = a1
if a1 < min:
    min = a1

if a2 > max:
    max = a2
if a2 < min:
    min = a2

if a3 > max:
    max = a3
if a3 < min:
    min = a3

if a4 > max:
    max = a4
if a4 < min:
    min = a4

if a5 > max:
    max = a5
if a5 < min:
    min = a5


if a6 > max:
    max = a6
if a6 < min:
    min = a6

if a7 > max:
    max = a7
if a7 < min:
    min = a7

if a8 > max:
    max = a8
if a8 < min:
    min = a8

if a9 > max:
    max = a9
if a9 < min:
    min = a9

# output result
print("The max number is {}".format(max))
print('The min number is {}'.format(min))




"""
Andy

2.find min
find min fetch each number one by one compare it with the current min
when all numbers have been finished scanning
the current min number is the result

given a0 to a9 as a list
set a0 as current min
scan and compare
set a0 as current min
    a0 <? min
    if true, a0 -> min
set a1 as current min
    a1 <? min
    if true, a1 -> min
    else do nothing
set a2 as current min
    a2 <? min
    if true, a2 -> min
    else do nothing
    ...
set a9 as current min
    a9 <? min
    if true, a9 -> min
    else do nothing
print out the final result

"""


