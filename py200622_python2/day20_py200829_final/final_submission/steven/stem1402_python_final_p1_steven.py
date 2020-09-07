def freq(str):
    str = str.split()
    str2 = []
    b = '''!()-[]{};:'"\,<>./?@#$%^&*_~... '''
    a = 'a,an,was,is,the,are,were,been,of,and,with'
    for i in str:
            if i not in a:
                if i not in b:
                    if not i.isdigit():
                        str2.append(i)
    total = 0
    for j in str:
        total += 1
    for i in range(0, len(str2)):
        counter = str.count(str2[i])
        print('Frequency of', str2[i], 'is', counter,"/", total)
str = input("Please enter something:")
freq(str)