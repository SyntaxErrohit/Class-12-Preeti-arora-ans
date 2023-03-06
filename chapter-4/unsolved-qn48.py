import csv

with open("contacts.csv", "r") as f:
    objcsv = csv.reader(f, delimiter="")
    for i in objcsv:
        print("Name:", i[0], "Phone:", i[1])