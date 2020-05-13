"""
main app
"""

import py200510.day02_py200513.calculator.arithm as arithm
import py200510.day02_py200513.calculator.logic as logic

print("=== My Multi-module Calcaltor ===")

# test functions of arithm
a = 3
b = 6

print(arithm.add(a,b))
print(arithm.sub(a,b))
print(arithm.mul(a,b))
print(arithm.div(a,b))
print(arithm.power(a,b))

# test functions of logic
b1 = True
b2 = False

print(logic.logic_and(b1, b2))
print(logic.logic_or(b1, b2))
print(logic.logic_not(b1))

print("=== End ===")
