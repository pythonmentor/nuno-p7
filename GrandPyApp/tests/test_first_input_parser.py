# from GrandPyApp.scripts import first_input_parser as first
import scripts.first_input_parser as first


def test_parse_user_input():
    test_user_input = "Bonjour GrandPy peut-tu me donner l'adresse d'openclassrooms stp ?"
    assert first.parse_user_input(test_user_input) == [
        "bonjour",
        "adresse",
        "openclassrooms"
        ]


def test_parse_user_input_empty():
    test_user_input = " "
    assert first.parse_user_input(test_user_input) == []


def test_important_words():
    test_user_input = "Bonjour GrandPy peut-tu me donner l'adresse d'openclassrooms stp ?"
    assert first.important_words(test_user_input) == "openclassrooms"

