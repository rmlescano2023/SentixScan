# This code will continuously make a CSV file while looping

import csv
import time

def write_to_csv(filename, data):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    base_filename = 'file_'
    iteration = 0

    while iteration != 5:
        csv_filename = f'{base_filename}{iteration + 1}.csv'
        header = ['Timestamp', 'Value']

        # Write header to the CSV file
        write_to_csv(csv_filename, header)

        # Generate data
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        value = 42  # Example value, replace it with your actual data source
        data = [timestamp, value]

        # Write data to the CSV file
        write_to_csv(csv_filename, data)

        print(f'Data written to {csv_filename}: {data}')
        time.sleep(1)  # Adjust the sleep duration as needed
        iteration += 1

if __name__ == "__main__":
    main()
