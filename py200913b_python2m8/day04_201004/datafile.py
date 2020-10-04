"""
Data file

1. csv
A CSV is a comma-separated values file, which allows data to be saved in a tabular format.
CSVs look like a garden-variety spreadsheet but with a . csv extension.
CSV files can be used with most any spreadsheet program, such as Microsoft Excel or Google Spreadsheets.

Text editor
spreadsheet program
database application export data as .CSV

keywords:
csv file sample download
https://www.stats.govt.nz/large-datasets/csv-files-for-download/

dataset source:
government data

dataset size
big data file
1. split
2. steaming

data clean/washing
dirty data
data pre-processing
data processing and analysis
data query

"""

# data clean
# data pre-processing


title = "Series_reference,Period,Data_value," \
        "Suppressed,STATUS,UNITS,Magnitude,Subject," \
        "Group,Series_title_1,Series_title_2,Series_title_3," \
        "Series_title_4,Series_title_5"

titlelist = title.split(",")
print(len(titlelist))

data1 = r"ECTM.S1AG1210,2000.01,9.1,,C,Dollars,6,Electronic Card Transactions (ANZSIC06) - ECT,Private - Values - Electronic card transactions  A/S/T by industry,Actual,Supermarket and grocery stores,,,"
datalist1 = data1.split(",")
print(len(datalist1))
for data in datalist1:
    print(data)
print()

data2 = r"ECTM.S1AG1210,2001.11,618.7,,C,Dollars,6,Electronic Card Transactions (ANZSIC06) - ECT,Private - Values - Electronic card transactions  A/S/T by industry,Actual,Supermarket and grocery stores,,,"
datalist2 = data2.split(",")
print(len(datalist2))
print(datalist2)