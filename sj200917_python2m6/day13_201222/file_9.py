"""
file output

writelines()
v.s. readlines()

"""


try:
    # step 1.
    file = open('file_9.txt','a')

    # step 2.
    # step 2.1 prepare data/content to save
    content_list = [
        '1001,c001,2020-12-20,ITEM001,10,2.49,24.90 \n',
        '1002,c002,2020-12-20,ITEM001,5,2.49,7.45 \n',
        '1003,c001,2020-12-21,ITEM002,10,3.00,30.00 \n'
    ]

    # step 2.2 execute writing
    file.writelines(content_list)

    # step 3.
    file.close()

except FileExistsError as fe:
    print(fe)

except Exception as e:
    print(e)


