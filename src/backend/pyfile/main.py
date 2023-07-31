from csv_module.new_csv import make_csv_file
from csv_module.read_file import read_csv_file
from csv_module.read_cp_file import copy_to_output

import os

def csv_file(input_file):
    if input_file != "":
        print("input.csvファイルの内容:", input_file)
        make_csv_file(input_file)
        read_csv_file(input_file)
        copy_to_output(input_file)
    else:
        print("csvファイルへの記載がされなかったのでアプリを終了します")

input_file = input("csvファイルへの記載を行ってください \n")
csv_file(input_file)