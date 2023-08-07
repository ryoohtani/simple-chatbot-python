import questionary

from views.view_section import SectionViews
from models.model_section import SectionModels

def main():
    view_main = SectionViews()
    view_main.first_show()

    question_one = questionary.select(
        "好きなの方は？",
        choices = ["やっぱ王道でしょ！", "やっぱ人と違うのでしょ！", "特にないかな〜"],
        use_arrow_keys = True
    ).ask()

    view_main.last_show()

    model_main = SectionModels()
    model_main.all_question(question_one)

if __name__ == "__main__": 
    main()