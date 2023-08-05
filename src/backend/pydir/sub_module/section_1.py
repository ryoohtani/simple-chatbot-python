import questionary

def a_end():
    print("最後の設問")

    a_routo = questionary.select(
        "スマホに入れているアプリは？",
        choices = ["Chrome", "Safari"],
        use_arrow_keys = True
    ).ask()

    if a_routo == "Chrome":
        print("あなたにオススメなサイトはChromeです!\n", "https://www.google.co.jp/")

    else:
        print("あなたにオススメなサイトはSafariです!\n", "https://www.apple.com/safari/")

if __name__ == "__main__": 
    a_end()
