"""

"""

import datetime
import time



def t():
    t1 = datetime.datetime.now()
    ts1 = t1.strftime('%Y-%m-%d %H:%M:%S')
    return t1,ts1


def millis(t1, t2):
    micros = (t2 - t1).microseconds
    print("micros: ",micros)
    delta = micros/1000
    return delta


def micros(t1, t2):
    delta = (t2-t1).microseconds
    return delta


def access_log(route_rule, headers, t1, t2, delta, db_delta, api_delta):

    access = {}
    access['route'] = route_rule
    access['headers'] = headers
    access['route_start'] = t1
    access['route_end'] = t2
    access['route_delta'] = delta
    access['db_delta'] = db_delta
    access['api_delta'] = api_delta
    return access


def main():
    t1 = datetime.datetime.now()
    print(t1)

    for i in range(5000000):
        a = '=' + str(i) + '='

    t2 = datetime.datetime.now()
    print(t2)

    print("delta t in ms = {}".format(millis(t1, t2)))


if __name__ == "__main__":
    main()
