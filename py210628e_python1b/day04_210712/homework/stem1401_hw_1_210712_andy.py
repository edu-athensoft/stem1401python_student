"""
[Homework]
Date: 2021-07-08
Rewrite the INVOICE printing program
Section 3 and 4
Due date: Before 2021-07-12 Mon.
Notes: Submit a full version of your program
"""


# section 1
company = 'East Repair Inc.'
doc_title = 'INVOICE'
address1 = '1912 Harvest Lane'
address2 = 'New York, NY 12210'

# line #1 = 70 chars + 10 chars
line1 = '{:70}{:>10}'.format(company, doc_title)
line = ''
line3 = '{:80}'.format(address1)
line4 = '{:80}'.format(address2)

print(line1)
print(line)
print(line3)
print(line4)
print(line)
print(line)
print(line)
print(line)

# section 2
# section 2-1
bill_to = 'Bill To'
bill_to_name = 'John Smith'
bill_to_address1 = '2 Court Square'
bill_to_address2 = 'New York, NY 12210'

# section 2-2
ship_to = 'Ship To'
ship_to_name = 'John Smith'
ship_to_address1 = '3787 Pineview Drive'
ship_to_address2 = 'Cambridge,MA 12210'

# section 2-3
title_invoice_no = 'Invoice #'
title_invoice_date = 'Invoice Date'
title_po_no = 'P.O.#'
title_due_date = 'Due Date'

# section 2-4
value_invoice_no = 'US-001'
value_invoice_date = '11/02/2019'
value_po_no = '2313/2019'
value_due_date = '26/02/2019'

# contents of section 2
template2 = '{:20}{:25}{:>23}{:>12}'
line1 = template2.format(bill_to, ship_to, title_invoice_no, value_invoice_no)
line = template2.format(bill_to_name, ship_to_name, title_invoice_date, value_invoice_date)
line3 = template2.format(bill_to_address1, ship_to_address1, title_po_no, value_po_no)
line4 = template2.format(bill_to_address2, ship_to_address2, title_due_date, value_due_date)
line5 = ''

print(line1)
print(line)
print(line3)
print(line4)
print(line5)
print(line5)

# section 3
title_1 = 'QTY'
tile_desc = 'DESCRIPTION'
title_unit_price = 'UNIT PRICE'
title_amount = 'AMOUNT'

item1_QTY = 1
item1_DESCRIPTION = 'Front and rear brake cables'
item1_UNIT_PRICE = 100.00
item1_AMOUNT = 100.00

item2_QTY = 2
item2_DESCRIPTION = 'New set of pedal arms'
item2_UNIT_PRICE = 15.00
item2_AMOUNT = 30.00

item3_QTY = 3
item3_DESCRIPTION = 'Labor 3hrs'
item3_UNIT_PRICE = 5.00
item3_AMOUNT = 15.00

title_subtotal = 'Subtotal'
title_sales_tax = 'Sales Tax 6.25%'
title_total = 'TOTAL'
subtotal = item1_AMOUNT + item2_AMOUNT + item3_AMOUNT
TAX_RATE = 6.25 * 0.01
tax_amount = subtotal * TAX_RATE
total = subtotal + tax_amount

template3a = '{:5}{:40}{:15}{:20}'
template3b = '{:<5}{:40}{:10}{:20}'
template3c = '{:>55}{:20}'

line1 = template3a.format(title_1, tile_desc, title_unit_price, title_amount)
line2 = template3b.format(item1_QTY, item1_DESCRIPTION, item1_UNIT_PRICE, item1_AMOUNT)
line3 = template3b.format(item2_QTY, item2_DESCRIPTION, item2_UNIT_PRICE, item2_AMOUNT)
line4 = template3b.format(item3_QTY, item3_DESCRIPTION, item3_UNIT_PRICE, item3_AMOUNT)
line5 = template3c.format(title_subtotal, subtotal)
line6 = template3c.format(title_sales_tax, tax_amount)
line7 = template3c.format(title_total, total)
line8 = ''

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)
print(line8)
print(line8)
print(line8)

# section 4
title_TC = 'Terms & Conditions'
payment_due_date = 'Payment is due within 15 days'
payable_to = 'Please make checks payable to: East Repair Inc'

print(title_TC)
print(payment_due_date)
print()
print(payable_to)
