"""
Project 2 version 1
"""

print()
# Title
print("{:<21} {:>59}".format("East Repair Inc.", "INVOICE"))
print()
# Location
print("{:<25}".format("1912 Harvest Lane"))
print("{:<25}".format("New York, NY 12210"))
print()
print()
print()
# Information
print("{:<25} {:<20} {:>20} {:>13}".format("Bill To", "Ship To", "Invoice #", "US-001"))
print("{:<25} {:<20} {:>20} {:>13}".format("John Smith", "John Smith", "Invoice Date", "11/02/2019"))
print("{:<25} {:<20} {:>20} {:>13}".format("2 Court Square", "3787 Pineview Drive", "P.O.#", "2312/2019"))
print("{:<25} {:<20} {:>20} {:>13}".format("New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"))
print()
print()
# Cost
print("{:^5} {:^35} {:^15} {:^23}".format("QTY", "DESCRIPTION", "UNIT PRICE", "AMOUNT"))
print("{:^5} {:<35} {:>15} {:>20}".format("1", "Front and rear brake cables", "100.00", "100.00"))
print("{:^5} {:<35} {:>15} {:>20}".format("2", "New set of pedal arms", "15.00", "30.00"))
print("{:^5} {:<35} {:>15} {:>20}".format("3", "Labor3hrs", "5.00", "15.00"))
print("{:>57} {:>20}".format("Subtotal", "145.00"))
print("{:>57} {:>20}".format("Sales Tax 6.25%", "9.06"))
print("{:>57} {:>20}".format("Total", "154.06"))
print()
print()
print()
print()
# Instructions
print("{:<25}".format("Terms & Conditions"))
print("{:<25}".format("Payment is due within 15 days"))
print("{:<25}".format("Please make checks payable to: East Repair Inc."))