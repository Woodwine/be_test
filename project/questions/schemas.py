from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class QuestionCreate(BaseModel):
    id: int
    question_id: int
    question: str
    answer: str
    creation_date: datetime

