import questionary
from sub_module.section_1 import a_end
from sub_module.section_2 import b_end
from sub_module.section_3 import c_end

def main_bot():
    print("おすすめ検索エンジン紹介！！")

    question_one = questionary.select(
        "好きなの方は？",
        choices = ["やっぱ王道でしょ！", "やっぱ人と違うのでしょ！", "特にないかな〜"],
        use_arrow_keys = True
    ).ask()

    if question_one == "やっぱ王道でしょ！":
        a_end()
    elif question_one == "やっぱ人と違うのでしょ！":
        b_end()
    else:
        c_end()
        
if __name__ == "__main__": 
    main_bot()