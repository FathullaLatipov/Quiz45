from fastapi import APIRouter
from database.testservice import get_questions_db, add_question_db
from database.userservice import user_answer_db

test_router = APIRouter(prefix='/test', tags=['Работа с тестами'])

# Получить все 20 вопросов async def all_20_questions()
# Для добавления вопросов async def add_question -> add_question_db
# Для получегия вопросов как для теста async def get_questions - > get_questions_db
# Проверка результатов async def check_answer -> XX
