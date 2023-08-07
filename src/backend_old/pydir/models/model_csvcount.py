import csv

def make_csv_file(model_main):
    csv_data = []
    csv_data.append([model_main])

    model_main = "./file_save/aggregation.csv"

    with open(model_main, mode="w") as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)