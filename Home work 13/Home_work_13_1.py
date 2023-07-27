import csv

try:
    with open('SampleCSVFile_11kb.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)