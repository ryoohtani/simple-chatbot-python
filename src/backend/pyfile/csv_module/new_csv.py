####################################
#比較用with open未使用版
import csv

def make_csv_file(input_file):
    csv_data = []

    csv_data.append([input_file])

    input_file = "./file_saving/input.csv"
    file = open(input_file, "w")
    writer = csv.writer(file)
    for writer_csv in csv_data:
        writer.writerow(writer_csv)
    file.close()
####################################
#比較用with open使用版
import csv

def make_csv_file(input_file):
    csv_data = []

    csv_data.append([input_file])

    input_file = "./file_saving/input.csv"
    with open(input_file, "w") as file:
        writer = csv.writer(file)
        for writer_csv in csv_data:
            writer.writerow(writer_csv)
####################################