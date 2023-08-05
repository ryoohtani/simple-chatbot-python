import questionary

def c_end():
    print("最後の設問")

    c_routo = questionary.select(
        "検索エンジンぐらいは冒険してみませんか？",
        choices = ["YANDEX", "DuckDuckGo"],
        use_arrow_keys = True
    ).ask()

    if c_routo == "YANDEX":
        print("あなたにオススメなサイトはYANDEXです!\n", "https://yandex.com/")

    else:
        print("あなたにオススメなサイトはDuckDuckGoです!\n", "https://duckduckgo.com/")

if __name__ == "__main__": 
    c_end()