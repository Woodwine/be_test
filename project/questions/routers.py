from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from project.db_methods import get_question_id, create_question, get_previous_question
from project.database import get_async_session
from project.questions.schemas import QuestionResponse
from project.questions.utils import get_question

router = APIRouter(
    prefix='/questions',
    tags=['questions']
)


@router.post('/', response_description='Add new questions into the database', response_model=QuestionResponse)
async def add_new_questions(questions_num: int, session: AsyncSession = Depends(get_async_session)):
    """
    Creates one or more unique quiz questions, returns a previous question.
    :param questions_num: int
    :param session: AsyncSession
    :return: QuestionResponse
    """

    questions = get_question(questions_num)
    result_id = await get_question_id(session)
    previous_question = await get_previous_question(session)

    while questions:
        item = questions.pop()
        if item.get('id') in result_id:
            questions.append(*get_question())
        else:
            result = await create_question(item, session)
            if result:
                result_id.append(item.get('id'))

    if previous_question:
        return {"question": previous_question[0]}

    return {"question": None}
