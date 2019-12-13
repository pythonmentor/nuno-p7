from GrandPyApp.first_input_parser import parse_user_input, important_words
from GrandPyApp.views import stop_words_custom, words_to_remove


def test_parse_user_input():
    test_user_input = "Bonjour GrandPy peut-tu me donner"\
        " l'adresse d'openclassrooms stp?"
    assert parse_user_input(test_user_input, stop_words_custom) == [
        "bonjour",
        "adresse",
        "openclassrooms"
        ]


def test_parse_user_input_empty():
    test_empty_user_input = " "
    assert parse_user_input(test_empty_user_input, stop_words_custom) == []


def test_important_words():
    test_user_input = "Bonjour GrandPy peut-tu me donner l'adresse"\
        " d'openclassrooms stp?"
    test_first_pass = parse_user_input(test_user_input, stop_words_custom)
    assert important_words(test_first_pass, words_to_remove) == "openclassrooms"


def test_important_words_2():
    test_user_input_2 = "Salut GrandPy peut-tu me dire ou se trouve"\
        " la Tour Eiffel S'il te plait?"
    test_second_pass = parse_user_input(test_user_input_2, stop_words_custom)
    assert important_words(test_second_pass, words_to_remove) == "tour eiffel"


def test_important_words_3():
    test_user_input_3 = "Hi, peut-tu me trouver ou se situe la ville"\
        " de Porto au Portugal stp?"
    test_third_pass = parse_user_input(test_user_input_3, stop_words_custom)
    assert important_words(test_third_pass, words_to_remove) == "ville porto portugal"


def test_important_words_4():
    test_empty_user_input = " "
    assert important_words(test_empty_user_input, words_to_remove) == " "
