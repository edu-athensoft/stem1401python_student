"""
main app
desc:   entrance of the program
date:   2020-05-05
author: Athens
"""

import py200421.day05_py200505.globalvar as globalvar
import py200421.day05_py200505.settingutil as settingutil

print("=== Main App ===")

print("Print out the initial values of global variables")
print("Show global variable: counter = {}".format(globalvar.counter))
print("Show global variable: summary = {}".format(globalvar.summary))
print("Show global variable: product = {}".format(globalvar.product))

# user input
globalvar.counter = int(input("input an integer for counter: "))
globalvar.summary = int(input("input an integer for summary: "))
globalvar.product = int(input("input an integer for product: "))
s = settingutil.doublesum(int(input("input an integer for x")))

# the latest values
print("Print out the latest values of global variables")
print("Show global variable: counter = {}".format(globalvar.counter))
print("Show global variable: summary = {}".format(globalvar.summary))
print("Show global variable: product = {}".format(globalvar.product))
print("Show double summary:  = {}".format(s))

# settingutil
# print(settingutil.doublesum(globalvar.summary))

print("=== End ===")