"""
[Homework]
Date: 2021-07-22
Quiz9
Due date: 2021-07-25
"""

"""
q1:
if, elif, else
"""

# q2
list1 = input('1.Please write down a random numbers: ')
list2 = input('2.Please write down another different numbers: ')
list3 = input('3.Please write down another different numbers: ')
list4 = input('4.Please write down another different numbers: ')
list5 = input('5.Please write down another different numbers: ')
list6 = input('6.Please write down another different numbers: ')
list7 = input('7.Please write down another different numbers: ')
list8 = input('8.Please write down another different numbers: ')
list9 = input('9.Please write down another different numbers: ')
list10 = input('10.Please write down another different numbers: ')

# min part
if list1 < list2 and list1 < list3 and list1 < list4 and list1 < list5 and list1 < list6 \
        and list1 < list7 and list1 < list8 and list1 < list9 and list1 < list10:
    print(list1, 'is the smallest number in this list.')

if list2 < list1 and list2 < list3 and list2 < list4 and list2 < list5 and list2 < list6 \
        and list2 < list7 and list2 < list8 and list2 < list9 and list2 < list10:
    print(list2, 'is the smallest number in this list.')

if list3 < list2 and list3 < list1 and list3 < list4 and list3 < list5 and list3 < list6 \
        and list3 < list7 and list3 < list8 and list3 < list9 and list3 < list10:
    print(list3, 'is the smallest number in this list.')

if list4 < list2 and list4 < list3 and list4 < list1 and list4 < list5 and list4 < list6 \
        and list4 < list7 and list4 < list8 and list4 < list9 and list4 < list10:
    print(list4, 'is the smallest number in this list.')

if list5 < list2 and list5 < list3 and list5 < list4 and list5 < list1 and list5 < list6 \
        and list5 < list7 and list5 < list8 and list5 < list9 and list5 < list10:
    print(list5, 'is the smallest number in this list.')

if list6 < list2 and list6 < list3 and list6 < list4 and list6 < list5 and list6 < list1 \
        and list6 < list7 and list6 < list8 and list6 < list9 and list6 < list10:
    print(list6, 'is the smallest number in this list.')

if list7 < list2 and list7 < list3 and list7 < list4 and list7 < list5 and list7 < list6 \
        and list7 < list1 and list7 < list8 and list7 < list9 and list7 < list10:
    print(list7, 'is the smallest number in this list.')

if list8 < list2 and list8 < list3 and list8 < list4 and list8 < list5 and list8 < list6 \
        and list8 < list7 and list8 < list1 and list8 < list9 and list8 < list10:
    print(list8, 'is the smallest number in this list.')

if list9 < list2 and list9 < list3 and list9 < list4 and list9 < list5 and list9 < list6 \
        and list9 < list7 and list9 < list8 and list9 < list1 and list9 < list10:
    print(list9, 'is the smallest number in this list.')

if list10 < list2 and list10 < list3 and list10 < list4 and list10 < list5 and list10 < list6 \
        and list10 < list7 and list10 < list8 and list10 < list9 and list10 < list1:
    print(list10, 'is the smallest number in this list.')

# max part
if list1 > list2 and list1 > list3 and list1 > list4 and list1 > list5 and list1 > list6 \
        and list1 > list7 and list1 > list8 and list1 > list9 and list1 > list10:
    print(list1, 'is the largest number in this list.')

if list2 > list1 and list2 > list3 and list2 > list4 and list2 > list5 and list2 > list6 \
        and list2 > list7 and list2 > list8 and list2 > list9 and list2 > list10:
    print(list2, 'is the largest number in this list.')

if list3 > list2 and list3 > list1 and list3 > list4 and list3 > list5 and list3 > list6 \
        and list3 > list7 and list3 > list8 and list3 > list9 and list3 > list10:
    print(list3, 'is the largest number in this list.')

if list4 > list2 and list4 > list3 and list4 > list1 and list4 > list5 and list4 > list6 \
        and list4 > list7 and list4 > list8 and list4 > list9 and list4 > list10:
    print(list4, 'is the largest number in this list.')

if list5 > list2 and list5 > list3 and list5 > list4 and list5 > list1 and list5 > list6 \
        and list5 > list7 and list5 > list8 and list5 > list9 and list5 > list10:
    print(list5, 'is the largest number in this list.')

if list6 > list2 and list6 > list3 and list6 > list4 and list6 > list5 and list6 > list1 \
        and list6 > list7 and list6 > list8 and list6 > list9 and list6 > list10:
    print(list6, 'is the largest number in this list.')

if list7 > list2 and list7 > list3 and list7 > list4 and list7 > list5 and list7 > list6 \
        and list7 > list1 and list7 > list8 and list7 > list9 and list7 > list10:
    print(list7, 'is the largest number in this list.')

if list8 > list2 and list8 > list3 and list8 > list4 and list8 > list5 and list8 > list6 \
        and list8 > list7 and list8 > list1 and list8 > list9 and list8 > list10:
    print(list8, 'is the largest number in this list.')

if list9 > list2 and list9 > list3 and list9 > list4 and list9 > list5 and list9 > list6 \
        and list9 > list7 and list9 > list8 and list9 > list1 and list9 > list10:
    print(list9, 'is the largest number in this list.')

if list10 > list2 and list10 > list3 and list10 > list4 and list10 > list5 and list10 > list6 \
        and list10 > list7 and list10 > list8 and list10 > list9 and list10 > list1:
    print(list10, 'is the largest number in this list.')

else:
    print('Error!you wrote two same number!')
