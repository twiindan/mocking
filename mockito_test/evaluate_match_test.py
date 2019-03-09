from mock import patch, call
from mockito import spy
from mockito import verify
from mockito import verifyZeroInteractions
from mockito import when, mock

from src.TindevQA import TindevQA


def test_person2_dislikes_person1():

    app = TindevQA()
    person1 = 'Luke'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}
    when(app).let_down_gently(...)
    app.evaluate(person1, person2)

    verify(app, times=1).let_down_gently(...)


def test_person2_dislikes_person1_parameters():

    app = TindevQA()
    person1 = 'Luke'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}
    when(app).let_down_gently(person1)
    app.evaluate(person1, person2)

    verify(app, times=1).let_down_gently(person1)


def test_person2_dislikes_person1_multiple_mocks():

    app = TindevQA()
    person1 = 'Luke'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}

    when(app).let_down_gently(person1)
    when(app).send_email(...)
    when(app).give_it_time(...)

    app.evaluate(person1, person2)
    verify(app, times=1).let_down_gently(person1)
    verify(app, times=0).send_email(...)
    verify(app, times=0).give_it_time(...)


def test_person2_likes_person1():

    app = TindevQA()
    person1 = 'Han Solo'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}

    when(app).let_down_gently(person1)
    when(app).send_email(...)
    when(app).give_it_time(...)

    app.evaluate(person1, person2)

    verify(app, times=2).send_email(...)
    verify(app, times=1).send_email(person1)
    verify(app, times=1).send_email(person2)
