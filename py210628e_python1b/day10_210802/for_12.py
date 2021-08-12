"""
[Demo] Application of For loop in Financial Statement
Company ABC Inc.
Data for Jan. 2020		at ABC Bank

DATE		ENTITY				WITHDRAW	DEPOSIT	BALANCE
2020-01-30	SERVICE FEE			 5.00				?
2020-01-25	INTEREST SURCHARGE	10.00			    ?
2020-01-20	RENTAL XYZ		  1000.00			    ?
2020-01-15	ROGERS				70.00				?
2020-01-10	CANADA GST						500.00	?
2020-01-05	RV QC  QST						200.00	?
2020-01-01  PROJECT MMM					   2000.00	?
forward from 2019									1000.00
"""

"""
Analysis

concept:
transaction :  a deposit or a withdraw

for loop?
balance = 1000
1st. balance = balance + deposit_1
2nd. balance = balance + deposit_2
3rd. balance = balance + deposit_3
4th. balance = balance - withdraw_4
5th. balance = balance - withdraw_5
6th. balance = balance - withdraw_6
7th. balance = balance - withdraw_7

balance = 1000
1st. balance = balance + trans_1
2nd. balance = balance + trans_2
3rd. balance = balance + trans_3
4th. balance = balance + trans_4
5th. balance = balance + trans_5
6th. balance = balance + trans_6
7th. balance = balance + trans_7

pattern
balance = balance + trans_i
i = 0 to 6

"""

