import questionary

def main_bot():
    print("おすすめ検索エンジン紹介！！")

    question_one = questionary.select(
        "好きなの方は？",
        choices = ["やっぱ最新でしょ！", "やっぱ古いのでしょ！", "該当なし"],
        use_arrow_keys = True
    ).ask()

    if question_one == "やっぱ最新でしょ！":
        print("テスト1")
    elif question_one == "やっぱ古いのでしょ！":
        print("テスト2")
    else:
        print("エラー")
        
if __name__ == "__main__": 
    main_bot()