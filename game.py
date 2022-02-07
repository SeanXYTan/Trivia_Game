"""
Description: Lab for week 5
The main trivia game, features include:
- Win/Loss tracking
- Category choices
Name: Sean Tan, A01277524
Date: Jan 31th, 2022
"""

from question_library import QuestionLibrary


class Game:
    """Game class that has the following features
    - playing the trivia game
    """
    def __init__(self):
        self.questions = []
        self.q_lib = QuestionLibrary()
        get_category = input("What Category? \n(type 'Categories' to see the list of categories available): ")
        if get_category.capitalize() == 'Categories':
            print(self.q_lib.categories)
            get_category = input("What Category?: ")
        get_difficulty = input("What Difficulty? (easy,/medium/hard): ")
        get_number = 0
        while get_number <= 0:
            get_number = int(input("How many questions do you want?: "))
        self.questions = self.q_lib.get_questions(get_category, get_difficulty, get_number)

    def play(self):
        """Loop that runs the trivia game based on the number of questions requested.
        """
        wins = 0
        losses = 0
        for question in self.questions:
            print(f"-----\n{question.as_string()}\n-----")
            answer = int(input("Type your answer as a number: "))
            while answer not in range(1,5):
                answer = input("Type your answer as a number (either 1,2,3 or 4): ")
            if answer == question.answers_id:
                print("\n*****\nCorrect!\n*****\n")
                wins += 1
            else:
                print(f"\n*****\nIncorrect!\nIt was {question.answers_id}\n*****\n")
                losses += 1
        print (f"------\nWins: {wins} \nLosses: {losses}\n------")

if __name__ == "__main__":
    g = Game()
    g.play()
