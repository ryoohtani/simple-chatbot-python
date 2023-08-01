import csv

def read_csv_file():
    with open("./file_saving/input.csv", mode="r") as file_read:
        reader = csv.reader(file_read)
        for line_csv in reader:
            print(line_csv[0])