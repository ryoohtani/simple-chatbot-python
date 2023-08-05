import questionary

def b_end():
    print("最後の設問")

    b_routo = questionary.select(
        "PCに入れているアプリは？",
        choices = ["FireFox", "Bing"],
        use_arrow_keys = True
    ).ask()

    if b_routo == "FireFox":
        print("あなたにオススメなサイトはFireFoxです!\n", "https://www.mozilla.org/firefox/")

    else:
        print("あなたにオススメなサイトはBingです!\n", "https://www.bing.com/")

if __name__ == "__main__": 
    b_end()