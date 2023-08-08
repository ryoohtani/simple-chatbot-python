import csv

class CSVCounter(object):
    def __init__(self):
        self.file_path = "./file_save/aggregation.csv"

    def save_aggregation_counts(self, voting_data):
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["検索エンジン", "投票数"])
            #itemsは辞書型のメソッドで、辞書内のキー(engine)と値(count)のペアを取得
            for engine, count in voting_data.items():
                writer.writerow([engine, count])

    def load_aggregation_counts(self):
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader)
                #辞書型でcsvファイルを格納する。word[0]が検索エンジン、word[1]が投票数をリストの内包表記を用いて格納する
                aggregation_counts = {word[0]: int(word[1]) for word in reader}
        except FileNotFoundError:
            aggregation_counts = {"Chrome": 0, "Safari": 0, "FireFox": 0, "Bing": 0, "YANDEX": 0, "DuckDuckGo": 0}
        return aggregation_counts

    def increment_aggregation_count(self, engine):
        counts_dict = self.load_aggregation_counts()
        #指定された検索エンジンの投票数を1つ増やす
        counts_dict[engine] += 1
        #データの保存し、csvが更新される
        self.save_aggregation_counts(counts_dict)