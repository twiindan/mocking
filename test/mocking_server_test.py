import requests

from src.TindevQA import TindevQA

def test_send_sms():

    app = TindevQA()
    user = 'Chewaka'
    text = 'Quieres enredarte entre mis pelos?'
    response = app.send_sms(user, text)

    r = requests.get('http://localhost:8080/stats')
    body = r.json()

    assert body['requests'][0]['from'] == 'Chewaka'
    assert body['requests'][0]['to'] == '34677722314'
    assert body['requests'][0]['text'] == 'Quieres enredarte entre mis pelos?'


def test_send_sms_with_error():
    app = TindevQA()
    user = 'Chewaka'
    text = 'Quieres enredarte entre mis pelos?'
    data = {'status_code': 500, 'message': 'Servidor Caido'}

    r = requests.post('http://localhost:8080/set_response', json=data)

    response = app.send_sms(user, text)
    assert response.status_code == 500
    assert response.text == 'Servidor Caido'
