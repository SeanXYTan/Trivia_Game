import inspect
import re
from unittest.mock import patch

import pytest

from question import Question


@pytest.fixture
def question():
    """Fixture with set question and answers"""
    q = Question(
        "Question text",
        "correct",
        ["wrong", "false", "incorrect"],
        "category",
        "medium",
    )
    q.answers = ["correct", "wrong", "false", "incorrect"]
    q.answer_id = 1
    return q


def test_question(question):
    """Simple attribute check"""
    assert question.question == "Question text"
    assert "correct" in question.answers
    assert "incorrect" in question.answers
    assert question.difficulty == "medium"
    assert question.category == "category"


def test_string(question):
    """Tests the str method"""
    question_string = str(question)
    lines = question_string.split("\n")
    assert "Question text" in question_string
    assert re.search(r"1\W+correct", question_string)
    assert "correct" in lines[1]

    assert lines[4].startswith("4")
    assert "incorrect" in lines[4]


@patch("random.shuffle")
def test_random_question(mock_random):
    """Checks the constructor calls random.shuffle at least once"""
    q = Question(
        "Question?", "correct", ["wrong", "incorrect", "false"], "general", "medium"
    )
    assert mock_random.call_count >= 1


def test_difficulty():
    """Checks the constructor raises an exception when an invalid difficulty is provided"""
    with pytest.raises(AttributeError):
        q = Question(
            "Question?",
            "correct",
            ["wrong", "incorrect", "false"],
            "general",
            "whatever",
        )

    for difficulty in ("easy", "medium", "hard"):
        q = Question(
            "Question?",
            "correct",
            ["wrong", "incorrect", "false"],
            "general",
            difficulty,
        )
        assert q.difficulty == difficulty


def test_score(question):
    """
    above 5s: 10 * difficulty (1, 2, 3)
    below 5s: int(difficulty * (225/elapsed - 7 * elapsed))
    """
    question.difficulty = "easy"
    assert question.get_score(10) == 10
    assert question.get_score(4) == 28
    assert question.get_score(1) == 218

    question.difficulty = "medium"
    assert question.get_score(10) == 20
    assert question.get_score(4) == 56
    assert question.get_score(1) == 436

    question.difficulty = "hard"
    assert question.get_score(10) == 30
    assert question.get_score(4) == 84
    assert question.get_score(1) == 654


def test_docstring():
    """Checks that the code has docstrings!"""
    objs = [
        Question,
        Question.get_score,
    ]

    for elem in objs:
        docstring = inspect.getdoc(elem)
        assert docstring is not None and len(docstring) > 5
