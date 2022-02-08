"""
Description: Lab for week 5
- Converts json files into a list full of dictionaries
- Retrieves questions based on arguments and stores them in a list to be returned
Name: Sean Tan, A01277524
Date: Jan 31th, 2022
"""

import json
import random
from question import Question


class QuestionLibrary:
    """Reads a json file and stores each question(dictionary) in a list

    Args:
        Question (class): A trivia question
    """
    def __init__(self, filename="trivia.json"):
        self.questions = []

        with open(filename, "r", encoding = "utf-8") as opened_file:
            data = json.load(opened_file)

        for qsn in data:
            self.questions.append(Question(qsn["question"], qsn["correct_answer"], qsn["incorrect_answers"], qsn["category"], qsn["difficulty"]))

        random.shuffle(self.questions)

    def __len__(self) -> int:
        return len(self.questions)

    def get_categories(self) -> set:
        """Gets the categories that are in the total list of questions
        and creates a set that does not repeat categories

        Returns:
            categories (set): a list of categories the questions in <self.questions> have
        """
        categories = set()
        for qsn in self.questions:
            categories.add(qsn.category)
        return categories

    def get_questions(self, category=None, difficulty=None, number: int=10) -> list:
        """Retrieves questions from the list that fit the parameters given

        Args:
            category (None): the category of the question
            difficulty (None): the difficulty of the question
            number (int, optional): The number of questions requested

        Returns:
            q_list (list): The first few questions that were requested are stored in a list.
        """
        if isinstance(category, int) is True:
            for idx, cat in enumerate(self.get_categories()):
                if idx+1 == category:
                    category = cat

        filtered_questions = self.questions.copy()

        if difficulty in ("easy", "medium", "hard"):
            filtered_questions = [qst for qst in filtered_questions if qst.difficulty == difficulty]
        if category in self.get_categories():
            filtered_questions = [qst for qst in filtered_questions if qst.category == category]

        q_list = []
        if number <= len(filtered_questions):
            for index in range(number):
                q_list.append(filtered_questions[index])
        else:
            q_list = filtered_questions

        return q_list
