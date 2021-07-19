"""
Final Exam

stem1401

Leon

"""
print("{}".format('East Repair Inc.'), "{:>75}".format('INVOICE'))

print("{}".format('1912 Harvest Lane'))

print("{}".format('New York, NY 12210'))
print()

print("{:<30}".format('Bill To'), "{:^15}".format('Ship To'), "{:>30}".format('Invoice #'), "{:>14}".format('US-001'))

print("{:<30}".format('John Smith'), "{:^18}".format('John Smith'), "{:>27}".format('Invoice Date'),
      "{:>14}".format('11/02/2019'))

print("{:<18}".format('2 Court Square'), "{:^52}".format('3787 Pineview Drive'), "{:>5}".format('P.O.#'),
      "{:>14}".format('2312/2019'))

print("{:<30}".format('New York, NY 12210'), "{:^28}".format('Cambridge, MA 12210'), "{:>17}".format('Due Date'),
      "{:>14}".format('26/02/2019'))
print()

print("{:<10}".format('QTY'), "{:}".format('DESCRIPTION'), "{:>35}".format('UNIT PRICE'), "{:>23}".format('AMOUNT'))

print("{:<5}".format('1'), "{:}".format('Front and rear brake cables'), "{:>26}".format('100.00'), "{:>26}".format('100.00'))

print("{:<5}".format('2'), "{:}".format('New set of pedal arms'), "{:>32}".format('15.00'), "{:>26}".format('30.00'))

print("{:<5}".format('3'), "{:}".format('Labor 3hrs'), "{:>43}".format('5.00'), "{:>26}".format('15.00'))

print("{:>60}".format('Subtotal'), "{:>26}".format('145.00'))

print("{:>60}".format('Sales Tax 6.25%'), "{:>26}".format('9.06'))

print("{:>60}".format('TOTAL'), "{:>26}".format('$154.06'))

print()
print("{:}".format('Terms & Conditions'))
print("{:}".format('Payment is due within 15 days'))
print()
print("{:}".format('Please make checks payable to: East Repair Inc.'))

