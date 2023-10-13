from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db_methods import get_question_id, create_question, get_previous_question
from project.database import get_async_session
from project.questions.schemas import QuestionCreate
from project.questions.utils import get_question

router = APIRouter(
    prefix='/questions',
    tags=['questions']
)


@router.post('/', response_description='Add new questions into the database')
async def add_new_questions(questions_num: int, session: AsyncSession = Depends(get_async_session)) -> QuestionCreate:
    questions = get_question(questions_num)
    result = await get_question_id(session)
    previous_question = await get_previous_question(session)

    while questions:
        item = questions.pop()
        if item.get('id') in result:
            questions.append(get_question())
        else:
            await create_question(item, session)
    return previous_question




