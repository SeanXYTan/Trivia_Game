import inspect
from unittest.mock import mock_open, patch

import pytest

from question import Question
from question_library import QuestionLibrary

JSON_FILE = """[
    {
        "question": "MEDIUM question (general category)?",
        "correct_answer": "correct",
        "incorrect_answers": ["wrong", "false", "incorrect"],
        "category": "category",
        "difficulty": "medium"
    },
    {
        "question": "HARD question (other category)?",
        "correct_answer": "correct",
        "incorrect_answers": ["wrong", "false", "incorrect"],
        "category": "other",
        "difficulty": "hard"
    }
]"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=JSON_FILE)
def lib(mock_file):
    return QuestionLibrary()


def test_library(lib):
    """Simple test and type checks"""
    assert len(lib) == 2
    assert all([type(q) == Question for q in lib.questions])


def test_library_get(lib):
    """Make sure the get_questions filter the questions correctly"""
    qs = lib.get_questions(category="other")
    assert len(qs) == 1
    assert qs[0].category == "other"

    qs = lib.get_questions(difficulty="hard")
    assert len(qs) == 1
    assert qs[0].difficulty == "hard"

    # An invalid difficulty will be accepted, but no filtering will be done
    qs = lib.get_questions(difficulty="whatever")
    assert len(qs) == 2
    assert "hard" in [q.difficulty for q in lib.questions]
    assert "medium" in [q.difficulty for q in lib.questions]


def test_get_categories(lib):
    """Checks the get_categories"""
    cats = lib.get_categories()
    assert len(cats) == 2
    assert "category" in cats
    assert "other" in cats


def test_docstrings():
    """Checks the code has docstrings!"""
    objs = [
        QuestionLibrary,
        QuestionLibrary.get_questions,
        QuestionLibrary.get_categories,
    ]

    for elem in objs:
        docstring = inspect.getdoc(elem)
        assert docstring is not None and len(docstring) > 5
