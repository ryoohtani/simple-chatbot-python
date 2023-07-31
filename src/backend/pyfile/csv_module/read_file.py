def read_csv_file(input_file):
    input_file = "./file_saving/input.csv"
    file_read = open(input_file)

    for line_file in file_read:
        print(line_file)
    
    file_read.close()