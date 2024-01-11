from fastapi import APIRouter
from database.userservice import register_user_db, user_answer_db, plus_point_user_db, get_all_users_db
from database.testservice import get_questions_db, add_question_db

user_router = APIRouter(prefix='/user', tags=['Users'])


# Регистрация пользователя
@user_router.post('/register')
async def register(username: str, phone_number: int, level: str):
    register = register_user_db(username, phone_number, level)
    return f'Вы успешно прошли регистрацию {register}'


# Получить всех пользователей
@user_router.get('/all_users')
async def all_users():
    return get_all_users_db()


@user_router.get('/leaders')
async def get_leaders(user_id: int, q_id: int, user_answer: str):
    get_leaders = user_answer_db(user_id, q_id, user_answer)
    return f'Лидеры {get_leaders}'


@user_router.post('/done')
async def done(user_id: int, correct_answers: int):
    done = plus_point_user_db(user_id, correct_answers)
    return f'Результат {done}'
