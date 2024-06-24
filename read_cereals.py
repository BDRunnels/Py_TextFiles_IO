import csv

filename = "cereal_grains.csv"

with open(filename, encoding="utf-8", newline="") as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)  # all non-numeric values have been quoted, rest are floats
    for row in reader:
        print(row)
