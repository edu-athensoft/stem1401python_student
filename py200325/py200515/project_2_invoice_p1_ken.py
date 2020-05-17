"""
For May 15th, 2020.
Project 2, Part 1.
Invoice formatting.
"""


# Company and Subject.
print("|{:<55}{:>55}|".format("East Repair Inc.", "INVOICE"))


# White space.
print("|{:<110}|\n".format("")*2, end="")

# Address company.
print("|{:<110}|".format("1912 Harvest Lane"))
print("|{:<110}|".format("New York, NY 12210"))

# White space.
print("|{:<110}|\n".format("")*5, end="")

# Bill To. Ship To. Invoice #. US-001
print("|{:<40}{:<40}{:>15}{:>15}|".format("Bill To","Ship To","Invoice #","US-001"))

# Details Bill To and Ship To. Invoice Date.
print("|{:<40}{:<40}{:>15}{:>15}|".format("John Smith","John Smith","Invoice Date","11/02/2019"))

# Details Bill To and Ship To. P.O.#.
print("|{:<40}{:<40}{:>15}{:>15}|".format("2 Court Square","3787 Pineview Drive","P.O.#","23/12/2019"))

# Details Bill To and Ship To. Due Date.
print("|{:<40}{:<40}{:>15}{:>15}|".format("New York, NY 12210","Cambridge, MA 12210","Due Date","26/02/2019"))

# White space.
print("|{:<110}|\n".format("")*3, end="")

# Table : Titles.
print("|{:^8}|{:^57}|{:^16}|{:^26}|".format("QTY","DESCRIPTION","UNIT PRICE","AMOUNT"))

# Table : Row 1.
print("|{:^8}|{:<57}|{:>16}|{:>26}|".format("1"," Front and rear brake cables","100.00 ","100.00 "))

# Table : Row 2.
print("|{:^8}|{:<57}|{:>16}|{:>26}|".format("2"," New set of pedal arms","15.00 ","30.00 "))

# Table : Row 3.
print("|{:^8}|{:<57}|{:>16}|{:>26}|".format("3"," labor 3hrs","5.00 ","15.00 "))

# Table : Subtotal.
print("|{:^8}{:<58}{:>17}|{:>26}|".format("", "", "Subtotal ","145.00 "))

# Table : Sales Tax 6.25%.
print("|{:^8}{:<58}{:>17}|{:>26}|".format("", "", "Sales Tax 6.25% ","9.06 "))

# Table : TOTAL.
print("|{:^8}{:<58}{:>17}|{:>26}|".format("", "", "TOTAL ","$154.06 "))

# White space.
print("|{:<110}|\n".format("")*15, end="")

# Terms & Conditions : Title.
print("|{:<110}|".format("Terms & Conditions"))

# Terms & Conditions : Details.
print("|{:<110}|".format("Payment is due within 15 days"))

# White space.
print("|{:<110}|\n".format("")*2, end="")

# Terms & Conditions : Check payability.
print("|{:<110}|".format("Please make checks payable to: East Repair Inc."))