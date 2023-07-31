from csv_module.new_csv import make_csv_file
import os

def csv_file(input_file):
    if input_file != "":
        print("ファイル名:", input_file)
        make_csv_file(input_file)
    else:
        print("文字を入力してください")

input_file = input("csvファイルへの記載を行ってください \n")
csv_file(input_file)