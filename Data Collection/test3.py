# This code accesses a certain row based on a row_number and checks if it contains a URL

import csv

def read_specific_row(csv_file, row_number):
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader, 1):  # Start counting from 1
            if count == row_number:  # Check if it's the desired row
                if row:  # Check if the row is not empty
                    return row[0]  # Return the contents of the first column
                else:
                    return None
    return None

csv_file = 'product_URLs.csv'
row_number = 1
data = read_specific_row(csv_file, row_number)

while data is not None:
    print(row_number)   
    print(data)

    row_number += 1
    data = read_specific_row(csv_file, row_number)