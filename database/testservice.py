from .models import Result, Questions
from database import get_db


# Топ 5 лидеров
def get_5_leaders_db():
    db = next(get_db())
    leaders = db.query(Result.user_id).order_by(Result.correct_answers.desc())

    return leaders[:5]


# Мы сами добавляем вопросы и варианты))
def add_question_db(main_question, answer1, answer2, answer3, answer4):
    db = next(get_db())
    new_question = Questions(main_question=main_question, answer1=answer1, answer2=answer2,
                             answer3=answer3, answer4=answer4)
    db.add(new_question)
    db.save()
    return 'Вопрос успешно добавлен!'


# Получить только 20 тестов
def get_questions_db():
    db = next(get_db())

    questions = db.query(Questions).all()

    return questions[:20]
