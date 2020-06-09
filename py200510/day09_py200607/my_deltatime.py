"""
delta t
"""


import datetime
access_start = datetime.datetime.now()
access_start_str = access_start.strftime('%Y-%m-%d %H:%M:%S')

access_end = datetime.datetime.now()
access_end_str = access_end.strftime('%Y-%m-%d %H:%M:%S')

access_delta = (access_end-access_start).seconds*1000

print(access_delta)