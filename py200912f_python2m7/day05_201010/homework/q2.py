# 2.
names = {'Amy': (22, 92),
         'Lily': (24, 100),
         'Sandy': (21, 87),
         'Peter': (23, 96),
         'Jack': (22, 94)}

names2 = dict(sorted(names.items(), key=lambda x: x[1][0]))
print(names2)

names3 = dict(sorted(names.items(), key=lambda x: x[1][1], reverse=True))
print(names3)