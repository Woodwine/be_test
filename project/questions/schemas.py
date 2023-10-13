from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class QuestionCreate(BaseModel):
    """
    Represents a created object of QuizQuestion.
    """

    id: int
    question_id: int
    question: str
    answer: str
    created_at: datetime


class QuestionResponse(BaseModel):
    """
    Represents a response object.
    """

    question: Optional[QuestionCreate] = None
