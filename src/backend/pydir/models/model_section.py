import questionary
from .model_csvcount import CSVCounter

class SectionModels(object):
    def __init__(self):
        self.aggregation_counter = CSVCounter()
        self.select_routo = None

    def all_question(self, question_one):
        if question_one == "やっぱ王道でしょ！":
            self.select_routo = questionary.select(
                "スマホに入れているアプリは？",
                choices=["Chrome", "Safari"],
                use_arrow_keys=True
            ).ask()

            #{}のプレースホルダーとformat関数を合わせることで、self.select_routo変数の中身を柔軟に使えるようにしました。
            print("あなたにオススメなサイトは{}です!\n".format(self.select_routo), "https://www.google.co.jp/")

        elif question_one == "やっぱ人と違うのでしょ！":
            self.select_routo = questionary.select(
                "PCに入れているアプリは？",
                choices = ["FireFox", "Bing"],
                use_arrow_keys = True
            ).ask()

            print("あなたにオススメなサイトは{}です!\n".format(self.select_routo), "https://www.mozilla.org/firefox/" if self.select_routo == "FireFox" else "https://www.bing.com/")

        else:
            self.select_routo = questionary.select(
                "検索エンジンぐらいは冒険してみませんか？",
                choices=["YANDEX", "DuckDuckGo"],
                use_arrow_keys = True
            ).ask()

            print("あなたにオススメなサイトは{}です!\n".format(self.select_routo), "https://yandex.com/" if self.select_routo == "YANDEX" else "https://duckduckgo.com/")

        #アプリの選択を実施する=Noneではないので、self.select_routo変数に代入される。if文内が実施される
        if self.select_routo is not None:
            self.aggregation_counter.increment_vote_count(self.select_routo)