from GrandPyApp import first_input_parser as first
from .config import STOP_WORDS


stop_words_custom = STOP_WORDS


def test_parse_user_input():
    test_user_input = "Bonjour GrandPy peut-tu me donner"\
        " l'adresse d'openclassrooms stp?"
    assert first.parse_user_input(
        test_user_input,
        stop_words_custom) == "openclassrooms"


def test_parse_user_input_empty():
    test_empty_user_input = " "
    assert first.parse_user_input(
        test_empty_user_input, stop_words_custom) == []
