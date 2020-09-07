"""
project 2
version: 2.0

how to choose to use variable?
"""

# sec1. heading
print('{:_^80}'.format(''))
company_name = 'East Repair Inc.'
print('{:<73}Invoice'.format(company_name))
print()
company_address = ('1912 Harvest Lane', 'New York, NY 12210')
print(company_address[0])
print(company_address[1])

# print('', '', '', sep='\n')
print("\n\n")

# sec2. basic info. of invoice
invoice_number = 'US-001'
client_name = 'John Smith'
invoice_date = '11/02/2019'
bill_address = ('2 Court Square', 'New York,NY 12210')
ship_address = ('3787 Pineview Drive', 'Cambridge,MA 12210')
PO_number = '2312/2019'
due_date = '26/02/2019'

strtemp2 = '{:25}{:20}{:>20}{:>15}'
print(strtemp2.format('Bill To', 'Ship To', 'Invoice #', invoice_number))
print(strtemp2.format(client_name, client_name, 'Invoice Date', invoice_date))
print(strtemp2.format(bill_address[0], ship_address[0], 'P.O.#', PO_number))
print(strtemp2.format(bill_address[1], ship_address[1], 'Due Date', due_date))

# print('', '', sep='\n')
print("\n")

# sec3. dataset of entries
"""
qty_item1 = 1
item1 = 'Front and rear brake cables'
price_item1 = 100
total_item1 = qty_item1*price_item1

qty_item2 = 2
item2 = 'New set of pedal arms'
price_item2 = 15
total_item2 = qty_item2*price_item2

qty_item3 = 3
item3 = 'Labor 3hrs'
price_item3 = 5
total_item3 = qty_item3*price_item3
"""

items =[
    [1, 'Front and rear brake cables', 100],
    [2, 'New set of pedal arms', 15],
    [3, 'Labor 3hrs', 5]
]


strtemp3a = '|{:^7}|{:^34}|{:^16}|{:^18}|'
strtemp3b = '|{:^7}|{:<34}|{:>16.2f}|{:>18.2f}|'
strtemp3c = '{:_^80}'
strtemp3d = '{:-^80}'

print(strtemp3c.format(''))
print(strtemp3a.format('QTY', 'DESCRIPTION', 'UNIT PRICE', 'AMOUNT'))
print(strtemp3d.format(''))
print(strtemp3b.format(items[0][0], items[0][1], items[0][2], items[0][0]*items[0][2]))
print(strtemp3d.format(''))
print(strtemp3b.format(items[1][0], items[1][1], items[1][2], items[1][0]*items[1][2]))
print(strtemp3d.format(''))
print(strtemp3b.format(items[2][0], items[2][1], items[2][2], items[2][0]*items[2][2]))
print(strtemp3d.format(''))

# sec4. summary
subtotal = items[0][0]*items[0][2]+items[1][0]*items[1][2]+items[2][0]*items[2][2]
sales_tax = subtotal*0.0625
total = subtotal+sales_tax

strtemp4a = '{:44}{:>16}|{:>18.2f}|'
strtemp4b = '{:60}|{:-^18}|'
strtemp4c = '{:44}{:>16}|{:>12}{:>.2f}|'
print(strtemp4a.format('', 'Subtotal', subtotal))
print(strtemp4a.format('', 'Sales Tax 6.25%', sales_tax))
print(strtemp4b.format('',''))
print(strtemp4c.format('', 'Total', '$', total))

# print('', '', sep='\n')
print("\n")

# footer
print('Terms & Conditions')
print('Payment is due within 15 days')
print()
print('Please make checks payable to: {}'.format(company_name))