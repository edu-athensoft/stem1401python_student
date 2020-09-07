result1 = [["Robert Master", 220, 340],
           ["Montreal Sprite", 320, 270],
           ["Smart Maker", 115, 405],
           ["Nova Robert", 450, 380],
           ["10 Stars", 100, 330]]


r = []
for i in range(len(result1)):
    if result1[i][1] > result1[i][2]:
        r.append(result1[i][1])

    elif result1[i][1] < result1[i][2]:
        r.append(result1[i][2])
    else:
        print("Error")
r.sort(reverse=True)
print(r)

if r[0] in result1[0]:
    print("No. 1 is Robert Master")
if r[0] in result1[1]:
    print("No. 1 is Montreal Sprite")
if r[0] in result1[2]:
    print("No. 1 is Smart Maker")
if r[0] in result1[3]:
    print("No. 1 is Nova Robert")
if r[0] in result1[4]:
    print("No. 1 is 10 Stars")

if r[1] in result1[0]:
    print("No. 2 is Robert Master")
if r[1] in result1[1]:
    print("No. 2 is Montreal Sprite")
if r[1] in result1[2]:
    print("No. 2 is Smart Maker")
if r[1] in result1[3]:
    print("No. 2 is Nova Robert")
if r[1] in result1[4]:
    print("No. 2 is 10 Stars")

if r[2] in result1[0]:
    print("No. 3 is Robert Master")
if r[2] in result1[1]:
    print("No. 3 is Montreal Sprite")
if r[2] in result1[2]:
    print("No. 3 is Smart Maker")
if r[2] in result1[3]:
    print("No. 3 is Nova Robert")
if r[2] in result1[4]:
    print("No. 3 is 10 Stars")

if r[3] in result1[0]:
    print("No. 4 is Robert Master")
if r[3] in result1[1]:
    print("No. 4 is Montreal Sprite")
if r[3] in result1[2]:
    print("No. 4 is Smart Maker")
if r[3] in result1[3]:
    print("No. 4 is Nova Robert")
if r[3] in result1[4]:
    print("No. 4 is 10 Stars")

if r[4] in result1[0]:
    print("No. 5 is Robert Master")
if r[4] in result1[1]:
    print("No. 5 is Montreal Sprite")
if r[4] in result1[2]:
    print("No. 5 is Smart Maker")
if r[4] in result1[3]:
    print("No. 5 is Nova Robert")
if r[4] in result1[4]:
    print("No. 5 is 10 Stars")
