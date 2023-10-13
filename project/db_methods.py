from datetime import datetime
from typing import List
from sqlalchemy import select, insert, desc
from sqlalchemy.ext.asyncio import AsyncSession

from project.questions.models import QuizQuestion
from project.questions.schemas import QuestionCreate


async def get_question_id(session: AsyncSession) -> List[int]:
    """
    Gets a list of all question id from the table 'quiz_question'.
    :param session: AsyncSession
    :return: List[int]
    """

    query = select(QuizQuestion.question_id)
    result = await session.execute(query)
    question_id = [i[0] for i in result.all()]
    return question_id


async def get_previous_question(session: AsyncSession) -> QuestionCreate | None:
    """
    Gets the last question from the table 'quiz_question'.
    :param session: AsyncSession
    :return: QuestionCreate | None
    """

    query = select(QuizQuestion).order_by(desc(QuizQuestion.id))
    result = await session.execute(query)
    return result.first()


async def create_question(question: dict, session: AsyncSession) -> bool:
    """
    Creates a new quiz question.
    :param question: dict
    :param session: AsyncSession
    :return: bool
    """
    created_at = datetime.strptime(question.get('created_at'), '%Y-%m-%dT%H:%M:%S.%fZ')

    statement = insert(QuizQuestion).values(
        question_id=question.get('id'),
        question=question.get('question'),
        answer=question.get('answer'),
        created_at=created_at
    )

    await session.execute(statement)
    await session.commit()
    return True
