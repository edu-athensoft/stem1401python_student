"""
project_2_steven
"""

print("{:} {:>78}".format("East Repair Inc.", "INVOICE"))

print()

print("{:}".format("1912 Harvest Lane"))
print("{:}".format("New York, NY 12210"))

print()
print()

print("{:} {:>32} {:>37} {:>16}".format("Bill to", "Ship to", "Invoice#", "US-001"))
print("{:} {:>32} {:>34} {:>16}".format("John Smith", "John Smith", "Invoice Date", "11/02/2019"))
print("{:} {:>37} {:>25} {:>16}".format("2 Court Square", "3787 Pineview Drive", "P.O.#", "2312/2019"))
print("{:} {:>33} {:>25} {:>16}".format("New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"))

print()
print()

print("{:^6} {:^48} {:^2} {:^32}".format("QTY", "DESCRIPTION", "UNIT PRICE", "AMOUNT"))

print("{:^6} {:} {:>32} {:>26}".format("1", "Front and rear brake cables", "100.00", "100.00"))
print("{:^6} {:} {:>38} {:>26}".format("2", "New set of pedal arms", "15.00", "30.00"))
print("{:^6} {:} {:>49} {:>26}".format("3", "Labor 3hrs", "5.00", "15.00"))

print("{:>67} {:>26}".format("Subtotal", "145.00"))
print("{:>67} {:>26}".format("Sales Tax 6.25%", "9.06"))
print("{:>67} {:>26}".format("TOTAL", "$154.06"))

print()
print()
print()
print()
print()
print()

print("Terms & Conditions")
print("Payment is due within 15 days")
print()
print("Please make checks payable to: East Repair Inc.")