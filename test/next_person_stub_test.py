from src.TindevQA import TindevQA
from mock import patch, Mock


@patch("src.TindevQA.TindevQA.get_random_user")
def test_new_person_decorator(mock_get_random_user):
    # Arrange
    app = TindevQA()
    user = {'people_seen': []}
    expected_person = 'Alexandra'
    mock_get_random_user.return_value = 'Alexandra'

    # Action
    actual_person = app.get_next_person(user)

    # Assert
    assert actual_person == expected_person


def test_new_person():
    # Arrange
    app = TindevQA()
    user = {'people_seen': []}
    expected_person = 'Alexandra'
    app.get_random_user = Mock()
    app.get_random_user.return_value = 'Alexandra'

    # Action
    actual_person = app.get_next_person(user)

    # Assert
    assert actual_person == expected_person


def test_new_person_context_manager():
    with patch.object(TindevQA, "get_random_user") as mock_get_random_user:
        # Arrange
        app = TindevQA()
        user = {'people_seen': []}
        expected_person = 'Alexandra'
        mock_get_random_user.return_value = 'Alexandra'

        # Action
        actual_person = app.get_next_person(user)

        # Assert
        assert actual_person == expected_person


@patch.object(TindevQA, "get_random_user")
def test_new_person_several_times(mock_get_random_user):

    app = TindevQA()
    user = {'people_seen': ['Sara', 'Alexandra']}
    expected_person = 'Leia'
    mock_get_random_user.side_effect = ['Alexandra', 'Sara', 'Leia']

    # Action
    actual_person = app.get_next_person(user)

    # Assert
    assert actual_person == expected_person
