from ..scripts_py import first_input_parser as first
# import scripts.first_input_parser as first


def test_parse_user_input():
    test_user_input = "Bonjour GrandPy peut-tu me donner"\
        " l'adresse d'openclassrooms stp?"
    assert first.parse_user_input(test_user_input) == [
        "bonjour",
        "adresse",
        "openclassrooms"
        ]


def test_parse_user_input_empty():
    test_empty_user_input = " "
    assert first.parse_user_input(test_empty_user_input) == []


def test_important_words():
    test_user_input = "Bonjour GrandPy peut-tu me donner l'adresse"\
        " d'openclassrooms stp?"
    test_first_pass = first.parse_user_input(test_user_input)
    assert first.important_words(test_first_pass) == "openclassrooms"


def test_important_words_2():
    test_user_input_2 = "Salut GrandPy peut-tu me dire ou se trouve"\
        " la Tour Eiffel S'il te plait?"
    test_second_pass = first.parse_user_input(test_user_input_2)
    assert first.important_words(test_second_pass) == "tour eiffel"


def test_important_words_3():
    test_user_input_3 = "Hi, peut-tu me trouver ou se situe la ville"\
        " de Porto au Portugal stp?"
    test_third_pass = first.parse_user_input(test_user_input_3)
    assert first.important_words(test_third_pass) == "ville porto portugal"


def test_important_words_4():
    test_empty_user_input = " "
    assert first.important_words(test_empty_user_input) == " "
