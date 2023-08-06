import questionary

class SectionModels(object):
    def all_question(self, question_one):

        if question_one == "やっぱ王道でしょ！":
            select_routo = questionary.select(
                "スマホに入れているアプリは？",
                choices = ["Chrome", "Safari"],
                use_arrow_keys = True
            ).ask()
            
            if select_routo == "Chrome":
                print("あなたにオススメなサイトはChromeです!\n", "https://www.google.co.jp/")
            else:
                print("あなたにオススメなサイトはSafariです!\n", "https://www.apple.com/safari/")

        elif question_one == "やっぱ人と違うのでしょ！":
            select_routo = questionary.select(
                "PCに入れているアプリは？",
                choices = ["FireFox", "Bing"],
                use_arrow_keys = True
            ).ask()
            if select_routo == "FireFox":
                print("あなたにオススメなサイトはFireFoxです!\n", "https://www.mozilla.org/firefox/")
            else:
                print("あなたにオススメなサイトはBingです!\n", "https://www.bing.com/")

        else:
            select_routo = questionary.select(
                "検索エンジンぐらいは冒険してみませんか？",
                choices = ["YANDEX", "DuckDuckGo"],
                use_arrow_keys = True
            ).ask()
            if select_routo == "YANDEX":
                print("あなたにオススメなサイトはYANDEXです!\n", "https://yandex.com/")
            else:
                print("あなたにオススメなサイトはDuckDuckGoです!\n", "https://duckduckgo.com/")