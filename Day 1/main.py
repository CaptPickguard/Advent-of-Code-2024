#!/usr/bin/python3

# Day 1
# import pandas as pd
# df = pd.read_csv("Equadgrams.txt",sep=" ")

fo = open("input.txt", "r")
str = fo.read()
baselist = str.split()
input1 = []
input2 = []
count = 1

for i in baselist:
    if count == 1:
        input1.append(i)
        count += 1
    elif count == 2:
        input2.append(i)
        count = 1

print("Read String is : ")

print(input2)

fo.close()


