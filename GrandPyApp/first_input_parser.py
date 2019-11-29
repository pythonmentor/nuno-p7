import re
import string
from .views import app

app.config.from_object('config')


def parse_user_input(user_input):
    """
    Get and parse user's sentences.
    """
    _punctuation = set(string.punctuation)
    for punct in set(user_input).intersection(_punctuation):
        user_input = user_input.replace(punct, ' ')
    user_input = ' '.join(user_input.split())

    user_input = re.split(",|'| |-|;", user_input)
    user_input = [x.lower() for x in user_input]

    stop_words_custom = app.config['STOP_WORDS']
    new_sentence = []

    for word in user_input:
        if word not in stop_words_custom:
            if len(word) > 2:
                if word[-2:] != "er":
                    new_sentence.append(word)
    return new_sentence


def important_words(parsed_sentence):
    """
    Get a positionement word
    """
    words_to_remove = app.config['WORDS_TO_REMOVE']
    new_sentence = []
    for word in parsed_sentence:
        if word not in words_to_remove:
            new_sentence.append(word)
    title = ' '.join(new_sentence)

    return title


if __name__ == "__main__":

    print("Salut, je suis GrandPy, je suis là afin de t'aider ;-)")

    while True:
        user_input = input('Que veux-tu savoir mon enfant?  :  ')
        parsed_user_input = parse_user_input(user_input)

        if len(parsed_user_input) >= 1:
            print("Mots a envoyer", parsed_user_input)
            break
        else:
            continue
