# homework 3

# 1
dict = {

}
if dict == {}:
    print("clear")
else:
    print("not clear")

# 2
n = int(input("Input a number:"))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)

# 3
dict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
}

print(min(dict.items()))
print(max(dict.items()))
