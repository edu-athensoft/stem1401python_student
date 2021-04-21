"""
q1
"""
from datetime import datetime
time = datetime.now()

print('year:',time.strftime('%Y'))
print('month:',time.strftime('%m'))
print('month:',time.strftime('%B'))
print('month:',time.strftime('%b'))
print('day:', time.strftime('%d'))
print('time:',time.strftime('%H:%M:%S'))
print('date and time',time.strftime('%d/%m/%Y, %H:%M:%S'))
print('date and time',time.strftime('%Y-%b-%d, %H:%M:%S'))
