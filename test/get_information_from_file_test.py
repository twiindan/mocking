from mock import patch, Mock

from src.TindevQA import TindevQA


@patch("builtins.open")
def test_get_valid_json(mock_open):
    app = TindevQA()
    filename = "configuration.json"
    expected_result = {'name': 'Leia', 'likes': ['Han Solo'], 'dislikes': ['Luke']}

    mock_file = Mock()
    mock_file.read.return_value = '{"name": "Leia", "likes": ["Han Solo"], "dislikes": ["Luke"]}'
    mock_open.return_value = mock_file

    actual_result = app.get_information_from_file(filename)

    assert actual_result == expected_result


@patch("builtins.open")
def test_get_information_ioerror(mock_open):
    app = TindevQA()
    filename = "configuration.json"

    mock_open.side_effect = IOError

    actual_result = app.get_information_from_file(filename)

    assert actual_result == "ERROR"


@patch("json.loads")
@patch("builtins.open")
def test_get_information_valueerror(mock_open, mock_loads):
    app = TindevQA()
    filename = "configuration.json"

    mock_file = Mock()
    mock_file.read.return_value = '{"name": "Leia", "likes": ["Han Solo"], "dislikes": ["Luke"]}'
    mock_open.return_value = mock_file
    mock_loads.side_effect = ValueError

    actual_result = app.get_information_from_file(filename)

    assert actual_result == "ERROR"
