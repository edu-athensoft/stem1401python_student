"""
system time
"""

import datetime

t1 = datetime.datetime.now()
print(t1)

t2 = datetime.datetime.now()
print(t2)

print(t2-t1)
print("\n")


#
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S.%f'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime)
theTime = datetime.datetime.now()


for i in range(5000000):
    a = '=' + str(i)+ '='

theTime2 = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print(theTime2)
theTime2 = datetime.datetime.now()

print("time escaped: {}".format(theTime2-theTime))
print("\n")
