import csv
import subprocess

def copy_csv_file():
    with open("./file_saving/input.csv", mode="r") as input_file_read:
        input_reader = csv.reader(input_file_read)
        #リスト内包表記を使って1行ずつリストとして格納
        input_data = [indata for indata in input_reader]

    with open("./file_saving/output.csv", mode="a") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(input_data)

        #ファイルの確認コマンド実行
        inout_directory = "./file_saving/"
        subprocess.run(["ls", "-la", inout_directory])