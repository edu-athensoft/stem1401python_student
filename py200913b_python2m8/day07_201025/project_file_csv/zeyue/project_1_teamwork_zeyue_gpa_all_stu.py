"""
Calculate the GPA for every student and print out the report properly
export as a text file
"""

try:
    csvfile1 = open("File_CSV_1.csv")
    csvfile2 = open("File_CSV_2.csv")
    csvfile3 = open(r"C:\Users\Li\PycharmProjects\stem1401python\py201011\File_CSV_3.csv")
    stugpas = open("studentGPAs.txt", "w")
    content = csvfile1.readlines() + csvfile2.readlines() + csvfile3.readlines()
    split_content = []
    gpas = []
    for i in range(len(content)):
        content[i] = content[i].split(",")
        for j in content[i]:
            if content[i][-1] == j:
                gpas.append(j[:-1])
    for i in range(len(gpas)-1):
        try:
            gpas[i] = float(gpas[i])
        except Exception as e:
            gpas.pop(i)
    print(gpas)
    sum = 0
    for i in gpas:
        try:
            sum += i
        except Exception as e:
            print(e)
    average = sum / len(gpas)
    for i in gpas:
        stugpas.write(str(i))
        stugpas.write("\n")
    stugpas.write(f"The average GPA is {average}")
except Exception as e:
    print(e)
finally:
    csvfile1.close()
    csvfile2.close()
    csvfile3.close()
