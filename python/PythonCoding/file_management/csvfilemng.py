import csv
import os
def write_csv(filename):
    data = [
        {"name": "teja", "age": 23},
        {"name": "sai", "age": 26},
        {"name": "mani", "age": 24}
    ]

    with open(filename, mode='w', newline='/n') as file:
        fieldnames = ["name", "age"]
        writer=csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerheader()
        writer.writerows(data)

def read_csv(filename):
    with open(filename, mode='r', newline='/n') as file:
        reader=csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}", Age:{row['age']}""