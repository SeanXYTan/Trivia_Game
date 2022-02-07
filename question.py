"""
Description: Lab for week 5
- The structure of a question
- Takes a question and returns it as a string that has the question and answers
Name: Sean Tan, A01277524
Date: Jan 31th, 2022
"""


import random


class Question:
    """Generates a question using an object given, assigns:
    - self.question = The trivia question
    - self.answers = The 4 choices, with one being the right answer
    - self.answers_if = The correct answers index #
    - self.category = The trivia question's category
    - self.difficulty = the trivia question's difficulty
    """
    def __init__(self, question: str, correct_answer: str, incorrect_answers: list, category: str, difficulty: str):
        self.question = question
        self.answers = [correct_answer]
        for num in incorrect_answers:
            self.answers.append(num)
        random.shuffle(self.answers)
        self.answers_id = self.answers.index(correct_answer) + 1
        self.category = category
        if difficulty in ["easy", "medium", "hard"]:
            self.difficulty = difficulty
        else:
            raise AttributeError

    def as_string(self) -> str:
        """Takes the trivia's question and answers and returns a string containing all of them

        Returns:
            (str): The string that has the trivia's question and answer choices.
        """
        m_string = [self.question]
        for index, answer in enumerate(self.answers):
            string = str(index + 1) + " " + answer
            m_string.append(string)
        return '\n'.join(map(str, m_string))
