try:
    f = open('homework_text','a+')
    content = 'read the next newspaper if u want to know what will happen... '
    f.write(content)
    print(content)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()