
#######削除機能###########
# import csv

# def copy_to_output(input_file):
#     input_file = "./file_saving/input.csv"
#     output_file = "./file_saving/output.csv"

#     with open(input_file, "r") as file_read, open(output_file, "w", newline='') as file_write:
#         reader = csv.reader(file_read)
#         writer = csv.writer(file_write)

#         for row in reader:
#             writer.writerow(row)
#########################



import csv

def copy_to_output(input_data):
    output_file = "./file_saving/output.csv"

    with open(output_file, "w", newline='') as file_write:
        writer = csv.writer(file_write)

        writer.writerow([input_data])
