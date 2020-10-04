try:
    f = open('homework_text','r')
    x = int(input('Please enter how many last lines you want to read:'))
    content = f.readlines()
    a = content[len(content) - x:]
    for i in a:
        print(i)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()