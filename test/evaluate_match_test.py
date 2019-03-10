from mock import patch, call
from src.TindevQA import TindevQA


@patch.object(TindevQA, "let_down_gently")
def test_person2_dislikes_person1(mock_let_down):

    app = TindevQA()
    person1 = 'Luke'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}

    app.evaluate(person1, person2)

    assert mock_let_down.call_count == 1


@patch.object(TindevQA, "let_down_gently")
def test_person2_dislikes_person1_parameters(mock_let_down):

    app = TindevQA()
    person1 = 'Luke'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}

    app.evaluate(person1, person2)

    mock_let_down.assert_called_once_with(person1)


@patch.object(TindevQA, "give_it_time")
@patch.object(TindevQA, "send_email")
@patch.object(TindevQA, "let_down_gently")
def test_person2_dislikes_person1_multiple_mocks(mock_let_down, mock_send_mail, mock_give_it_time):

    app = TindevQA()
    person1 = 'Luke'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}

    app.evaluate(person1, person2)

    mock_let_down.assert_called_once_with(person1)
    assert mock_send_mail.call_count == 0
    assert mock_give_it_time.call_count == 0


@patch.object(TindevQA, "send_email")
def test_person2_likes_person1( mock_send_mail):

    app = TindevQA()
    person1 = 'Han Solo'
    person2 = {'name': 'Leia',
               'likes': ['Han Solo'],
               'dislikes': ['Luke']}

    app.evaluate(person1, person2)

    person1_mail_received = mock_send_mail.call_args_list[0]
    person2_mail_received = mock_send_mail.call_args_list[1]
    assert person1_mail_received == call(person1)
    assert person2_mail_received == call(person2)
