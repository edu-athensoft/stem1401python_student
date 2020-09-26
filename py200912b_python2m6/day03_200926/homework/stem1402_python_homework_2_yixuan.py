n = int(input("Input a number："))
formule = dict()
for x in range(1,n+1):
    formule[x]=x * x
print(formule)
print()
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for i in (dic1, dic2, dic3): dic4.update(i)
print(dic4)