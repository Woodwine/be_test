from typing import Any
import requests


def get_question(num: int = 1) -> Any:
    url = f'https://jservice.io/api/random?count={num}'
    questions = requests.get(url).json()
    return questions
