print("================== Start of the module ======================")
print(' 1. Arithmetic operators \n 2. Logical operators')
a = int(input('Please enter the number before the option you want:'))
while a != 1 and a != 2:
    a = int(input('Please enter a valid number:'))
if a == 1:
 print(' 1.add \n 2.substract \n 3.multiply \n 4.divise \n 5.power')
 x = int(input('Please enter the number before the option you want:'))
 while x != 1 and x != 2 and x != 3 and x != 4 and x!= 5:
    x = int(input('Please enter a valid number:'))
 if x == 1:
  import py200513.calculator.mod_1_adding
 elif x == 2:
  import py200513.calculator.mod_2_substract
 elif x == 3:
    import py200513.calculator.mod_3_multiply
 elif x == 4:
    import py200513.calculator.mod_4_division
 elif x == 5:
  import py200513.calculator.mod_5_power
if a == 2:
    print(' 1.and \n 2.or \n 3.not ')
    y = int(input('Please enter the number before the option you want:'))
    while y != 1 and y != 2 and y != 3:
        y = int(input('Please enter a valid number:'))
    if y == 1:
        import py200513.calculator.mod_6_logical_operator_AND
    elif y == 2:
        import py200513.calculator.mod_7_logical_operator_OR
    elif y == 3:
        import py200513.calculator.mod_8_logical_operator_NOT

print('==================== End of the module ======================')



