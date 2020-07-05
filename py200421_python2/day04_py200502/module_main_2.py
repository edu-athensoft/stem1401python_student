"""
main module

import
as

alias
"""

import py200421.day04_py200502.module_arithmetic as arith
import py200421.day04_py200502.module_logic as logic


print("=== main module ===")

print("Test arithmetic operation")
print(arith.add(1, 2))

print(arith.sub(1, 2))

print(arith.mul(2, 3))

print(arith.div(2, 3))

print("Test logic operation")
print(logic.logic_and(True, False))
print(logic.logic_or(True, False))
print(logic.logic_not(True))
print(logic.logic_not(False))

print("==== end main ===")
