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

    def __str__(self) -> str:
        m_string = f"{self.question}"
        for index, answer in enumerate(self.answers):
            string = "\n" + str(index+1) + " " + answer
            m_string += string
        return m_string

    def get_score(self, time: float) -> int:
        """Gets the score based on the time elapsed and the difficulty of the question.

        Args:
            time (float): The time elapsed for the question.

        Returns:
            score (int): The score that's been calculated.
        """

        if self.difficulty == "easy":
            diff = 1
        elif self.difficulty == "medium":
            diff = 2
        elif self.difficulty == "hard":
            diff = 3

        if time > 5.0:
            score = diff * 10
        else:
            score = diff * (225//time - 7 * time)

        return score
