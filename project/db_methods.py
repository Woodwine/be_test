from sqlalchemy import select, insert, desc
from sqlalchemy.ext.asyncio import AsyncSession

from questions.models import QuizQuestion
from questions.schemas import QuestionCreate


async def get_question_id(session: AsyncSession):
    query = select(QuizQuestion.question_id)
    result = await session.execute(query)
    return result.all()


async def get_previous_question(session: AsyncSession):
    query = select(QuizQuestion).order_by(desc(QuizQuestion.id))
    try:
        result = await session.execute(query)
        return result.first()
    except:
        return {}


async def create_question(question: QuestionCreate, session: AsyncSession) -> bool:
    question['creation_date'] = question['creation_date'][:-1]
    statement = insert(QuizQuestion).values(question.model_dump())
    try:
        await session.execute(statement)
        await session.commit()
        return True
    except Exception:
        return False
