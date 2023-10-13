from sqlalchemy import Column, String, Integer, TIMESTAMP

from project.database import Base


class QuizQuestion(Base):
    """
    Represents quiz question object.
    """

    __tablename__ = 'quiz_question'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    question_id: int = Column(Integer, unique=True, nullable=False)
    question: str = Column(String, nullable=False)
    answer: str = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
