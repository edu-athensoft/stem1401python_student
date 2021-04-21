"""
function:       ok                          5/5
structure:      ok                          1.25/1.25
convention:     ok                          1.25/1.25
comment:        missing                     1.00/1.25
user-friendly:  ok                          1.25/1.25

subtotal:       9.75
"""

import time, datetime
while True:
    now = datetime.datetime.now()
    result = now.strftime('%H:%M:%S')
    print('\r'+result, end='',flush= True)
    time.sleep(1)