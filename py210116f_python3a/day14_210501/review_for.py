"""
nested for-loop

(row,column)
row = 0..32
column = 0..14
"""

total = 0

for col in range(0, 15):
    for row in range(0, 33):
        total = col * 32 + row
        if total > 479:
            break
        print(f'({row}, {col})')
    print()



