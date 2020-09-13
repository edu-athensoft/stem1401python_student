"""
multi-module program
"""

import sj200116.py200521.calculator.arithmetic as arith
import sj200116.py200521.calculator.logic as logic

# arithmetic operation
# add
print(arith.add(1, 2))
# sub
print(arith.sub(1, 2))
# mul
print(arith.mul(1, 2))
# div
print(arith.div(1, 2))
# modulus
print(arith.mod(3, 2))
# power
print(arith.power(3, 2))


# logic operation
bool1 = True
bool2 = False
# logic_and
print(logic.logic_and(bool1, bool2))
# logic_or
print(logic.logic_or(bool1, bool2))
# logic_not
print(logic.logic_not(bool1))
print(logic.logic_not(bool2))


# print(bool1 and bool2)





