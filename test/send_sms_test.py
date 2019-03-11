from src.TindevQA import TindevQA


def test_send_sms():
    app = TindevQA()
    user = 'Chewaka'
    text = 'Quieres enredarte entre mis pelos?'
    response = app.send_sms(user, text)
    assert response.ok == True

