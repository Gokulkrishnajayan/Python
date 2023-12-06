import csv

def read_csv_column(file_path, column_index):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            if column_index < len(row):
                print(row[column_index])
            else:
                print("Column index",column_index,"is out of range for this row.")
                return

file_path = 'csv.txt'
column_index_to_read =int(input("Enter the column index:"))

read_csv_column(file_path, column_index_to_read)
