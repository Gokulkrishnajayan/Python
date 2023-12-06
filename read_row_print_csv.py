import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            print(row)

file_path = 'csv.txt'

read_csv_file(file_path)
