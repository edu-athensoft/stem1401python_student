"""
Read a real .csv file known as data file
Print out line by line


[Homework]
1. Create a CSV file
3. Read and load data into memory
4. Print out the data properly


"""


def showdata(datalist):
    for entry in datalist:
        print(entry)   # with an extra empty line
        # print(entry, end="")

def showdatafield(entry):
    fields = entry.split(",")
    for field in fields:
        print(field)

# main program
# settings
DATA_FILE = "ect-Aug-2020-lower-level-data-release-csv.csv"

# data input
datalist = []
with open(DATA_FILE) as file:
    datalist = file.readlines()

# data processing
linenum = 1
entry1 = datalist[1]
showdatafield(entry1)

# data output
# showdata(datalist)