import GrandPy.static.scripts.first_input_parser as first


def test_parse_user_input():
    user_input = "Bonjour GrandPy peut-tu me donner l'adresse d'openclassrooms stp ?"
    assert first.parse_user_input(user_input) == [
        "bonjour",
        "adresse",
        "openclassrooms"
        ]
