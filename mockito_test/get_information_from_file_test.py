import json
import builtins
from mockito import when, mock
from src.TindevQA import TindevQA


def test_get_valid_json():
    app = TindevQA()
    filename = "configuration.json"
    expected_result = {'name': 'Leia', 'likes': ['Han Solo'], 'dislikes': ['Luke']}

    mock_file = mock()
    when(mock_file).read().thenReturn('{"name": "Leia", "likes": ["Han Solo"], "dislikes": ["Luke"]}')
    when(builtins).open(filename).thenReturn(mock_file)
    actual_result = app.get_information_from_file(filename)
    assert expected_result == actual_result


def test_get_information_ioerror():

    app = TindevQA()
    filename = "configuration.json"
    when(builtins.open(filename)).read().thenRaise(IOError)
    actual_result = app.get_information_from_file(filename)

    assert actual_result == "ERROR"


def test_get_information_valueerror():
    app = TindevQA()
    filename = "configuration.json"
    when(json).loads(...).thenRaise(ValueError)

    actual_result = app.get_information_from_file(filename)

    assert actual_result == "ERROR"
