import csv

filename = "OlympicMedals_2020.csv"

with open(filename, encoding="utf-8", newline="") as csv_file:  # should always include newline=""
    #  allows csv module to deal with newline characters
    headers = csv_file.readline().strip("\n").split(",")
    print(f"Column Headers: {headers}")
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
