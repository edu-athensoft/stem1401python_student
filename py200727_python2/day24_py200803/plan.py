"""
plan

step1. choose a data structure to represent the data of the statement

step2. calculate the balance and find a way using loop

step3. output the financial statement with determined balance

"""


print("=== Financial Statement ===")
print("Company:  XYZ Inc.")
print("Period:   Jan-2020")
print("Date:  August-3-2020")

# step 1.

# 2019
forward_balance = 1000.0

# DATE,ENTITY,WITHDRAW,DEPOSIT,BALANCE
trans = [['2020-01-01','PROJECT MMM',0, 2000.00, 0],
         ['2020-01-05','RV QC  QST',0, 200.00, 0],
         ['2020-01-10','CANADA GST',0, 500.00, 0],
         ['2020-01-15','ROGERS',70.00, 0, 0],
         ['2020-01-20','RENTAL XYZ',1000.00, 0, 0],
         ['2020-01-25','INTEREST SURCHARGE',10.00, 0, 0],
         ['2020-01-30','SERVICE FEE',5.00, 0, 0]]
print()
print("=== Original data ===")
print(f"forward_balance = {forward_balance}")
print(trans)
print()

# step 2.
# trail calculation
# print(trans[0])

for record in trans:
    forward_balance = forward_balance+record[3]-record[2]
    record[4] = forward_balance
    print(forward_balance)
    print(record)
    print()

# step 3.
# reverse all records, and design the layout
# print(trans)
for i in range(6,-1,-1):
    print(trans[i])
print()
print()

"""
[Demo] Financial Statement
Data for Jan. 2020		ABC Bank  for company XYZ Inc.

DATE		ENTITY				WITHDRAW	DEPOSIT	BALANCE
2020-01-30	SERVICE FEE			   5.00				?
2020-01-25	INTEREST SURCHARGE	  10.00				?
2020-01-20	RENTAL XYZ			1000.00			    ?
2020-01-15	ROGERS				  70.00				?
2020-01-10	CANADA GST					    500.00	?
2020-01-05	RV QC  QST						200.00	?
2020-01-01  PROJECT MMM				       2000.00	?
forward from 2019									1000.00
"""
print()
# print(trans[0])
strtemp = "{date:^14}{entity:^20}{withdraw:^10}{deposit:^10}{balance:^10}"

print(strtemp.format(date='DATE',entity='ENTITY',withdraw='WITHDRAW',deposit='DEPOSIT',balance='BALANCE'))

strtemp = "{date:14}{entity:20}{withdraw:10}{deposit:10}{balance:10}"
for i in range(6,-1,-1):
    print(strtemp.format(date=trans[i][0],entity=trans[i][1],withdraw=trans[i][2],deposit=trans[i][3],balance=trans[i][4]))



# forward_balance = forward_balance+trans[1][3]-trans[1][2]
# trans[1][4] = forward_balance
# print(forward_balance)
# print(trans[1])
# print()
#
# forward_balance = forward_balance+trans[2][3]-trans[2][2]
# trans[2][4] = forward_balance
# print(forward_balance)
# print(trans[2])
# print()
#
# forward_balance = forward_balance+trans[3][3]-trans[3][2]
# trans[3][4] = forward_balance
# print(forward_balance)
# print(trans[3])


# step 3.


