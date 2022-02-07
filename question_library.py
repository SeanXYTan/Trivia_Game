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
        self.categories = set()

        with open(filename, "r", encoding = "utf-8") as opened_file:
            data = json.load(opened_file)

        for qsn in data:
            self.categories.add(qsn["category"])
            self.questions.append(Question(qsn["question"], qsn["correct_answer"], qsn["incorrect_answers"], qsn["category"], qsn["difficulty"]))

        random.shuffle(self.questions)

    def get_questions(self, category: str='', difficulty: str='', number: int=1) -> list:
        """Retrieves questions from the list that fit the parameters given

        Args:
            category (str): the category of the question
            difficulty (str): the difficulty of the question
            number (int, optional): The number of questions requested

        Returns:
            list: The first few questions that were requested are stored in a list and returned
        """
        difficulties = ["easy", "medium", "hard"]
        filtered_questions = []

        for trivia in self.questions:
            if category.capitalize() == trivia.category and difficulty.lower() == trivia.difficulty:
                filtered_questions.append(trivia)
            elif (category.capitalize() == trivia.category
                    and difficulty.lower() not in difficulties):
                filtered_questions.append(trivia)
            elif (category.capitalize() not in self.categories
                    and difficulty.lower() == trivia.difficulty):
                filtered_questions.append(trivia)
            elif (category.capitalize() not in self.categories
                    and difficulty.lower() not in difficulties):
                filtered_questions.append(trivia)
            else:
                pass

        q_list = []
        if number <= len(filtered_questions):
            for index in range(number):
                q_list.append(filtered_questions[index])
        else:
            q_list = filtered_questions

        return q_list


if __name__ == "__main__":
    f = QuestionLibrary()
