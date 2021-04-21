"""
Quiz
date: 2020-11-29
to be scored

Problem: Renaming files in a batch
Write a program to rename multiple files in a specified directory

Requirements:
design and plan

sample design:
assuming 1: 
    file1.html, file2.html, file3.html,..., filen.html
    change file extension of each one to .txt
assuming 2:
    change file extension from one to another, keep main file name unchanged
assuming 3:
    change file name with extension from one to another
"""

import os

directory = input("What is the full path of the directory where are the files to rename?")

# Assuming 1:

try:
    stop = 0
    while stop != -1:
        for i in range(1, stop+1):
            os.rename(f"{directory}{os.sep}file{i}.html", f"{directory}{os.sep}file{i}.txt")
            print(f"Renamed {directory}{os.sep}file{i}.html to {directory}{os.sep}file{i}.txt")
        stop = int(input("How many files will you rename?(Type -1 to exit)"))
except Exception as e:
    print(e)


# Assuming 2

try:
    filename = ""
    extension = ""
    while filename != "-1":
        if filename != "":
            os.rename(f"{directory}{filename}", f"{directory}{os.sep}{filename[:filename.index('.')-1]}{extension}")
            print(f"Renamed {directory}{filename} to {directory}{os.sep}{filename[:filename.index('.')-1]}{extension}")
        filename = input("What is the name of the file to rename?(Type '-1' to exit)")
        extension = input("What will the new extension be?")
except Exception as e:
    print(e)