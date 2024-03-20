# This code reads a CSV file and prints everything in it's first column

import csv

def read_first_column(csv_file):
    count = 1
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Check if row is not empty
                print(count)
                print(row[0])
                count += 1

# Example usage
csv_file = 'product_URLs.csv'
read_first_column(csv_file)
