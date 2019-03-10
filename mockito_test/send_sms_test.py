import requests
from mockito import when, mock
from requests import Timeout

from src.TindevQA import TindevQA

#
# def test_send_sms():
#     app = TindevQA()
#     user = 'Chewaka'
#     text = 'Quieres enredarte entre mis pelos?'
#     response = app.send_sms(user, text)
#     assert response.ok == True


def test_send_sms_with_mockito():
    app = TindevQA()
    user = 'Chewaka'
    text = 'Quieres enredarte entre mis pelos?'
    response_mock = mock({'status_code': 200, 'text': 'Ok'})
    when(requests).post(...).thenReturn(response_mock)

    response = app.send_sms(user, text)
    assert response.status_code == 200


def test_send_sms_get_500_error():
    app = TindevQA()
    user = 'Chewaka'
    text = 'Quieres enredarte entre mis pelos?'
    response_mock = mock({'status_code': 501})
    when(requests).post(...).thenReturn(response_mock)

    response = app.send_sms(user, text)
    assert response.status_code == 501


def test_send_sms_get_timeout():
    app = TindevQA()
    user = 'Chewaka'
    text = 'Quieres enredarte entre mis pelos?'
    when(requests).post(...).thenRaise(Timeout)

    response = app.send_sms(user, text)
    assert response == "ERROR"
