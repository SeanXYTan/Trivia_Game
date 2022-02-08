"""
Description: Lab for week 5
The main trivia game, features include:
- Win/Loss tracking
- Category listing
Name: Sean Tan, A01277524
Date: Jan 31th, 2022
"""

import time
from question_library import QuestionLibrary


class Game:
    """Game class that has the following features
    - playing the trivia game
    """
    def __init__(self):
        self.questions = []
        self.q_lib = QuestionLibrary()
        for idx, cat in enumerate(self.q_lib.get_categories()):
            print(idx+1, cat)

        get_category = input("What Category?: ")
        if get_category in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            get_category = int(get_category)
        elif get_category not in self.q_lib.get_categories():
            get_category = None

        get_difficulty = input("What Difficulty? (easy,/medium/hard): ")
        if (get_difficulty.lower() not in ['easy', 'medium', 'hard']
                or get_difficulty == ''):
            get_difficulty = None

        self.questions = self.q_lib.get_questions(get_category, get_difficulty)

    def play(self):
        """Plays the trivia game
        - Prints the questions and the answers
        - Prompts the user to select an answer based on the number assigned
        - Calculates the score based on the time taken to answer the question
        - Gives no score if the answer was not right
        - Ends the game once the user has answered all questions
        """
        wins = 0
        losses = 0
        score = 0
        for question in self.questions:
            print(f"-----\n{question.__str__()}\n-----")
            start = time.time()
            answer = int(input("Type your answer as a number: "))
            while answer not in range(1,5):
                answer = input("Type your answer as a number (either 1,2,3 or 4): ")
            end = time.time()
            elapsed = end -start
            if answer == question.answers_id:
                print("\n*****\nCorrect!\n*****\n")
                wins += 1
                score += question.get_score(elapsed)
            else:
                print(f"\n*****\nIncorrect!\nIt was {question.answers_id}\n*****\n")
                losses += 1
        print (f"------\nWins: {wins} \nLosses: {losses}\nScore: {score}\n------")
