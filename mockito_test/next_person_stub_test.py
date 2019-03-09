from src.TindevQA import TindevQA
from mockito import when, mock, unstub


def test_new_person_decorator():
    # Arrange
    app = TindevQA()
    user = {'people_seen': []}
    expected_person = 'Alexandra'
    when(app).get_random_user().thenReturn('Alexandra')

    # Action
    actual_person = app.get_next_person(user)

    # Assert
    assert actual_person == expected_person


def test_new_person_several_times():

    app = TindevQA()
    user = {'people_seen': ['Sara', 'Alexandra']}
    expected_person = 'Leia'
    when(app).get_random_user().thenReturn('Alexandra', 'Sara', 'Leia')

    # Action
    actual_person = app.get_next_person(user)

    # Assert
    assert actual_person == expected_person
