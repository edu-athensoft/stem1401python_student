"""
mainapp - reload using module: imp.reload(module_name)

deprecated, not recommended
"""

print("=== Test Game ===")
print("--- main game app ---")

import py200421.day06_py200509.gamelevel
print("    loaded for 1st time")
print()

import py200421.day06_py200509.gamelevel as gamelevel

import importlib
importlib.reload(gamelevel)
print("    loaded for 2nd time")

print("=== end of main game app ===")


