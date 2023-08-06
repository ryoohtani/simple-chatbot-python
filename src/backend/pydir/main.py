import questionary

from models.model_section import SectionModels
from views.view_section import SectionViews

def main():

    view_main = SectionViews()
    view_main.first_show()

    question_one = questionary.select(
        "好きなの方は？",
        choices = ["やっぱ王道でしょ！", "やっぱ人と違うのでしょ！", "特にないかな〜"],
        use_arrow_keys = True
    ).ask()

    view_main.last_show()

    modele_main = SectionModels()
    modele_main.all_question(question_one)
        
if __name__ == "__main__": 
    main()