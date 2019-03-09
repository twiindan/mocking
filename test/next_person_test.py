from src.TindevQA import TindevQA


def test_new_person():
    # Arrange
    app = TindevQA()
    user = {'people_seen': []}
    expected_person = 'Alexandra'

    # Action
    actual_person = app.get_next_person(user)

    # Assert
    assert actual_person == expected_person
