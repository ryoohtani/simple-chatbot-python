import csv

def copy_csv_file():
    with open("./file_saving/input.csv", mode="r") as input_file_read:
        input_reader = csv.reader(input_file_read)
        data_to_write = [row for row in input_reader]

    with open("./file_saving/output.csv", mode="a", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data_to_write)