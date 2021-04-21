"""
writelines()

readlines()
"""


try:
    file = open("text19.txt",'w')
    content = ['line 1.aksdfasdf\n','line 2.alsdfkasfdasl\n','line 3. alkjfasjfasdf\n']
    file.writelines(content)
# except FileNotFoundError as fe:
#     print(fe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)

finally:
    file.close()



with open("text19.txt", 'w') as file:
    content = ['line 1.aksdfasdf\n', 'line 2.alsdfkasfdasl\n', 'line 3. alkjfasjfasdf\n']
    file.writelines(content)