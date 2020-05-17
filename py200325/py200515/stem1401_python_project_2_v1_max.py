"""
Project 2 V1
"""

# Title
print("{}{:>89}".format("East Repair Inc.", "INVOICE"))

print()

# Address
print('{}'.format("1912 Harvest Lane"))
print('{}'.format("New York, NY 12210"))

print("\n\n\n\n")

# Information
print('{:<35}{:<25}{:>25}{:>20}'.format("Bill To", "Ship To", "Invoice #", "US-001"))
print('{:<35}{:<25}{:>25}{:>20}'.format("John Smith", "John Smith", "Invoice Date", "11/02/2019"))
print('{:<35}{:<25}{:>25}{:>20}'.format("2 Court Square", "3787 Pineview Drive", "P.O.#", "2312/2019"))
print('{:<35}{:<25}{:>25}{:>20}'.format("New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"))

print("\n\n")

# Services
print(' -------------------------------------------------------------------------------------------------------')
print('|{:^9}|{:^49}|{:^18}|{:^24}|'.format("QTY", "DESCRIPTION", "UNIT PRICE", "AMOUNT"))
print('|-------------------------------------------------------------------------------------------------------|')
print('|{:^9}| {:<47} |{:>17} |{:>23} |'.format(1, "Front and rear brake cables", 100.00, 100.00))
print('|-------------------------------------------------------------------------------------------------------|')
print('|{:^9}| {:<47} |{:>17} |{:>23} |'.format(2, "New set of pedal arms", 15.00, 30.00))
print('|-------------------------------------------------------------------------------------------------------|')
print('|{:^9}| {:<47} |{:>17} |{:>23} |'.format(3, "Labor 3hrs", 5.00, 15.00))
print(' -------------------------------------------------------------------------------------------------------|')
print(' {:^9}  {:<47}  {:>17} |{:>23} |'.format("", "", "Subtotal", 145.00))
print(' {:^9}  {:<47}  {:>17} |{:>23} |'.format("", "", "Sales Tax 6.25%", 9.06))
print('                                                                               |------------------------|')
print(' {:^9}  {:<47}  {:>17} |{:>23} |'.format("", "", "TOTAL", "$154.06"))
print('                                                                                ------------------------ ')

print("\n\n\n\n\n\n\n\n")

# Instructions
print('{}'.format("Terms & Conditions"))
print('{}'.format("Payment is due within 15 days"))
print('{}'.format("Please make checks payable to: East Repair Inc."))