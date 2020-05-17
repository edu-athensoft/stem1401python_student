"""
Project 2 V1
/Users/kevinteng/PycharmProjects/stem1401python/py200513/project_2/stem1401_python_project_2_v2_Kevin.py
"""

# name and address
company_name = "East Repair Inc."
print("{:<}{:>74}".format("East Repair Inc.", "INVOICE"))

print()

print("{:<}".format("1912 Harvest Lane \nNew York, NY 12210"))

print("\n\n\n")

# Bill TO, Ship TO, Invoice #, Invoice Date, P.O.# and Due Date
print("{:<30}{:<25}{:>20}{:>15}".format("Bill To", "Ship To", "Invoice #", "US-001"))
print("{:<30}{:<25}{:>20}{:>15}".format("John Smith", "John Smith", "Invoice Date", "11/02/2019"))
print("{:<30}{:<25}{:>20}{:>15}".format("2 Court Square", "3787 Pineview Drive", "P.O.#", "2312/2019"))
print("{:<30}{:<25}{:>20}{:>15}".format("New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"))

# The table
print("\n")

# first line
print("{:^7} {:^34} {:^20} {:^26}".format("QTY", "DESCRIPTION", "UNITE PRICE", "AMOUNT"))

# des_1
qty_1 = 1
des_1 = "Front and real brake cables"
unit_price_1 = 100.00
amount_1 = unit_price_1 * qty_1

print("{:^7} {:<34} {:>20.2f} {:>26.2f}".format(qty_1, des_1, unit_price_1, amount_1))

# des_2
qty_2 = 2
des_2 = "New set of pedal arms "
unit_price_2 = 15.00

amount_2 = unit_price_2 * qty_2
print("{:^7} {:<34} {:>20.2f} {:>26.2f}".format(qty_2, des_2, unit_price_2, amount_2))

# des_3
qty_3 = 3
des_3 = "Labor 3hrs"
unit_price_3 = 5.00
amount_3 = unit_price_3 * qty_3
print("{:^7} {:<34} {:>20.2f} {:>26.2f}".format(qty_3, des_3, unit_price_3, amount_3))


# Tax and Subtotal
subtotal = amount_1 + amount_2 + amount_3
print("{:>63}{:>27.2f}".format("Subtotal", subtotal))

tax = subtotal * 0.0625
print("{:>63}{:>27.2f}".format("Sales Tax 6.25%", tax))

# Total
total = subtotal * 1.0625
print("{:>63}{:>27.2f}".format("TOTAL", total))



# terms & conditions
print("\n\n\n\n\n\n\n")

print("Terms & Conditions")
print("Payment is due within 15 days")

print()

print("Please make checks payable to: East Repair Inc.")








