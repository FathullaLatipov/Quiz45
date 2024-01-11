from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String)
    phone_number = Column(Integer, unique=True)
    level = Column(String, default='None')
    datetime = Column(DateTime)


# Таблица вопросов
class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, unique=True, nullable=False)
    answer1 = Column(String)
    answer2 = Column(String)
    answer3 = Column(String)
    answer4 = Column(String)
    correct_answer = Column(Integer, nullable=False)
    timer = Column(Integer)


# Результат лидеров/результатов
class Result(Base):
    __tablename__ = 'leaders'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    correct_answers = Column(Integer, default=0)
    level = Column(String)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')


# Ответы пользователя на вопросы
class UserAnswers(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    q_id = Column(Integer, ForeignKey('questions.id'))
    level = Column(String, ForeignKey('users.level'))
    user_answer = Column(String)
    correctness = Column(Boolean, default=False)
    timer = Column(DateTime)

    user_fk = relationship(User, foreign_keys=[user_id],  lazy='subquery')
    question_fk = relationship(Questions, foreign_keys=[q_id], lazy='subquery')