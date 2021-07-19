
# section 1
company = 'East Repair Inc.'
doc_title = 'INVOICE'
address1 = '1912 Harvest Lane'
address2 = 'New York, NY 12210'

# line #1 = 70 chars + 10 chars
line1 = '{:70}{:>10}'.format(company, doc_title)
line2 = ''
line3 = '{:80}'.format(address1)
line4 = '{:80}'.format(address2)

print(line1)
print(line2)
print(line3)
print(line4)
print(line2)
print(line2)
print(line2)
print(line2)

# section 2
# section 2-1
bill_to = 'Bill To'
bill_to_name = 'John Smith'
bill_to_address1 = '2 Court Square'
bill_to_address2 = 'New York, NY 12210'

# section 2-2
ship_to = 'Bill To'
ship_to_name = 'John Smith'
ship_to_address1 = '2 Court Square'
ship_to_address2 = 'New York, NY 12210'

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
line1 = template2.format(bill_to, bill_to_name, bill_to_address1, bill_to_address2)
line2 = template2.format(ship_to, ship_to_name, ship_to_address1, ship_to_address2)
line3 = template2.format(title_invoice_no, title_invoice_date, title_po_no, title_due_date)
line4 = template2.format(value_invoice_no, value_invoice_date, value_po_no, value_due_date)

print(line1)
print(line2)
print(line3)
print(line4)
print()
