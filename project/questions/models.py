from sqlalchemy import Column, String, Integer, TIMESTAMP

from project.database import Base


class QuizQuestion(Base):
    __tablename__ = 'quiz_question'

    id: int = Column(Integer, primary_key=True)
    question_id: int = Column(Integer, unique=True)
    question: str = Column(String)
    answer: str = Column(String)
    created_at = Column(TIMESTAMP)
