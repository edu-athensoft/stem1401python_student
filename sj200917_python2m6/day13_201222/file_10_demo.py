"""
analyze based on data file(s)
"""

try:
    # step 1.
    file = open('file_9.txt')

    # step 2.
    data = file.readlines()

    num = len(data)
    print(f"There are {num} of records in total.")

    cust1 = []

    for record in data:
        print(record)
        line = record.split(',')
        print(line)

        if line[1] == 'c001':
            cust1.append(line)

    # output data of cust1
    print(cust1)

    # step 3.
    file.close()

except FileExistsError as fe:
    print(fe)

except Exception as e:
    print(e)