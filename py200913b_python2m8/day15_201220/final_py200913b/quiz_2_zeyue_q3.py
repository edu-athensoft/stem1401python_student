"""
3. Text Clock (10')
Description
Write a program to show time ticks like an electronic clock.
The time should change every one second.
Only one string of current time displays and refreshes.
"""

"""
function:       ok                          5/5
structure:      ok                          1.25/1.25
convention:     ok                          1.25/1.25
comment:        missing                     1.00/1.25
user-friendly:  ok                          1.25/1.25

subtotal:       9.75
"""

import datetime
import time as t

INTERVAL = 1

while True:
    print(f"\r{datetime.datetime.now().strftime('%H:%M:%S')}", end="", flush=True)
    t.sleep(INTERVAL)