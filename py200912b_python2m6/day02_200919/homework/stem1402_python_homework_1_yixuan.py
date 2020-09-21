"""
yixuan
"""
# dict = {
seasons = {
    "spring": "3、4、5月",
    "summer": "6、7、8月",
    "fall"  : "9、10、11月",
    "winter": "12、1、2月"
}

print("spring:{}".format(seasons["spring"]))
print("summer:{}".format(seasons["summer"]))
print("fall:{}".format(seasons["fall"]))
print("winter:{}".format(seasons["winter"]))


Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},
         'Dict2': {'name': 'Bob', 'age': '25'}
}
del Dict['Dict2']
print(Dict)

print(Dict['Dict1'])
print(Dict['Dict2'])

Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},
         'Dict2': {'name': 'Bob', 'age': '25'}
}
del Dict['Dict1']
print(Dict)