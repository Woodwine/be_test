from typing import Any, List
import requests


def get_question(num: int = 1) -> List[Any]:
    """
    Get a list of questions from public API.
    :param num:
    :return: List[Any]
    """

    url = f'https://jservice.io/api/random?count={num}'
    questions = requests.get(url).json()
    return questions
