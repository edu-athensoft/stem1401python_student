"""
mainapp - reload using module: imp.reload(module_name)

deprecated, not recommended
"""

print("=== Test Game ===")
print("--- main game app ---")

import py200421.day06_py200509.gamelevel
import py200421.day06_py200509.gamelevel as gamelevel

import imp
imp.reload(gamelevel)

print("=== end of main game app ===")


